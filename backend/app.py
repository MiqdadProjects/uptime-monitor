from flask import Flask, jsonify
from monitor import check_all_sites

app = Flask(__name__)

@app.route('/')
def dashboard():
    sites = check_all_sites()
    return jsonify(sites)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
