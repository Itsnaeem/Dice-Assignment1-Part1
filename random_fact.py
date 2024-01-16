from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_random_fact():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    if response.status_code == 200:
        data = response.json()
        return f"Random Fact: {data['text']}"
    else:
        return "Failed to retrieve a fact."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=89, debug=True)
