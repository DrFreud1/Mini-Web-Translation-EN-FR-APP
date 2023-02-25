from flask import Flask, render_template, request

from machinetranslation import translator

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get("textToTranslate")
    # Write your code here
    translation = translator.english_to_french(textToTranslate)
    return translation


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get("textToTranslate")
    # Write your code here
    translation = translator.french_to_english(textToTranslate)
    return translation


@app.route("/englishToSpanish")
def englishToSpanish():
    textToTranslate = request.args.get("textToTranslate")
    # Write your code here
    translation = translator.english_to_spanish(textToTranslate)
    return translation


@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    # Write the code to render template


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)