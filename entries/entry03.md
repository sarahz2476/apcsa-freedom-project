# Entry 3
##### 02/13/2021

## Content
For the pass weeks, I have been focusing on learning about my freedom project tool, [CS50](https://cs50.harvard.edu/college/2021/fall/). Just to reiterate what Nina and mine project is about, we are using **CS50** to create a **Study Guide for the APCSA** I have been focusing on [Week 9: Flask](https://cs50.harvard.edu/college/2021/fall/weeks/9/).

### Basic Notes for Flask
Flask is a Web Server Gateway Interface (WSGI) framework which is a library of codes that comes with a set of conventions for how it should be used. A function that flask has is that we can parse request. The flask requires out codes to be organized with:
- `app.py` -> this is where the python code will be at
- `requirements.py` -> a list of required libraries in our web application
- `static/` -> a directory of static files which includes images and CSS and JavaScript files
- `templates/` -> a directory for HTML files that will form web pages

A basic `app.py` template look like:
```c#
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
```
- the `from flask import Flask` imports `Flask` from the flask libraries
- `app` is the python file's name which will also be the flask variable's name 
- `@app.route("/")` -> this will label a function for the `/` route. The `@app.route` is from Flask and the `@` modifies a function
- the `index()` is a function that will render a template from `index.html`

As I did more research about flask I found a [web page about flask](https://www.tutorialspoint.com/flask/flask_overview.htm) which includes many functions of flask. Obviously, I did not go through all of them. I think it would be the best to start my freedom project first and then develop my understanding of flask if needed for my application since I have a limited amount of time. But I was very surprise with how much content flask has.

I made a [small program](https://ide-6bbb60f064c04a0292e9d817cdb2daf9-8080.cs50.ws/) to help me understand Flask. Basically, I wanted to get the user's age, name, and school which I will use to greet them. My app.py code look like this:
```c#
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/greet")
def greet():
    name = request.args.get("name")
    age = request.args.get("age")
    school = request.args.get("school")
    return render_template("greet.html", name = name, age = age, school = school)

```
For my html page, I used ` Hey {{name}}, from {{school}}. I see that you are {{age}} years old. Nice to meet you!`. This looks logical because this what the professor did to get the name. However my result print `Hey None, from None. I see that you are None years old. Nice to meet you!` no matter what I typed. Therefore, I had to go back to the video and realized that I made a syntax error. In my index.html, the code that got did not have my desired result looks like this:
```c#
<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="stylesheet" href="../style.css" type="text/css">
        <meta name = "viewpoint" content = "initial-scale = 1", "wide = device-width">
        <title>Hello</title>
    </head>    
    <body>
        <form action = "/greet" methods = "get">
            <input autocomplete = "off" autofocus  = "name" placeholder = "Name" type = "text">
            <input autocomplete = "off" autofocus  = "age" placeholder = "Age" type = "text">
            <input autocomplete = "off" autofocus  = "school" placeholder = "School" type = "text">
            <input type = "submit">
        </form>
        <script src="../script.js"></script>
    </body>    
</html>
```
While the correct code is:
```c#
<!DOCTYPE html>
<html lang="en"> 
    <head>
        <link rel="stylesheet" href="../style.css" type="text/css">
        <meta name = "viewpoint" content = "initial-scale = 1", "wide = device-width">
        <title>Hello</title>
    </head>
        
    <body>
        <form action = "/greet" methods = "get">
            <input autocomplete = "off" autofocus name = "name" placeholder = "Name" type = "text">
            <input autocomplete = "off" autofocus name = "age" placeholder = "Age" type = "text">
            <input autocomplete = "off" autofocus name = "school" placeholder = "School" type = "text">
            <input type = "submit">
        </form>
        <script src="../script.js"></script>
    </body>    
</html>
```
The error was that I did not add `name` to `autofocus name`. In a way it did helped me understand flask more because I started to google things ups. I found a method that can print without connecting it to a html file.

Another thing to remember is that to run programs with flask, you have to use `flask run`. Once you type this in, you will be returned with a link and once you press the link, you will get to the web page. I think this is something to keep in mind because after my research, I realized I had no idea how to run it so I had to go back and check.


### Engineering Design Process
In the Engineering Design Process, I say I would be between **Plan the most promising solution and Create a prototype**. Me and partner have started to discuss where we would start. I suggested we start with html just to have a basic template of what out project might look like and then add in the back-ends functions. The product we had in mind is:
 - front page -> would have a overview of the APCSA course
 - the units would be on the side bars OR the units would be on the top of the page and the units will be on the side. 

### Skills
The skills I used this time was **How to Google** and **Time management**. I googled other resources about flask which helped me understand flask a little more and how funcational flask was. With the large content that flask was I realized that learning all of them is pribably not the best use of time since I might not even use some of the functions, thus I try to prioritize learning the basics of flask and brainstorming my first prototype and how I would start it. I will learn more about flask when needed to. The webpage I found through googling definitely will be a big help since it separate flask contents into different section. In the future, if I need to specfic content of flask, this would save so much time.  

## Next Steps!! 
The next step for us is to actually start our prototype. We would also outline what out MVP is to better help us understand what part we should focus on the most. I think it would be the best to start coding and learn more about cs50 through this. I am pretty excited about it since I do have some ideas in minds. I do hope that we can finish out study guide before the AP exam since it can also help us review in a way. Hopefully, everything goes well!

[Previous](entry02.md) | [Next](entry04.md)

[Home](../README.md)
