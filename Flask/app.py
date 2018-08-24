import os
from flask import Flask, render_template, jsonify, request, abort
from api import get_recommendation

# Initialization of the Bar Recommender App
app = Flask('BarRecommenderApp')

# Homepage of app will just return baseball html template
@app.route('/')
def renderbasehtml():
    return render_template('recommender.html')

# Post method for lookalike recommendations
@app.route('/recommend', methods = ['POST'])
def give_recommendation():

    # check to see if what is being passed is a JSON
    if not request.json:
        abort(400)
    # check to see that the necessary entries are in the JSON

    elif (('Bar_List' not in request.json) or ('Neighbors' not in request.json)
    or ('Specific_State' not in request.json)):
        abort(400)

    # using get_neighbors function from api to return lookalike bars
    else:
        data = request.json
        response = get_recommendation(data)
        return jsonify(response)



# Running Baseball App
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
