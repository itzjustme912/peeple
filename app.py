from flask import Flask, render_template, request
from peeple.account import Account
from datetime import datetime
import peeple.utils as utils
import pandas as pd


try:
    df_existing = pd.read_csv("accounts.csv")
    accounts = utils.df_to_list(df_existing)
except:
    accounts = []

chats_dictionary: dict[str, pd.DataFrame] = {}

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
    global accounts
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for account in accounts:
            if account.get_username() == username:
                print(account.get_password(), password)
                print(type(account.get_password()), type(password))
                if account.get_password() == password:
                    return f"<h1>Welcome back {account.get_full_name()}!</h1>"
                else:
                    return "<h1>Incorrect password</h1>"
        return "<h1>Username not found</h1>"


@app.route("/chats", methods=["GET"])
def get_chats():
    global chats_dictionary
    user1_arg = request.args["user_1"]
    user2_arg = request.args["user_2"]
    file_name, df_chats = utils.load_chats(user1_arg, user2_arg)
    print(file_name)
    print(df_chats.values.tolist())
    chats_dictionary[file_name]= df_chats
    return [df_chats.values.tolist(), file_name]

@app.route("/messages", methods=["POST"])
def send_messages():
    global chats_dictionary
    if request.method == "POST":
        username = request.form["username"]
        msg = request.form["message"]
        key = request.form["key"]
        curr_chat = chats_dictionary[key]
        curr_datetime = datetime.now()
        new_row = {"name": username, "message": msg, "timestamp": curr_datetime}
        curr_chat.append(new_row)
        chats_dictionary[key] = curr_chat
        curr_chat.to_csv(f"./user_chats/{key}")

if __name__ == "__main__":
    app.run()
