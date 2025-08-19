from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve main page
@app.route('/')
def serve_index():
    return send_from_directory('.', 'home.html')

# Serve any other file in the folder
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
