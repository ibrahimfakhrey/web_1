import requests
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


data={
    "img":"https://images.unsplash.com/photo-1661956601031-4cf09efadfce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80",
    "i": "https://images.unsplash.com/photo-1661956601031-4cf09efadfce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80",

}

rating={
    "img":1,
    # "i":2
}



@app.route("/")
def start():
    images=data
    return render_template("lessson5.html",img=images)
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        link = request.form.get("link")
        data[name] = link
        return redirect("/")
    return render_template("add.html")

@app.route("/show")
def show():
    key = request.args.get('key')
    for k in rating:
        if k==key:
            return f"{rating[key]}"

    return f" i didnot find a rating for {key}"

































if __name__==("__main__"):
    app.run(debug=True)
