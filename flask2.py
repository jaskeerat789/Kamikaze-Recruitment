from flask import Flask, request
 
app = Flask(__name__)
 

@app.route('/', methods=['GET','POST'])
def form_example():
    if request.method =='POST':
        name = request.form.get('name')
        return'<h1>HELLO {}.</h1>'.format(name)
    return '''<form method="POST">
                  Name: <input type="text" name="name"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

app.run(host='127.0.0.1', port= '5000' )