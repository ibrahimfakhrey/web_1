import requests
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)
End_point="https://api.openweathermap.org/data/2.5/weather"
lat="30.350176"
lon="31.219482"
API_KEY="868c5469fc5add3122d3e7e8313c8f3e"
users={
    "ahmed":"1234",
    "ma7moud":"0000",
    "wa7eed":"1122"
}




@app.route("/")
def start():

    return render_template("start.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        for thing in users:
            if thing ==name:
                if password==users[thing]:
                    params = {
                        "lat": lat,
                        "lon": lon,
                        "appid": API_KEY
                    }

                    response = requests.get(url=End_point, params=params)

                    data = response.json()
                    print(data)

                    temper = data["main"]["temp"]
                    celtemp = int(temper) - 273
                    desc = data["weather"][0]["main"]
                    hum = data["main"]["humidity"]
                    city_name = data["name"]
                    return render_template("weather.html", temp=celtemp, city=city_name)



                else:
                    m="your password is incorrect"
                    return render_template("4.html",m=m)
        m="you are not with us "
        return render_template("4.html",m=m)

    return render_template("test.html")
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        users[name]=password
        return redirect(url_for('login'))

    return render_template("register.html")










































if __name__==("__main__"):
    app.run(debug=True)
