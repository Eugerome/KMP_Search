from flask import Flask, request, render_template
import kmp_logic as kmp

app = Flask(__name__)
text = None
len_txt = 50

# this function creates string to search
def create_text():
    global text
    text = kmp.generate_string(len_txt)

# this validates input
def process_input(pattern):
    if len(pattern) > len_txt:
        return "Pattern longer than the search string, try a smaller string"
    elif len(pattern) == 0:
        return "No pattern submitted, please input pattern"
    else:
        pattern = pattern.upper()
        success = True
        for l in pattern:
            if l not in kmp.letters:
                success = False 
                break
        if success is True:
            return kmp.KMP_search(text, pattern)
        else:
            return 'Invalid char present, please use "A", "B", "C", or "D"'


@app.route("/")
def home():
    create_text()
    return render_template("template.html", text = text)

@app.route("/", methods=["POST"])
def form_post():
    pattern = request.form["pattern"]
    pattern = process_input(pattern)
    return render_template("template.html", text = text, indexes = pattern)

if __name__ == "__main__":
    app.run()