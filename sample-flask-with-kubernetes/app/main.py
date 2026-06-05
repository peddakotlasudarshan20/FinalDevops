# import os

# from flask import Flask, render_template

# app = Flask(__name__, template_folder='templates')
# env = os.environ.get('VERSION', '--')

# @app.route('/')
# def root():
#     return render_template(
#         'index.html',
#         message=f'You accessed the {env} version of the app.',
#     )

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

import random
from flask import Flask, request

app = Flask(__name__)

secret_number = random.randint(1, 10)


@app.route("/", methods=["GET", "POST"])
def game():
    global secret_number

    message = " Guess a number between 1 and 10"
    message_color ="#ffffff"

    if request.method == "POST":
        guess = request.form.get("guess")

        try:
            guess = int(guess)

            if guess == secret_number:
                message = f" Correct! The number was {secret_number}. New game started!"
                message_color = "#00ff88"
                secret_number = random.randint(1, 10)

            elif guess < secret_number:
                message = " Too Low! Try Again."
                message_color = "#ffd43b"

            else:
                message = " Too High! Try Again."
                message_color = "#ff6b6b"

        except ValueError:
            message = " Please enter a valid number."
            message_color = "#ff4757"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Number Guessing Game</title>

        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Poppins', sans-serif;
            }}

            body {{
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(
                    135deg,
                    #667eea,
                    #764ba2,
                    #6a11cb,
                    #2575fc
                );
                background-size: 400% 400%;
                animation: gradientMove 10s ease infinite;
            }}

            @keyframes gradientMove {{
                0% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
                100% {{ background-position: 0% 50%; }}
            }}

            .container {{
                width: 400px;
                padding: 35px;
                text-align: center;

                background: rgba(255,255,255,0.1);
                backdrop-filter: blur(15px);

                border-radius: 20px;
                border: 1px solid rgba(255,255,255,0.2);

                box-shadow:
                    0 8px 32px rgba(0,0,0,0.3);
            }}

            h1 {{
                color: white;
                margin-bottom: 20px;
                font-size: 32px;
            }}

            .message {{
                color: {message_color};
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 20px;
                min-height: 30px;
            }}

            input {{
                width: 100%;
                padding: 14px;
                border: none;
                border-radius: 12px;
                outline: none;
                font-size: 18px;
                text-align: center;
                margin-bottom: 20px;
            }}

            button {{
                width: 100%;
                padding: 14px;
                border: none;
                border-radius: 12px;

                background: linear-gradient(
                    45deg,
                    #00c6ff,
                    #0072ff
                );

                color: white;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;

                transition: 0.3s;
            }}

            button:hover {{
                transform: translateY(-3px);
                box-shadow: 0 10px 20px rgba(0,0,0,0.3);
            }}

            .footer {{
                color: rgba(255,255,255,0.8);
                margin-top: 20px;
                font-size: 14px;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🎲 Number Guessing Game</h1>

            <div class="message">
                {message}
            </div>

            <form method="POST">
                <input
                    type="number"
                    name="guess"
                    min="1"
                    max="10"
                    placeholder="Enter a number"
                    required
                >

                <button type="submit">
                    🚀 Submit Guess
                </button>
            </form>

            <div class="footer">
                Made with Flask ❤️
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)