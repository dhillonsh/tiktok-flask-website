from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/homepage")
def home():
    return render_template("homepage.html")

@app.route("/hello/<user>")
def user(user):
    return render_template("user.html", user=user)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
