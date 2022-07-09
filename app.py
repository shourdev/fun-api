from flask import Flask, jsonify
import random
import pyjokes
app = Flask(__name__)

@app.route("/")
def home():
   return ("Hi")

@app.route('/joke')
def joke():
    


    joke = pyjokes.get_joke(language="en")
    return(joke)



    



if __name__ == "__main__":
    app.run(debug=False,port=8000)
   
    
