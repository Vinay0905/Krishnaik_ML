from flask import Flask, render_template, request




app=Flask(__name__)


@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to this flask course.</h1></body></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            return f"Hello {name}, thanks for the form."
        # on empty name, re-render form with an error message
        return render_template("form.html", error="Please enter your name.")
    return render_template("form.html")





if __name__=="__main__":
    app.run(debug=True)

