from flask import Flask, request, render_template, url_for # importing Flask and other modules
import random #for generating random integers
 
# Flask constructor
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template('index.html')

 
@app.route('/', methods =["GET", "POST"])
def email_slicer():
    if request.method == "POST": 
       email = request.form.get("email")  # getting input with name = email in HTML form
       email = email.strip()  #getting rid of unnecessary spaces
       email1 = email.split("@")[0]  #splitting the string at '@" symbol 
       domain = email.split("@")[1]  #assigning domain address to a variable
       if email == "":
       		user_name = "NO Input!"
       else :
                user_name = email1[0:5]+ str(random.randint(0,10)) #adding random generated integer
 
    return render_template('index.html',result1 = email1, result2 = domain, result3 = user_name )
 
if __name__=='__main__':
   app.run()
