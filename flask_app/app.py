from flask import Flask
import kmp_logic as kmp

app = Flask(__name__)

@app.route("/")
def home():
    len_txt = 50
    text = kmp.generate_string(len_txt)
    return text

if __name__ == "__main__":
    app.run()