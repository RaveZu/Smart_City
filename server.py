from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve HTML files directly
@app.route('/home.html')
def home():
    return send_from_directory('.', 'home.html')

@app.route('/smartcity.html')
def smartcity():
    return send_from_directory('.', 'smartcity.html')

@app.route('/component.html')
def component():
    return send_from_directory('.', 'component.html')

@app.route('/donate.html')
def donate():
    return send_from_directory('.', 'donate.html')

# Serve CSS
@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

# Optional: redirect root to home.html
@app.route('/')
def index():
    return send_from_directory('.', 'home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
