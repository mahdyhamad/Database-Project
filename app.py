from flask import Flask

app = Flask(__name__, instance_relative_config=True)

@app.route('/home')
def index():
    return "this is the home page";


if __name__ == "__main__":
    app.run()