from flask import Flask, render_template, request, redirect
from function_test import hello


app = Flask(__name__)

def log_request(req: str, res: str) -> None:
    with open('dirty_grammar.log', 'a') as log:
        print(req, res, file=log);

@app.route('/dirty_grammar', methods=['POST'])
def hello( ) -> 'html':
    #get the text and return determiners
    phrase = request.form['phrase'];
    letters = {'a', 'an', 'the', 'your', 'my', 'your', 'his', 'her', 'many', 'much', 'few', 'a few', 'a lot of'};
    split_text = phrase.split(" ");
    results  = str(letters.intersection(split_text));
    log_request(phrase, results);
    return render_template('result.html', the_results=results, the_phrase=phrase);

@app.route('/')
@app.route('/entry')
def entery_page() -> 'html':

    return render_template('entry.html', the_title='welcome to dirty grammar on the web!');

app.run(debug=True);
