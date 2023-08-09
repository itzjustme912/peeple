from flask import Flask, render_template, request
from peeple.account import Account
import peeple.utils as utils
import pandas as pd


try:
    df_existing = pd.read_csv("accounts.csv")
    accounts = utils.df_to_list(df_existing)
except:
    accounts = []


app = Flask(__name__, template_folder="html")


@app.route("/")
def welcome_message():
    return render_template("index.html")


@app.route("/register")
def get_register():
    return render_template("registration.html")


@app.route("/register", methods=["POST", "GET"])
def save_details():
    global accounts
    global df_existing
    if request.method == "POST":
        user_account = Account(
            request.form["full-name"],
            request.form["gender"],
            request.form["username"],
            request.form["password"],
        )
        accounts.append(user_account)
        df_acc = utils.list_to_df(accounts)
        df_acc.to_csv("accounts.csv")
        return f"<h1>Registered succesfully {user_account.get_full_name()}"
    else:
        return "<h1>Please enter details!</h1>"


@app.route("/admins", methods=["GET"])
def output_members():
    member_accounts = []
    for curr_member in accounts:
        member_accounts.append(curr_member.get_full_name())
    return ", ".join(member_accounts)


@app.route("/login")
def get_login():
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    global account
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for account in accounts:
            if account.get_username() == username:
                if account.get_password() == password:
                    return f"<h1>Welcome back {account.get_full_name()}!</h1>"
                else:
                    return "<h1>Incorrect password</h1>"
        return "<h1>Username not found</h1>"


if __name__ == "__main__":
    app.run()
