from flask import Flask, render_template
import json
from monitor import check_all_sites

app = Flask(__name__)

@app.route('/')
def dashboard():
    sites = check_all_sites()
    return render_template('dashboard.html', sites=sites)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
