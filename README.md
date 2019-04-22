# KMP_Search
A Flask based webpage that performs a KMP search on a randomly generated string

## Running 
- Ensure Flask is installed
- Run app.py in the flask_app folder
- Visit the page in a browser


## Use
The webpage generates a random string out of 4 letters (A, B, C, D). The user can then input a pattern into the search box. The pattern __must__ be comprised of the above 4 letters, otherwise it will not search. After hitting "Pattern Search" the app will output a list of indexes at which the pattern starts.

## To Do:
- Replace the list output with something prettier
- Update template
- Highlight matched pattern in the text
- Put into a docker container
