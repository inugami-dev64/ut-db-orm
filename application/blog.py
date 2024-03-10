from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .database import db
from application.auth import login_required
from application.models.Post import Post
from application.models.User import User
from application.models.Comment import Comment

bp = Blueprint('blog', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    query = None
    if request.method == 'POST':
        query = request.form['query']

    posts = search(query)

    return render_template('blog/index.html', posts=posts)

def search(query):
    #TODO implement filtering (the hint is in the name ;) )
    #PS: filter by title ;)
    posts = list(map(
        lambda o: Post.withUser(o[1], o[0]),
        db.session.query(User, Post).filter(User.id == Post.author_id).all())
    )
    #Hint: you need to filter after the first filter ;)

    return posts

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            c1 = Post(title=title, body=body, author_id=g.user['id'])

            db.session.add(c1)
            db.session.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = None #TODO implement me (you probably need to google [get SQLAlchemy object by id])

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post.author_id != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            #TODO implement
            #remember, we already have teh post object ;)

            db.session.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blog.index'))