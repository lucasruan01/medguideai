from flask import Flask, render_template
from app.routes.chat import chat

app = Flask(__name__)

app.register_blueprint(chat)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)