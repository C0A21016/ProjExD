
import random
import datetime
Q1 = "サザエの旦那の名前は？"
Q2 = "カツオの妹の名前は？"
Q3 = "タラオはカツオから見てどんな関係？"
Q = [Q1,Q2,Q3]
def ma():
    se = shutudai()
    kaito(se)


def shutudai():
    print("問題 ")
    m = random.randint(0,2)
    print(Q[m])
    return Q[m]
def kaito(se):
    A1 = ["マスオ","ますお"]
    A2 = ["わかめ","わかめ"]
    A3 = ["甥","おい","甥っ子","おいっこ"]
    kai = input()
    if se == Q1:
        if kai in A1:
            print("正解!!")
        else:
            print("出直してこい")

    if se == Q2:
        if kai in A2:
            print("正解!!")
        else:
            print("出直してこい")

    if se == Q3:
        if kai in A3:
            print("正解!!")
        else:
            print("出直してこい")


if __name__ == "__main__":
    ma()
