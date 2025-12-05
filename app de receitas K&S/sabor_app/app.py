from flask import Flask, render_template, jsonify
import json
import os
app = Flask(__name__)
DB_FILE = "database.json"
def load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf_8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/catalog")
def catalog():
    return render_template("catalog.html")

@app.route("/api/recipes")
def api_recipes():
    return jsonify(load_db())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)