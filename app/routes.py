from app import my_obj
from flask import Flask, render_template, flash, redirect, url_for, request

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@my_obj.route("/", methods = ['GET', 'POST'])
def home():

    if request.method == 'POST':
        flash(request.form["cityName"])
        return redirect(url_for('home'))
        
    return render_template("home.html", name = name, city_names = city_names)