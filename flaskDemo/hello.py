from flask import Flask, render_template, request, url_for, redirect, flash
app = Flask(__name__)

#@app.route("/")
@app.route('/try.html/', methods=['POST', 'GET'])
def render_text():
	a_text = ''
	if request.method == "POST":
		a_text = request.form['utext']
		
	return render_template("try.html", a_text = a_text)

# def render_html():
# 	return render_template("try.html")

# def hello():
#   return "Hello World!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000)