from flask import Flask, render_template
from function_test import hello


app = Flask(__name__)

@app.route('/salam')
def salam() -> str:
    return "salam";

@app.route('/dirty_grammar')
def hello( ) -> str:
    text = input("please enter your sentences");
    #get the text and return determiners
    determiners = {"a","an","the","some","many", "much", "this","that", "those", "his", "her", "your", "my"};
    split_text = text.split(" ");
    found_determiners = determiners.intersection(split_text);
    return str(found_determiners);

@app.route('/entry')
def entery_page() -> 'html':
    return render_template('ntry.html', the_title='welcome to the search4 letters on the web!');

app.run();
