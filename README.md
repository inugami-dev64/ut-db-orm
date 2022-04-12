<h1>Developer and Databeses 101</h1>

**Greetings, wanderer!** You have found yourself on a quest to get to know more about the life of a database and how it is used in "real life".
Keep in mind that this is only one of many uses for a database. Development being the most common usa we will be talking about just that. And ofcourse you will have plenty of opporunities to make your hands dirty. 

Note that this application is not ment to look "nice" or give the best user experience but only to give you an **insight into databases in development**.

Furthermore, this application uses rather old way of designing an application (<u>monolithic architecture</u>).
This is not to say it is good or bad, although nowadays using <u>microservice architecture</u> is much more common, the main thing here is that you get to know databases and get some experience using them in application development.

It is also recommended googling the underlined words ;).

<h2>Setup</h2>
To run the application you must first setup environment variables like so:
<h4>Mac</h4>
```bash
$ export FLASK_APP=application
$ export FLASK_ENV=development
```

<h4>Linux</h4>
```bash
> set FLASK_APP=application
> set FLASK_ENV=development
```

<h4>Windows</h4>
```bash
> $env:FLASK_APP = "application"
> $env:FLASK_ENV = "development"
```

<h3>Init DB</h3>
```bash
flask init-db
```
<h3>Run</h3>
```bash
flask run
```

<h2>Assignment 0</h2>
* Read the before manual, start the application 
(default port is 5000, if you waht to change that, use `flask run --host=0.0.0.0 --port=80`)
* Register an account
* Log in
* Create a post
* Try to edit a post (THIS SHOULDN'T WORK)

<h2>Assignment 1</h2>
Your first task is to implement SQL queries `get_post` and `update` inside application/blog.py.
Tip: Look at `index` and `create` functions respectively.
* Implement beforementioned SQL scripts
* Try to edit a post again, now it should be working, if not, you did something wrong!

<br>
<div style="background-color: rgba(82,63,63,0.78); padding: 0.1rem 1rem; border-radius: 20px">

Now to the main part of this exercise... ORM ([Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)).

ORM offers us a nice way to describe our database inside our code, which also unites the database objects with the back-end objects.

ORM makes it easy to maintain models and develop fast and reliably.

The main trade-off with ORM is that it does not perform queries as fast as native SQL scripts and can it can have difficulties when implementing niche models/relations.
The latter and sometimes the first can be averted by adding custom SQL to problematic pieces.


As with all things IT, there is no clear benefit but the decision should be made considering the complexity and the required time of a certain system.

We will also implement ORM in our project, for this we use SQLAlchemy, the most popular ORM for python.
</div>



<h2>Assignment 2</h2>


<h2>Deliverables</h2>
The end result should pass all tests that are written for you. There is no point in fooling said tests as they are only there for your benefit!
######For instructions on running tests, look below
If all is well, please send your code to your supervisor in Discord in ZIP format.

<h2>Running tests</h2>
If all assignments are done correctly then all tests should pass.
(You can also run the tests inside PyCharm, it makes no difference.)
```bash
 python -m pytest tests
```
