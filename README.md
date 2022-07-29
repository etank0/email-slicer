# email-slicer
### ( Python Mini Project )

In this project I have made a webpage that will take an email address as an  input and show us the "Email Username", "Email Domain" and "Suggested Username".
I have used Flask as backend, the website will be hosted on a local server, which we can view in a browser.

## Table of Contents

- [Setup](#Setup)
- [Files](#Files)
- [Result](#Result)

## Setup

In setup, you have to install flask and set up a virtual environment having all the required dependencies. All is explained on the Flask website :

<a href="https://flask.palletsprojects.com/en/2.1.x/installation/#python-version"><img src="https://flask.palletsprojects.com/en/2.1.x/_static/flask-icon.png"></a>

## Files

Files needed here are inside "myproject" folder as mentioned on the above linked webpage.(Please follow all the steps mentioned on the flask website and then follow.)
 
 ### app.py
 
 This is our main Python file. The email-slicer code is here and the result or returned output is going to be displayed on our website.
 
 ```txt
 Below lines of my Python file are the most important.
 
       email = email.strip()  #getting rid of unnecessary spaces
       email1 = email.split("@")[0]  #splitting the string at '@" symbol 
       domain = email.split("@")[1]  #assigning domain address to a variable
```
 
 ### templates
 
 This is the folder where we will keep our Html files. I have only used one page i.e. "index.html". You can have more.
 
 ### static
 
 This is the folder where you can put files that you would like to add in your website. I have only image i.e. "bg.jpg" which is used as the background for my html file.
 
 ## Result
 
 Let's look at how our website looks and functions.
 
 ### Running app.py from terminal
 
 (https://github.com/etank0/email-slicer/tree/main/images/11.jpg?raw=true)
  
 ### Fresh in Firefox
 
 (https://github.com/etank0/email-slicer/tree/main/images/12.jpg?raw=true)
 
 ### After Entering Email
 
(https://github.com/etank0/email-slicer/tree/main/images/13.jpg?raw=true)
 
 ### Final Result
 
 (https://github.com/etank0/email-slicer/tree/main/images/14.jpg?raw=true)
 

