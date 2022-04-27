# Entry 5
##### 04/26/2022

## Content
Through the past week, I have finish my MVP which includes Unit 1 - 10 of the APCSA course. For reminders, our tool is ***CS50***, specifically Flask and Python. I have recently started to learn about deploying our project. 

#### Finishing MVP
To finish my MVP, I had to add the content from Unit 1 to 10 since I already set up Flask in the MVP and coded the side bar that the user will use to navigate through the study guide. I mainly used my notes that I took when going through the lesson from Project Stem and I try my best to kind the lesson togther rather than copying exactly from Project Stem. This part was easy but it was extemely tedious. And I had to review css and html markups. Mainly, my code look like this:
```c#
<html lang="en">
    <head>
        <link rel="stylesheet" type="text/css" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    table {
      border-collapse: collapse;
      width: 100%;
    }

    td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }
    </style>   
    </head>
{% extends "base.html" %}

{% block content %}
        <h1>Unit 10: Recursion</h1>
        
        <h3>All about Recursion</h3>
        <h4>What is recursion?</h4>
        <body>What make methods classify as recursion methods is that it <b>CALLS ITSELF</b>. Recursion risks never stopping so it is important for a base to exist. In other words an input for which there will be no recursive call, and that each recursive call moves you closer to the base case. When the recursive call comes before the print statement, the output will be LIFO, which stands for last-in-first-out. When the print statement is after the recursive call like this, it’s like walking downstairs and leaving a piece of information on each step. When we reach the bottom (the base case), we turn around and walk back up the stairs, meaning that we’ll read off the information on the lowest step first (which was the last piece of information added). Anything done by recursion can also be done by iteration and vice versa. However, choosing to do iterations or recursion is not always clear</body>
...
        
{% endblock %}
</html>
```
Because all the units templates needed the side bar so I used Flask Template Inheritance as mentioned in my last blog. All of my contents for the unit are between `{% block content %}` and `{% endblock %} `. `{% extends "base.html" %}` basically connects the current unit template (in the code above, it is unit 10) to the base template. Here's a screen shot of unit 10 with all the info.
<img width="1440" alt="Screen Shot 2022-04-26 at 11 18 49 PM" src="https://user-images.githubusercontent.com/56265188/165433064-9d2da8b8-2e63-4d4d-964a-0112196e2e7d.png">

#### Deploy in Flask
I have recently started to learn about deploying a flask app. I decided to deploy my app on [Heroku](https://www.heroku.com/). To help me understand this procress better, I used:
- [The Flask Mega-Tutorial Part XVIII: Deployment on Heroku](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku) 
- [Codemy.com: Push Flask Apps To Heroku For Webhosting - Python and Flask #11](https://www.youtube.com/watch?v=Li0Abz-KT78) video so that I can see how the process is like visually

So far the notes I have taken:
Heroku is basically a cloud platform that support several programming languages including Python. My main usage of Heroku is using it so that my app has a URL this everyone will be able to have access to my app.

- To deploy to Heroku, you have to install Heroku CLI and create a Heroku account
- Then type `heroku login` where you will be asked to input your email address and password
- Next Create a new Git repository using:
 ```c#
$ cd my-project/
$ git init
$ heroku git:remote -a apcsa-fp
```
OR if you have an Existing Git repository, you can just use:` $ heroku git:remote -a apcsa-fp`. NOTE that it says `apcsa-fp`; that is because I created an app in my heroku account
- Last, you Commit your code to the repository and deploy it to Heroku using Git like this:
```c#
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

## Engineering Design Process / Skills
In the Engineering Design Process, I would say I am on ***Testing and evaluating the prototype*** and going into ***Improving as needed***. There are some areas that can be improved and make the application more aesthetically pleasing. Obviously, my application is functioning however it is not deployed yet and I also have to check for grammar mistakes in the application. 

The skills I used this time was ***Consideration*** and ***Growth Mindset***. While reviewing contents in Project Stem, I realized that some info in Project Stem jumps around which gets annoying. Taking into that in consideration, I decided to group info based on the content topic. I also improved my Growth Mindset. Adding the content was tedious because it was a lot of info to organized, set up, and then write into the template. In some moments, I wanted to scream but I took a break, came back, and kept on working on it. 

### Next Steps
My next step obviously would be to deploy my web application. Overall, I am proud of my progress. 


[Previous](entry04.md) | [Next](entry06.md)

[Home](../README.md)
