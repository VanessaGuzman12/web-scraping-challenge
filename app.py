from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_PyMongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape():

    mars= scrape_mars.scrape_all()
    mongo.db.collection.update({},mars, upsert=True)
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)