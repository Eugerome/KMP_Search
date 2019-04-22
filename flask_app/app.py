from flask import Flask, request, render_template
import kmp_logic as kmp

app = Flask(__name__)
text = None

# this function creates string to search
def create_text():
    global text
    len_txt = 50
    text = kmp.generate_string(len_txt)

@app.route("/")
def home():
    create_text()
    return render_template("template.html", text = text)

@app.route("/", methods=["POST"])
def form_post():
    pattern = request.form["pattern"].upper()
    return render_template("template.html", text = text, indexes = pattern)

if __name__ == "__main__":
    app.run()