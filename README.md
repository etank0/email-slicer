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

<a href="https://flask.palletsprojects.com/en/2.1.x/installation/#python-version"><img src = "https://user-images.githubusercontent.com/89385145/231574201-a823f3ec-ff4b-47f0-9677-6eb74c020cfd.png" height = "300px"></a>

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
 
 This is the folder where you can put files that you would like to add in your website. I have an image i.e. "bg.jpg" which is used as the background for my html file. I also have a 'styles.css' file that is used for styling.
 
 ## Result
 
 Let's look at how the website looks and functions.
 
 ### Running app.py from terminal

![Screen2](https://user-images.githubusercontent.com/89385145/189984487-dde80b8c-f306-41a3-973d-b3df8a77db1d.jpg)


 ### Fresh in Firefox
 
![Screenshot from 2022-12-02 01-34-49](https://user-images.githubusercontent.com/89385145/205149698-f5ce7c34-10c6-4568-bda2-8939dd692e3c.png)

 ### Result after entering Email
 
 ![Screenshot from 2022-12-02 01-36-47](https://user-images.githubusercontent.com/89385145/205149762-f4bef393-ded2-424c-bbb4-6e1c1ef3e3b2.png)

