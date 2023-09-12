from flask import Flask
import socket, json

app = Flask(__name__)

@app.route("/")
def index():
        hostname = socket.gethostname()
        get_ip = socket.gethostbyname(hostname)
        return get_ip

@app.route('/name')
def myname():
        return "Dayashankar M M"

@app.route('/health')
def health():
        return json.dumps({'success':True}), 200, {'ContentTpye':'application/json'}

if __name__ == '_main':
        app.run(host="0.0.0.0", port="8090")