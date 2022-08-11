from flask import Flask, render_template, request, flash
from pymongo import MongoClient
from forms import SignUp, SignIn
from turbo_flask import Turbo

app = Flask(__name__)
turbo = Turbo(app)
app.secret_key = 'Login System'
cluster = "mongodb://localhost:27017"
client = MongoClient(cluster)
db = client['practice']
login = db.login


@app.route("/", methods=['GET', 'POST'])
def index():
    signup = SignUp()
    signin = SignIn()
    if signup.signup.data and signup.validate():
        print('Sign Up')
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Passwords don't match")
        else:
            dict = {'name': name, 'email': email, 'password': password, 'confirm_password': confirm_password}
            login.insert_one(dict)
            flash("User Added")

    if signin.signin.data and signin.validate():
        print('Sign In')
        email = request.form['email']
        password = request.form['password']
        data = login.find_one({'email': email})
        if data is None:
            flash("No such email exist")
        elif password != data['password']:
            flash('Password is wrong')
        else:
            flash("User Logged In")

    return render_template("sign_up_in.html", signup=signup, signin=signin)


if __name__ == "__main__":
    app.run(use_reloader=True)