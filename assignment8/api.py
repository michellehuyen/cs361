from dataclasses import dataclass
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@dataclass
class Macronutrient:
    name:str
    cals_per_gram: int

    def calc_calories(self) -> int:
        if self.name.lower() == "carbohydrate":
            return self.cals_per_gram * 4
        elif self.name.lower() == "protein":
            return self.cals_per_gram * 9
        else:
            return 0

@app.route('/calculate-cals/<string:name>/<int:grams>')
def calculate_cals(name, grams):
    if name and grams:
        macro = Macronutrient(name, grams)
        response = {
            "macro-name": name,
            "grams": grams,
            "calories": macro.calc_calories()
        }
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)