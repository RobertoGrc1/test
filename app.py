from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def run_script():
    result = subprocess.run(["python3", "test.py"], capture_output=True, text=True)
    return f"<pre>{result.stdout}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
