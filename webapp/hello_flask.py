from flask import Flask, render_template, request
from function_test import hello


app = Flask(__name__)

@app.route('/salam')
def salam() -> str:
    return "salam";

@app.route('/dirty_grammar', methods=['POST'])
def hello( ) -> str:
    #get the text and return determiners
    phrase = request.form['phrase'];
    letters = {'a', 'an', 'the', 'your', 'my', 'your', 'his', 'her', 'many', 'much', 'few', 'a few', 'a lot of'};
    split_text = phrase.split(" ");
    found_determiners = letters.intersection(split_text);
    return str(found_determiners);

@app.route('/entry')
def entery_page() -> 'html':

    return render_template('entry.html', the_title='welcome to dirty grammar on the web!');

app.run(debug=True);
