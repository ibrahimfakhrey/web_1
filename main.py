import requests
from flask import Flask,render_template,request
app = Flask(__name__)
End_point="https://api.openweathermap.org/data/2.5/weather"
lat="30.350176"
lon="31.219482"
API_KEY="868c5469fc5add3122d3e7e8313c8f3e"
users={
    "hana":"1234",
    "bosy":"0000",
    "merhan":"1122"
}
data={


}

@app.route("/",methods=["GET","POST"])
def wall():
    if request.method=="POST":
        user_name=request.form.get("name")
        user_comment=request.form.get("comment")
        #write your code below
        data[user_name]=user_comment
        print(data)

        return render_template("wall.html",items=data)
    return render_template("lesson3.html")
@app.route("/getting weather",methods=["GET","POST"])
def start():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        for i in users:
            if i==name:
                if users[i]==password:

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
            return "ERROR 404"
    return render_template("index.html")




if __name__==("__main__"):
    app.run(debug=True)



