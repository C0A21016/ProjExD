
import random
import datetime


def shutudai():
    Q1 = "サザエの旦那の名前は？"
    Q2 = "カツオの妹の名前は？"
    Q3 = "タラオはカツオから見てどんな関係？"
    Q = [Q1,Q2,Q3]
    print("問題 ")
    m = random.randint(Q)
    print(m)
    return m
def kaito(m):
    A1 = ["マスオ","ますお"]
    A2 = ["わかめ","わかめ"]
    A3 = ["甥","おい","甥っ子","おいっこ"]
    if m == Q1:
        if m in A1:
            print("正解!!")
    if m == Q2:
        if m in A2:
            print("正解!!")
    if m == Q3:
        if m in A3:
            print("正解!!")
    else:
        print("出直してこい")

if __name__ == "__main__":
    shutudai()
    kaito(m)
