from flask import Flask, render_template, request, redirect
import random



app = Flask(__name__)
'''
@app.after_request
def disable_cache(req):
    req.headers["Cache-Control"] = "no-cache"
    return req'''

@app.route("/" , methods=['POST','GET'])
def home():
    if request.method == 'POST':
        try:
            return redirect("game_pop")
        except:
            "the site has crashed!"
    else: 
        return render_template('index.html')

@app.route("/game_pop", methods=['GET','POST'])
def game_pop():
    a = open('gamelinks.txt','r')
    b = a.read().split()
    a.close()
    return redirect(random.choice(b))

if __name__ == '__main__':
    app.run(debug=True)