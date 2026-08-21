from flask import Flask , render_template , flash , request



app = Flask(__name__)

# for flash msg doing needed
app.secret_key = 'my_secret'

@app.route('/')
def home_page():
    
    flash("Welcome to home")
    
    return render_template("index.html")
 

@app.route('/about')
def about_page():
    
    flash("Hi i am About page")
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/send_params')
def accept_params():
    
    name = request.args.get("name")  # accepting whatever the frontend send parameters in URL : /send_params?name=Zarhan&lang=JS and Python
    
    lang = request.args.get("lang" , default="")
    
    print(f"I am {name} and learning {lang} " )
    
    return f" <h3>I am {name} and learning {lang} </h3>"

app.run( debug=True )