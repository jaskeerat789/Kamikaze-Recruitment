from flask import Flask, request

main = Flask(__name__)


@main.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        name = request.form.get('name')
        return'<h3> Hey {}, your request was succesful!'.format(name)
    return '''<form method="POST">
                  Name: <input type="text" name="name"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


main.run(host='127.0.0.1', port='5000')
