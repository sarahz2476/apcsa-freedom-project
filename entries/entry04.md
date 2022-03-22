# Entry 4
##### 03/21/2022

## Content 
Through the past weeks, I have been focusing learning about Flask, starting my MVP, and incorporating Flask onto my freedom project. For context, Nina and I are using **CS50** to create a **Study Guide for the APCSA**. The user will be able to review informations on certain units based on which units they clicked on the side bar.

Using the [The Mega-Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) I am able to further understand:
- Setting up Flask
- Flask routing
- [Flask Template Inheritance](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)

#### Setting up Flask
Setting up flask was very confusing to me. I did not quite understand if I can use Flask immediately in my CS50 IDE or if I had to download Flask or Python. I somewhat skipped this part when I first started and try to set up other flask functions. After reviewing this with my teacher using the The Mega-Flask Tutorial, I was able to understand how. Basically CS50 IDE already has Python but we need to download Flask. 

Before setting up Flask, make sure your have Python and created a directory where your project will be in. After that, you should set up a virtual environment in the terminal using `$ python3 -m venv venv` and activate it with `$ source venv/bin/activate`. This will allow you to install Flask without messing up your computer.

You install Flask  with `(venv) $ pip install flask`. To check if Flask in installed in the virtual environment, input `>>> import flask` and if there is no errors then Flask has successfully installed and you can start. 

My set up for my project is that I have an app directory which contains guide.py, my static directory, and templates directory. My static directory only contains an image. On the other hand, the templates directory contains all the html files including the basic template of each units, each unit templates,  \_.init.\_py file and routes.py file.

We set up a \_.init.\_py  file to create a package which can be imported. The \_.init.\_py look like this:
```#C
from flask import Flask

app = Flask(__name__)

from app import routes
```
The code above basically creates the application object as an instance of class Flask imported from the flask package. The \__name\__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used. For some reason, passing \__name\__ is almost always going to configure Flask in the correct way. Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files, which will be explained later. The application then imports the routes module (which will also be explained later). 

*Important:* Before running Flask, Flask needs to be told how to import it, by setting the FLASK_APP environment variable: `(venv) $ export FLASK_APP=guide.py` However because  environment variables aren't remembered across terminal sessions, we need to input `(venv) $ pip install python-dotenv`

#### Flask Route
The next part would be Flask Routing. I set up my routes.py like this: 
```#C
from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/unit1')
def unit1():
    return render_template('unit_1.html')
    
@app.route('/unit2')
def unit2():
    return render_template('unit_2.html')
<! –– this is part of it because the rest is too long and it is in a similar format ––>   
```
In the code above, the `@app.route()` decorator creates an association between the URL given as an argument and the function. So for example, for `@app.route('/')` and `@app.route('/home')`, if the URL request these two web browser it would invoke the function to return the home.html template through the function `render_template('home.html')` In the html file, I would link the unit with the same name of the parameter in my `@app.route()` to make my side bar work.
```#C
   <div><a href = "/home">Home</a></div>
   <div><a href = "/unit1">Unit 1: Primitive Types</a></div>
   <div><a href = "/unit2">Unit 2: Using Objects</a></div>
   <div><a href = "/unit3">Unit 3: Boolean Expressions / If statements</a></div>
   <div><a href = "/unit4">Unit 4: Iteration</a></div>
   <div><a href = "/unit5">Unit 5: Writing Classes</a></div>
   <div><a href = "/unit6">Unit 6: Array</a></div>
   <div><a href = "/unit7">Unit 7: ArrayList</a></div>
   <div><a href = "/unit8">Unit 8: 2D Array</a></div>
   <div><a href = "/unit9">Unit 9: Inheritance</a></div>
   <div><a href = "/unit10">Unit 10: Recursion</a></div>
```
Thus when the user clicks to Unit 3 it would bring them to Unit 3 templates where all the content should be in. 

#### Flask Template Inheritance
My projects has a lot of templates and I would need each templates to require the side bar. However, it is very very very time consuming to make the same copy of same bar in 11 diffrent template.  Thus I use Template Inheritance. Basically you can have a base.html where it include parts of the page layouts that are common in every template and uses blocks so that derived templates can override it. Thus containing the common parts but also include new parts specfic to specfic templates

