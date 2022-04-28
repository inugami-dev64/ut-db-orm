from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from application.auth import login_required

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    from application import Post, User, db

    if request.method == 'POST':
        query = request.form['query']
        posts = search(query)

    else:
        posts = list(map(
            lambda o: Post.withUser(o[1], o[0]),
            db.session.query(User, Post).filter(User.id == Post.author_id).all())
        )

    return render_template('blog/index.html', posts=posts)

def search(query):
    from application import Post, User, db
    #TODO implement filtering (the hint is in the name ;) )
    posts = list(map(
        lambda o: Post.withUser(o[1], o[0]),
        db.session.query(User, Post).filter(User.id == Post.author_id).all())
    )

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
            from application import Post, db
            c1 = Post(title=title, body=body, author_id=g.user['id'])

            db.session.add(c1)
            db.session.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    from application import Post

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
            from application import Post, db
            #TODO implement
            #remember, we already have teh post object ;)

            db.session.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    from application import Post, db
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blog.index'))