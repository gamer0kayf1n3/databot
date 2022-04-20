from flask import Flask, send_from_directory
from threading import Thread

app = Flask(__name__, static_url_path='')

@app.route('/public_html/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
