import requests
from flask import Flask,render_template,request
from werkzeug.utils import redirect

app = Flask(__name__)

images={
    "1":"https://images.unsplash.com/photo-1469474968028-56623f02e42e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=874&q=80",
    "2":"https://images.unsplash.com/photo-1469474968028-56623f02e42e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=874&q=80",
    "3":"https://images.unsplash.com/photo-1514525253161-7a46d19cd819?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80"
}
rating={
    "1":20,
    "2":0,
    "3":0
}


@app.route("/")
def start():


    return render_template("session5.html",img=images)

@app.route("/show")
def show ():
    key=request.args.get('key')
    print(key)
    for k in rating :
        if k==key:
            return f"{rating[key]}"
    return "i didnot find rating for this "
@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        name=request.form.get("name")
        link=request.form.get("link")
        images[name]=link
        return redirect("/")


    return render_template("add.html")



if __name__==("__main__"):
    app.run(debug=True)