So for my project my base.html template looks like:
```#C
...
</style>   
    </head>
    <body>
        <div class="sidebar">
            <div><a href = "/home">Home</a></div>
            <div><a href = "/unit1">Unit 1: Primitive Types</a></div>
            <div><a href = "/unit2">Unit 2: Using Objects</a></div>
            <div><a href = "/unit3">Unit 3: Boolean Expressions / If statements</a></div>
            <div><a href = "/unit4">Unit 4: Iteration</a></div>
            <div><a href = "/unit5">Unit 5: Writing Classes</a></div>
            <div><a href = "/unit6">Unit 6: Array</a></div>
            <div><a href = "/unit7">Unit 7: ArrayList</a></div>
            <div><a href = "/unit8">Unit 8: 2D Array</a></div>
            <div><a href = "/unit9">Unit 9: Inheritance</a></div>
            <div><a href = "/unit10">Unit 10: Recursion</a></div>
        </div>
       <div class ="content">
           {% block content %}{% endblock %}
       </div>

    </body>
    
</html>
```
The `block` control statement defines the place where the derived templates can insert themselves. Blocks are given a unique name, which derived templates can reference when they provide their content. Now instead of having a long html file that inludes the code for side bar and specfic units, the code would be way shorter and looks something like this:
```#C
{% extends "base.html" %}

{% block content %}
        <style>
                
        </style>
        <h1>Welcome to the APCSA Course Study Guide!</h1>
        <hr>
        <h3>In this course, we will be reviewing about......</h3>
        <center><img src="../static/JAVA.jpg" alt = "java" width = "45%" height = "auto" ></center>
        <h3>We will be reviewing about:</h3>
        <ol>
                <li>Primitive Types</li>
                <li>Using Objects</li>
                <li>Boolean Expressions / If statements</li>
                <li>Iteration</li>
                <li>Writing Classes</li>
                <li>Array</li>
                <li>ArrayList</li>
                <li>2D Array</li>
                <li>Inheritance</li>
                <li>Recursion</li>
        </ol>
{% endblock %}
```
Notice that the new layout you are coding is between `{% block content %}` and `{% endblock %}` and remember that it shoudl alway be in between `{% block content %}` and `{% endblock %}` for new layouts. In the beginning I kept getting error even though I check the syntax and everything look fine. The Flask Mega Tutorial has exact format. I then realized it was because I include `{% endfor %}` which is NOT suppose to be included.

#### Results:
*Home page*:

<img width="1437" alt="Screen Shot 2022-03-21 at 9 46 37 PM" src="https://user-images.githubusercontent.com/56265188/159397436-8bdefbb1-56cb-46b5-8881-4e4e2899bd6d.png">

*Unit 1 page (not done) but you can see that the side bar is there, even though we have not phyically code it in that specific template.*

<img width="1433" alt="Screen Shot 2022-03-21 at 9 47 10 PM" src="https://user-images.githubusercontent.com/56265188/159397386-fe4673ae-de2b-4a2b-bb20-2d5338c5cf95.png">

## Engineering Design Process/ Skills
In the Engineering Design Process, I'm currently at **Creating the Prototype**. I've been learning my tool while applying what I learn to make my MVP. Flask has definitely made building my web application easier and more time efficient. As I finish up my MVP, I hope I can explore more of Flask and use it to incorprate little quizzes into my freedom project. 

In the past week, I've learn **Organization** and paying **Attention to details**. With many templates and files I had to make sure I group the files in the correct directory which helps with referring to different files. Because each unit is link to its own template, if you spell something wrong or forgot to add something, the routing would fail. Thus it is important to stay focus and pay attention.

## Next Steps
My next steps would be to add the contents of each units in. There is definitely lots of informations to organize. This process is probably going to take pretty long but I hope I get it done sooner so I can get to the beyond MVP parts because I am excited to explore other flask functions

[Previous](entry03.md) | [Next](entry05.md)

[Home](../README.md)
