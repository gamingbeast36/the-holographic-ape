from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/articles")
def articles():
    return render_template("articles.html")

@app.route("/disease_of_addiction")
def disease():
    return render_template("disease_of_addiction.html")



if __name__ == "__main__":
    app.run()


