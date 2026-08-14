from flask import Flask


app = Flask(__name__)

@app.route('/')
def home_page():
    return '''
    <h1 style="color: green; background-color: orange;">
        hello this is Server side - flask
    </h1> 
    <button type="button" onclick="location.href='/about'">
        Go to About
    </button>
    '''

@app.route('/about')
def about_page():
    return '''
            <h1 style="color: red ; background-color:green"> flask is a python lightweight framework for api/web server</h1>
            
            <button type="button" onclick="location.href='/'">
              Go back
            </button>
            
            '''


app.run( debug=True )