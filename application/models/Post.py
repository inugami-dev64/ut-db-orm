from sqlalchemy import func

from ..database import db


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='post', lazy='joined')

    username = ''

    def __init__(self, title, body, author_id):
        self.title = title
        self.body = body
        self.author_id = author_id

    @staticmethod
    def withUser(post, user):
        return {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'created': post.created,
            'author_id': post.author_id,
            'username': user.username,
            'comments': [{'id': comment.id, 'body': comment.body} for comment in post.comments],

        }
