from flask import Flask, request, jsonify
from hangrypy import Hangry
from ingreedypy import Ingreedy
app = Flask(__name__)


@app.route("/")
def home():
    return app.send_static_file('recipe.html')

@app.route("/get")
def recipe():
    url = request.args.get('url', '')
    if url:
        recipe = Hangry(url=url).to_dict()
        for idx, ingredient in enumerate(recipe['ingredients']):
            recipe['ingredients'][idx] = Ingreedy().parse(ingredient)
        return jsonify(recipe)


if __name__ == "__main__":
    app.run(debug=True)
