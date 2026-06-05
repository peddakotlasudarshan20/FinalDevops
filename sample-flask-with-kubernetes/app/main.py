import os

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
env = os.environ.get('VERSION', '--')

@app.route('/')
def root():
    return render_template(
        'index.html',
        message=f'You accessed the {env} version of the app.',
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)