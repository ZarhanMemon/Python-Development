from flask import Flask , render_template , request

app = Flask(__name__)


@app.route('/')
def home_page():
    
    name = "Zarhan"
    language = "Py"
    
    items = [ "Apple" , "Grapes" , "Cocoa"]
    
    html = '''<b style='color:blue'> I am from flask server</b>'''
    
    return render_template("form_page.html" , name =name , lang=language , fruits = items , html = html) 


@app.route('/predict' , methods=["POST" ,"GET"])
def predict():
    
    if request.form :
        name = request.form['user_name']
        password = request.form['password']
        email = request.form['email']
    
        print( f'{name} | {email} | {password}')
    
        return 'U created an account by email ' + email
    
    return 'Sorry please check the form data'




app.run(debug=True)