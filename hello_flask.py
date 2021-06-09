from flask import Flask
from function_test import hello


app = Flask(__name__)

@app.route('/')
def hello( ) -> str:
    text = input("please enter your sentences");
    #get the text and return determiners
    determiners = {"a","an","the","some","many", "much", "this","that", "those", "his", "her", "your", "my"};
    split_text = text.split(" ");
    found_determiners = determiners.intersection(split_text);
    return str(found_determiners);

app.run();
