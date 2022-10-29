# Modules
from crypt import methods
from os import getlogin, write
import time
import datetime
from datetime import date, timedelta
import sys
import locale
from flask import Flask, request, render_template

# Set locale
locale.setlocale(locale.LC_ALL, '')

# Flask constructor
app = Flask(__name__)  

# Program startup
@app.route("/")
def startup():
    return render_template("index.html")

# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    isLogin = False
    # Import NIM
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
    inpNIM = request.form.get("NIM")
    # Input
    if (inpNIM in dataNIM):
        nama = dataNama[dataNIM.index(inpNIM)]
        isLogin = True
    else:
        nama = ""
        isLogin = False
    f = open("session.txt", "w")
    f = f.write(f"{nama}\n{isLogin}")
    # Output
    if (request.method == "POST"):
        return render_template("index.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("index.html")


# Petunjuk arah
@app.route("/rute", methods=["POST", "GET"])
def rute():
    f = open("session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    isLogin = f[1]
    tanggal = request.form.get("tanggal")
    tanggal = int(time.mktime(datetime.datetime.strptime(tanggal, "%m/%d/%Y").timetuple()))
    tanggal = datetime.datetime.fromtimestamp(tanggal).strftime("%A")
    gerbang = request.form.get("gerbang")
    # Output
    if (request.method == "POST"):
        return render_template("index.html", tanggal = tanggal, isLogin = isLogin, nama = nama)
    else:
        return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)