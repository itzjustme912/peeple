from peeple.account import Account
import pandas as pd

# write a function that takes a pandas dataframe as input and returns a list of accounts

# pass in  a variable which has been assaigned to a dataframe in a function which takes
# in the dataframe and somehow loops through it to create individual accounts and store
# them in a list which is a list of objects and returns the list


def df_to_list(data_frame):
    account_list = []
    for index, row in data_frame.iterrows():
        curr_account = Account(
            row["Full Name"], row["Gender"], row["Username"], row["Password"]
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
    df = pd.DataFrame(df_list, columns=["Full Name", "Gender", "Username", "Password"])
    return df

