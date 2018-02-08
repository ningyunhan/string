from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

	res = 0
	string = request.form['string']

	t = re.findall(r'\-\.\d+|\-\d+\.\d+|\d+\.\d+|\.\d+|-\d+|\-\d+\.|\d+', string)
	if(len(t) == 0):
		return jsonify({"message": "Oh I can't find digits in this string. The result is: " + '""'})

	for i in range(len(t)):
		if(t[i][0] == '-'):
			res = res - float(t[i][1:])
		else:
			res += float(t[i])
	if(int(res) == res):
		res = int(res)
	res = "My result is: " + str(res)
	return jsonify({"result": res})



if __name__ == "__main__":
    app.run(debug = True)