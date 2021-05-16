#password generator
import random
import string
import pandas as pd

def Password_generator(length):
    account = input("Enter account for which password is being generated: ")
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    all = upper + lower + numbers + symbols

    temp = random.sample(all,length)
    password = "".join(temp)
    p_generated = {"Password":password,"Account":account}
    dct = {k:[v] for k,v in p_generated.items()}
    df = pd.DataFrame(dct)
    cols = ["Password","Account"]
    print(df)
    df.to_csv(index=False,mode='a',header=False,path_or_buf="./password.csv",columns=cols)

Password_generator(12)

