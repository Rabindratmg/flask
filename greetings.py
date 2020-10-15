from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return "hello Rabee i am here to check you"

if __name__=="__main__":
    app.run(debug=True)