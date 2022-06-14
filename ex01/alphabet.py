import random
import datetime
kurikaesi = 5
mojisuu = 10
kekkan = 2
cc = 0
count = 0
moji = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def mn():
    st = datetime.datetime.now()
    for h in range(kurikaesi):
        yy = shutudai()
        mondai(yy)
        if count == 2:
            break
    ed = datetime.datetime.now()
    print("所要時間は"+((ed-st).seconds)+"かかりました")
def shutudai():
    taisho = []
    kek = []
    for i in range(mojisuu):
        at = random.randint(0,25)
        taisho.append(moji[at])
    sy = ' '.join(taisho)
    print("対象文字 :")
    print(sy)
    for f in range(kekkan):
        nn = random.randint(0,9)
        ke = taisho.pop(nn)
        kek.append(ke)
    taisho = ' '.join(taisho)
    print("欠損文字 :")
    print(taisho)
    return kek
def mondai(kek):
    for n in range(kurikaesi):
        a1 = input("欠損文字はいくつあるでしょうか?")
        if int(a1) == kekkan:
            print("正解です.それでは、具体的に欠損文字数を1つずつ入力してください")
        else:
            print("不正解です.またチャレンジしてください")
            cc+=1
            break
        for r in range(kekkan):
            a2 = input(str(r+1)+"つ目の文字を入力してください :")
            if a2 in kek:
                kek.remove(a2)
                count +=1
                if count == 2:
                    print("正解!これでおわり")
                    return count
                    break
            if a2 not in kek:
                print("不正解です.またチャレンジしてください")
                cc += 1
                break
            
if __name__ == "__main__":
    mn()

