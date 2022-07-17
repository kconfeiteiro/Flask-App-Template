from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home(): 
    return render_template("home")

@app.route("/theory")
def theory(): 
    return render_template("theory.html")

@app.route("/navigation")
def navigation():
    return render_template("navigation.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)