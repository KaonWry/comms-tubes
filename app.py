# Import modules
import locale
from flask import Flask, request, render_template
import datetime
from datetime import date, timedelta


# Set locale for time
locale.setlocale(locale.LC_ALL, '')

# Flask constructor
app = Flask(__name__)  

# Program startup
@app.route("/")
def startup():
    return render_template("index.html")

# Login NIM
@app.route("/login", methods=["GET", "POST"])
def login():
    # Import NIM and Nama list
    importData = open("dataKelas02.txt", "r")
    importData = importData.read()
    importData = (importData.split("\n"))
    dataNIM = [0] * len(importData)
    dataNama = [0] * len(importData)
    j = 0
    for i in importData:
        i = i.split("-")
        dataNama[j] = i[1]
        dataNIM[j] = i[0]
        j += 1
    nomorNIM = request.form.get("NIM")
    isLogin = False
    if (nomorNIM in dataNIM):
        Nama = dataNama[dataNIM.index(nomorNIM)]
        isLogin = True
        return render_template("index.html", isLogin = isLogin, Nama = Nama, NIM = nomorNIM)
    else:
        isLogin = False        
        return render_template("index.html", isLogin = isLogin)
    

if __name__=='__main__':
    app.run(debug=True)