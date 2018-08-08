from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	players=["sergio ramos" , "gareth bale" , "marcelo"]
	return render_template("index.html", players=players , likes_same_sport=True)

if __name__ == '__main__':
   app.run(debug = True)