from flask import Flask, request, render_template
import sys
import os

# Add parent directory to path to import from database module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.mongoDb import collection

app = Flask(__name__) # create a Flask app instance

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)
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

@app.route('/second')
def second():
    return 'second page'    

# @app.route('/api/<name>')
# def api(name):
#     length = len(name)
#     if length > 5:
#         return 'Name is too long'
#     elif length < 3:
#         return 'Name is too short'
#     else:
#         return f'Hello {name}'
@app.route('/api')
def api():
    name = request.args.get('name')
    age = request.args.get('age')
    length = len(name)
    if length > 5:
        return 'Name is too long'
    elif length < 3:
        return 'Name is too short'
    else:
        return f'Hello {name, age}'


if __name__ == '__main__': # check if the script is being run directly
    app.run(host = '0.0.0.0', port = 9000, debug=True) # run the app in debug mode