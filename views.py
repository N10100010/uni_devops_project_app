from uni_devops_project_app import app
from flask import Flask, request, jsonify, render_template, redirect, url_for

import re

## static templates for local use
RETURN_TO_MAIN = """
<form action = "http://localhost:10000">
    <input type="submit" value="To Start">
</form>
"""

def fizzbuzz(fizbuz: int = 16) -> str:
    start = """\t<div>\n\t\t<h2>The FizzBuzz...</h2>
        """
    end = """
        </div>
        """

    v = ""
    for fb in range(fizbuz):
        if fb % 3 == 0 and fb % 5 == 0:
            v += "\n\t\t<p>fizzbuzz</p>"
            continue
        elif fb % 3 == 0:
            v += "\n\t\t<p>fizz</p>"
            continue
        elif fb % 5 == 0:
            v += "\n\t\t<p>buzz</p>"
            continue

        v += f"\n\t\t<p>\n{fb}</p>"

    return start + v + end


@app.route('/fizzbuzz', methods=['POST'])
def post_fizzbuzz():
    if request.method == 'POST':

        try:
            number = int(re.search(r'\d+', request.form['fizzbuzz']).group())
        except :
            return render_template(
                'index.html',
                message="You really should have entered at least one number in the string. Try again..."
            )

        s = fizzbuzz(number)

        return s + RETURN_TO_MAIN


@app.route('/')
def index():

    return render_template('index.html', message='')
