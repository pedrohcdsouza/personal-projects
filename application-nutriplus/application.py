from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contacts():
    return render_template("contacts.html")

@app.route("/cliente/<username>")
def clients(username):
    return render_template("clients.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)