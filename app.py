import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, template_folder=".")

@app.route('/', methods=['GET'])
def my_form():
	return render_template("my-form.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
	text1 = request.form['text1']
	text2 = request.form['text2']
	
	if text1 == text2:
		stringComparison = True
	else:
		stringComparison = False
		print("different")

	return render_template("my-form.html", compareResult=stringComparison)
	 
if __name__ == '__main__':
	app.run()
