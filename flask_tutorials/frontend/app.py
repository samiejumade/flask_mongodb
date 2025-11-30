from flask import Flask, render_template, request
from datetime import datetime
import requests
import sys
import os

# Add parent directory to path to import from database module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.mongoDb import collection

BACK_END_URL = "http://127.0.0.1:9000"

app = Flask(__name__) # create a Flask app instance
@app.route('/') # define a route for the root URL

def home():
    day_of_week = datetime.today().strftime('%A')
    print(day_of_week)
    return render_template('index.html', day_of_week=day_of_week)
    
@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACK_END_URL + '/submit', json=form_data)
    # return 'data submitted sucessfully'
    return render_template('success.html')

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for items in data:
        print(items)
        del items['_id']
    data ={
        'data':data
    }
    return data
# @app.route('/submit', methods=['POST'])
# def submit():
#     form_data = dict(request.json)
#     collection.insert_one(form_data)
#     return render_template('success.html')

if __name__ == '__main__': # check if the script is being run directly
    app.run(host = '0.0.0.0', port = 8000, debug=True) # run the app in debug mode