from flask import Flask ,  jsonify , request

# jsonfy(data) - function to send the json data like in JS res.json(data , {success:200})
 
app = Flask( __name__)


@app.route('/')
def home():
    return " Server happy "

@app.route("/prediction_api")
def predict_api():
    
    input = request.args.get("x" , default=None)
    
    if input is None:
        return jsonify({"error": "Missing parameter 'x'"}), 500
    
     # Try converting to integer
    try:
        x_val = int(input)
    except ValueError:
        return jsonify({"message": "Invalid input. Please send a number."}), 202
    
    
    # sample test api data we gone send through json
    data = { "Output" : int(input)**2 , "Accuracy":100.0}
    
    
    return jsonify( data ) , 200       # data-json , status code


app.run( debug=True)