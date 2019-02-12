from flask import Flask, request

users = {}

app = Flask(__name__)

@app.route('/<username>', methods = ['GET', 'POST'])
def index(username):

    if request.method == 'POST':
        if user.get(username,-1) != -1:
            return 'Welcome back ' + str(username)
        else:
            users[str(username)] = str(username)
    else:
        return 'Welcome, you may make a POST request'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
        

    
        
    
