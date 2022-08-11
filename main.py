from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from forms import SignUp, SignIn



app = Flask(__name__)
app.secret_key = 'Login System'
cluster = "mongodb://localhost:27017"
client = MongoClient(cluster)
db = client['practice']