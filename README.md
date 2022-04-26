<h1>Developer and Databeses 102 (Assignment 2)</h1>

**Greetings, wanderer!** We meet again... this time, as promised we will take a look inside world of ORMs and try it out ourselves.




<h2>Assignment 2 (In detail)</h2>

<hr>
<div style="background-color: rgba(82,63,63,0.78); padding: 0.1rem 1rem; border-radius: 20px">

Now to the main part of this exercise... ORM ([Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)).

ORM offers us a nice way to describe our database inside our code, which also unites the database objects with the back-end objects.

ORM makes it easy to maintain models and develop fast and reliably.

The main trade-off with ORM is that it does not perform queries as fast as native SQL scripts and can it can have difficulties when implementing niche models/relations.
The latter and sometimes the first can be averted by adding custom SQL to problematic pieces.


As with all things IT, there is no clear benefit but the decision should be made considering the complexity and the required time of a certain system.

We will also implement ORM in our project, for this we use SQLAlchemy, the most popular ORM for python.
</div>
<h3>NB! To start Assignmet 2 checkout to branch "assignment2"!</h3>
<hr>

<h2>Deliverables</h2>
The end result should pass all tests that are written for you. There is no point in fooling said tests as they are only there for your benefit!
<h6>For instructions on running tests, look below</h6>
If all is well, share the repository with your lab supervisor for POINTS.

<h2>Running tests</h2>
If all assignments are done correctly then all tests should pass.
(You can also run the tests inside PyCharm, it makes no difference.)
```bash
 python -m pytest tests
```
