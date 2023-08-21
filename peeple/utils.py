from peeple.account import Account
import pandas as pd


def df_to_list(data_frame):
    account_list = []
    for index, row in data_frame.iterrows():
        curr_account = Account(
            str(row["Full Name"]),
            str(row["Gender"]),
            str(row["Username"]),
            str(row["Password"]),
        )
        account_list.append(curr_account)
    return account_list


def list_to_df(list_acc):
    df_list = []
    for account in list_acc:
        curr_element = []
        curr_element.append(account.get_full_name())
        curr_element.append(account.get_gender())
        curr_element.append(account.get_username())
        curr_element.append(account.get_password())
        df_list.append(curr_element)
    df = pd.DataFrame(df_list, columns=["FullName", "Gender", "Username", "Password"])
    return df


def load_chats(user_1, user_2):
    user_accs = [user_1, user_2]
    user_accs.sort()
    file_name = f"{user_accs[0]}_{user_accs[1]}.csv"
    try:
        df_existing = pd.read_csv(f"./user_chats/{user_accs[0]}_{user_accs[1]}.csv")
        print("Previous chats found.")
    except:
        df_existing = pd.DataFrame(columns=["Timestamp", "Name", "Message"])
        print("Previous chats not found, new chat has been created.")
    return file_name, df_existing
