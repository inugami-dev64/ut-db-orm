import os
from flask import Flask

from . import auth
from . import blog
from .database import db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, instance_relative_config=True)

app.debug = True

app.config['DATABASE'] = os.path.join(app.root_path, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'dev'
app.config['SECRET_KEY'] = 'dev'

db.init_app(app)

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


app.register_blueprint(auth.bp)

app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')

# Only use for initializing the db
# db.create_all()
# db.session.commit()
