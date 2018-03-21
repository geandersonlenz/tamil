from flask import Flask, request, render_template, jsonify
from textblob import TextBlob
import json
import spacy

nlp = spacy.load("en")

app = Flask(__name__)

@app.route('/count')
def my_form():
    return render_template('forms.html')

@app.route('/count', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper()
        count_text = text.count("oi")
        return jsonify ({'count': count_text})

@app.route('/tags')
def my_form2():
    return render_template('forms2.html')


@app.route('/tags', methods=['POST'])
def tags():
    if request.method == 'POST':
        text = request.form['text2']
        blob = TextBlob(text)
        tags = blob.tags
        return jsonify ({'tags': tags})

@app.route('/tokenization')
def my_form3():
    return render_template('forms3.html')


@app.route('/tokenization', methods=['POST'])
def tokens():
    if request.method == 'POST':
        text = request.form['text3']
        doc = nlp(text)
        tokenization = [token.orth_ for token in doc]
        return jsonify({'tokenization': tokenization})


@app.route('/lemmatisation')
def my_form4():
    return render_template('forms4.html')

@app.route('/lemmatisation', methods=['POST'])
def lemma():
    if request.method == 'POST':
        text = request.form['text4']
        doc = nlp(text)
        lemmatisation = [word.lemma_ for word in doc]
        return jsonify({'lemmatisation': lemmatisation})

@app.route('/postagging')
def my_form5():
    return render_template('forms5.html')

@app.route('/postagging', methods=['POST'])
def postag():
    if request.method == 'POST':
        text = request.form['text5']
        #tagging = []
        doc = nlp(text)
        tokenization = json.dumps([token.orth_ for token in doc])
        postagging = json.dumps([i.tag_ for i in doc])
        return jsonify({tokenization, postagging})

if __name__ == '__main__':
    app.run(debug=True)