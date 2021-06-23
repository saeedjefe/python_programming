from flask import Flask, render_template, request, redirect, escape
from function_test import hello


app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('dirty_grammar.log', 'a') as log:
        print( req.form, req.user_agent, req.remote_addr, file=log, sep='|');


@app.route('/dirty_grammar', methods=['POST'])
def hello( ) -> 'html':
    #get the text and return determiners
    phrase = request.form['phrase'];
    letters = {'a', 'an', 'the', 'your', 'my', 'your', 'his', 'her', 'many', 'much', 'few', 'a few', 'a lot of'};
    split_text = phrase.split(" ");
    results  = str(letters.intersection(split_text));
    log_request(request, results);
    return render_template('result.html', the_results=results, the_phrase=phrase);

@app.route('/')
@app.route('/entry')
def entery_page() -> 'html':

    return render_template('entry.html', the_title='welcome to dirty grammar on the web!');

@app.route('/viewlog')
def show_the_log() -> str:
    with open('dirty_grammar.log') as view_log:
        contents = view_log.read();
    return escape(contents);

app.run(debug=True);
