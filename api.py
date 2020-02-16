from flask import Flask, request, jsonify
import src

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!<br/>The GET methods offered are:<ul><li>/db - access database info</li><li>/random - returns random restaurant</li><li>/delete - delete the database objects</li></ul>The POST methods offered are: <ul><li> /filldb - fills database with local restaurants with a radius (meters) parameter</li></ul>"

@app.route('/db', methods = ['GET'])
def db():
    src.db_connect()
    return jsonify(results = src.dbget())

@app.route('/random', methods = ['GET'])
def random():
    return jsonify(results = src.randomizer())

@app.route('/delete', methods = ['GET'])
def deldb():
    src.db_connect()
    src.dbdel()
    return "ok", 200

@app.route('/filldb', methods = ['POST'])
def filldb():
    src.db_connect()
    src.dbdel()
    rad = request.args['radius']
    lat = src.getlat()
    lng = src.getlng()
    src.getrest(lat,lng,rad)
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True)
