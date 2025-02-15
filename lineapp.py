from flask import Flask, request


app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/api/dirupdate", methods=["POST"])
def recive():
    name = request.data
    print(name.decode('utf-8'))
    return "Hello, World!"

if __name__ == "__main__":
    port = 5000
    app.run(host='0.0.0.0', port=port)