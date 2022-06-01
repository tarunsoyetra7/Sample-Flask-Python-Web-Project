from flask import Flask, render_template, redirect, request, url_for, session
import mysql.connector

# database connection from python to mysql
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="Bank")


app = Flask(__name__)
app.secret_key = "this is top secret"

# below codes will check the user is already login or not
@app.route("/")
def index():
    if "id" in session:
        id = session["id"]
        return render_template("dashboard.html", title="Dashboard")
    else:
        return render_template("login.html", title="Please Login")


# below codes will check the credential of employees
@app.route("/check_login", methods=["POST"])
def check_login():
    username = str(request.form["username"])
    password = str(request.form["password"])

    mycursor = mydb.cursor()
    mycursor.execute("select * from accountant_info where acc_info_username='"+username+"'")
    user = mycursor.fetchone()
    if user is None:
        return render_template("login.html", title_new="Invalid Username! Login Again")
    else:
        mycursornew = mydb.cursor()
        mycursornew.execute(
            "select * from accountant_info where acc_info_username='"+username+"' and acc_info_pass='"+password+"'")
        newuser = mycursornew.fetchone()
        if newuser is None:
            return render_template("login.html", title_new="Invalid Password! Login Again")
        else:
            session["id"] = user[0]
            return redirect(url_for("dashboard"))

# if credential of employees is correct than it will forward to its dashboard
@app.route("/dashboard")
def dashboard():
    if "id" in session:
        id = session["id"]
        return render_template("dashboard.html", title="Dashboard")
    else:
        return render_template("login.html", title="Please Login First")


@app.route("/create_customer_profile")
def create_customer_profile():
    if "id" in session:
        id = session["id"]
        return render_template("create_customer_profile.html")
    else:
        return render_template("login.html", title="Please Login First")


@app.route("/update_customer_profile")
def update_customer_profile():
    if "id" in session:
        id = session["id"]
        return render_template("update_customer_profile.html")
    else:
        return render_template("login.html", title="Please Login First")


@app.route("/create_account")
def create_account():
    if "id" in session:
        id = session["id"]
        return render_template("create_account.html")
    else:
        return render_template("login.html", title="Please Login First")


@app.route("/delete_account")
def delete_account():
    if "id" in session:
        id = session["id"]
        return render_template("delete_account.html")
    else:
        return render_template("login.html", title="Please Login First")


@app.route("/deposit_money")
def deposit_money():
    if "id" in session:
        id = session["id"]
        return render_template("deposit_money.html")
    else:
        return render_template("login.html", title="Please Login First")


@app.route("/withdraw_money")
def withdraw_money():
    if "id" in session:
        id = session["id"]
        return render_template("withdraw_money.html")
    else:
        return render_template("login.html", title="Please Login First")


@app.route("/logout")
def logout():
    session.pop("id", None)
    return render_template("login.html", title="Please Login")


if __name__ == "__main__":
    app.run(debug=True)