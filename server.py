from flask import Flask, render_template, request
import socket

app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/',methods=['GET'])
def func():
    return render_template("app.html")

if __name__ == "__main__":
    ip = socket.gethostbyname(hostname)
    app.run(host=ip,debug=True)