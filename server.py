from flask import Flask, send_from_directory

app = Flask(__name__)

# Main page
@app.route('/')
def home():
    return send_from_directory('.', 'home.html')

# Other pages
@app.route('/component')
def component():
    return send_from_directory('.', 'component.html')

@app.route('/donate')
def donate():
    return send_from_directory('.', 'donate.html')

@app.route('/smartcity')
def smartcity():
    return send_from_directory('.', 'smartcity.html')

# Serve CSS
@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
