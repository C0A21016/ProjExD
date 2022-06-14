
import random
import datetime
shutudai()
def shutudai():
    Q1 = "サザエの旦那の名前は？"
    Q2 = "カツオの妹の名前は？"
    Q3 = "タラオはカツオから見てどんな関係？"
    Q = [Q1,Q2,Q3]
    A1 = ["マスオ","ますお"]
    A2 = ["わかめ","わかめ"]
    A3 = ["甥","おい","甥っ子","おいっこ"]
    prnt(input(random.randint(Q)))
def kaito(ans):
    if ans in A1:
        print("正解!!")
    else:
        print("出直してこい")
