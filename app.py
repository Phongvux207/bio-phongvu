from flask import Flask, render_template
import json, os

app = Flask(__name__)

def load_profile():
    path = os.path.join(app.root_path, 'profile.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    profile = load_profile()
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
