import json
from flask import Flask, redirect, url_for, render_template, request
from difflib import get_close_matches

data = json.load(open("data.json"))

new = Flask(__name__)
meaning_list =[]

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    else:
        return "Sorry, The word does not exist." 
    
@new.route('https://arjunr7.github.io/simpledict/')
def home():
    return render_template('index.html')

@new.route('/meaning', methods=['POST'])
def definition():
    if request.method=='POST':
        name = request.form['nm']
        x = meaning(name)
        if isinstance(x, list):
            return render_template('meaning.html', val = (len(x)-1),l = x, word=name)

        else:
            if len(get_close_matches(name,data))>0:
                label = 'y'
                x = meaning(get_close_matches(name,data)[0])
                return render_template('meaning.html', val = (len(x)-1),l = x, flag=label, alt_wrd=get_close_matches(name,data)[0])
            else:
                return "<html><script>function goBack() {window.location.href='https://arjunr7.github.io/simpledict/';}</script><body><h1>%s</h1></body><button onclick='goBack()'>Home</button></html>" %x
        label= 'n'

if __name__ == '__main__':
    new.run(debug=True)