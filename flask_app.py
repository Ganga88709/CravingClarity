# flask_app.py
from flask import Flask, render_template, request,redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/run_streamlit')
def run_streamlit():
    # Execute the Streamlit app
    subprocess.Popen(['streamlit', 'run', 'app.py'])
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)

