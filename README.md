# email-slicer
### ( Python Mini Project )

In this project I have made a webpage that will take an email address as an  input and show us the "Email Username", "Email Domain" and "Suggested Username".
I have used Flask as backend, the website will be hosted on a local server, which we can view in any browser.

## Table of Contents

- [Setup](#Setup)
- [Files](#Files)
- [Result](#Result)

## Setup

In setup, you have to install flask and set up a virtual environment having all the required dependencies. Everything is explained on the Flask website :

<a href="https://flask.palletsprojects.com/en/2.1.x/installation/#python-version"><img src="https://flask.palletsprojects.com/en/2.1.x/_static/flask-icon.png"></a>

## Files

Files needed here are inside "myproject" folder as mentioned on the above linked webpage.(Please follow all the steps mentioned on the flask website and then come back and continue.)
 
 ### app.py
 
 This is our main Python file. The email-slicer code is here and the result or returned output is going to be displayed on our website.
 
 ```python3
 #Below lines of my Python file are the most important.
 
       email = email.strip()  #getting rid of unnecessary spaces
       email1 = email.split("@")[0]  #splitting the string at '@" symbol 
       domain = email.split("@")[1]  #assigning domain address to a variable
```
 
 ### templates
 
 This is the folder where we will keep our Html files. I have only used one page i.e. "index.html". You can have more.
 
 ### static
 
 This is the folder where you can put files that you would like to add in your website. I have an image i.e. "bg.jpg" which is used as the background for my html file. I also have a 'styles.css' file that is use for styling.
 
 ## Result
 
 Let's look at how the website looks and functions.
 
 ### Running app.py from terminal

![Screen2](https://user-images.githubusercontent.com/89385145/189984487-dde80b8c-f306-41a3-973d-b3df8a77db1d.jpg)

 ### Fresh in Firefox

![Screen1](https://user-images.githubusercontent.com/89385145/189984628-bf7bc304-37cb-4788-95b4-995534d36b9d.jpg)

 ### After Entering Email
 
![new2](https://user-images.githubusercontent.com/89385145/181860855-ad0b34f9-e6a3-4180-9b5f-d51a119be7ce.jpg)

 ### Final Result
 
 ![new3](https://user-images.githubusercontent.com/89385145/181860865-a415b8b2-6340-48f5-af88-7c73f2061f1a.jpg)
