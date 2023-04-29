"""_summary_

    Returns:
        _type_: Server code
"""
#import json
from machinetranslation import translator
from flask import Flask, render_template, request


app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """_summary_

    Returns:
        _type_: translate english to french
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    fr_str = translator.english_to_french(text_to_translate)
    
    return "Translated text to French" + fr_str

@app.route("/frenchToEnglish")
def french_to_english():
    """_summary_

    Returns:
        _type_: translate french to english
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    eng_str = translator.french_to_english(text_to_translate)
    return "Translated text to English" + eng_str

@app.route("/")
def render_index_page():
    """index page to launch
    """
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
