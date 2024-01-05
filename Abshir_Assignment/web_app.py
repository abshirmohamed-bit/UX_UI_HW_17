from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Portfolio')
def portfolio():
    return render_template('Portfolio.html')

@app.route('/Contact')
def contact():
    return render_template('Contact.html')

@app.route('/About')
def about_Me():
    return render_template('About_me.html')