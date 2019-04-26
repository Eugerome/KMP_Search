from flask import Flask, request, render_template
import kmp_logic as kmp

app = Flask(__name__)
text = None
len_txt = 50

# this function creates string to search
def create_text():
    global text
    text = [kmp.generate_string(len_txt)]

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
            result = kmp.KMP_search(text[0], pattern)
            if result:
                return result
            else:
                return "No matching pattern found"
        else:
            return 'Invalid char present, please use "A", "B", "C", or "D"'

# this restructures the text string to highlight the matching text
def higlight_pattern(indexes, len_ptrn):
    global text
    text = text[0]
    text_split = []
    # find the start and end of each pattern match 
    split_indexes = [0]
    start = end = 0
    while end < len(indexes):
        while end + 1 < len(indexes) and indexes[start] + len_ptrn > indexes[end + 1]:
            end += 1
        split_indexes.extend([indexes[start], indexes[end]+len_ptrn])
        end += 1
        start = end
    split_indexes.append(-1)
    i = 0
    while i < len(split_indexes)-1:
        text_split.append(text[split_indexes[i] : split_indexes[i + 1]])
        i += 1
    
    return text_split




@app.route("/")
def home():
    create_text()
    return render_template("template.html", text = text)

@app.route("/", methods=["POST"])
def form_post():
    global text
    pattern = request.form["pattern"]
    indexes = process_input(pattern)
    # if pattern was found, highlight it
    if isinstance(indexes, list) is True:
        text = higlight_pattern(indexes, len(pattern))
    return render_template("template.html", text = text, indexes = indexes)

if __name__ == "__main__":
    app.run()


