
import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    button =event.widget
    num=button["text"]
    if num=="=":
        eq=entry.get()
        entry.delete(0,tk.END)
        re=eval(eq)
        return entry.insert(tk.END,re)
    elif num=="←":
        et=entry.get()
        aa = len(et)
        entry.delete(aa-1,tk.END)
    elif num=="p":
        entry.delete(0,tk.END)
        re="ぱわー！！"
        entry.insert(tk.END,re)
    elif num=="Zz":
        tkm.showinfo("寝よか")
    elif num=="C":
        entry.delete(0,tk.END)

        

    else:
        entry.insert(tk.END,num)
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x700")
    root.title("超高機能電卓")
    entry=tk.Entry(root, justify="right",width=10,font=("Times New Roman",40))
    entry.grid(column=0,columnspan=5)
    r,c=1,0
    pi=3.14

    for i, num in enumerate(["C","-","/","*","Zz","p","pi","←",9,4,8,7,6,5,3,2,1,0,"+","="]):
        button = tk.Button(root,text=f"{num}", width=4,height=2, font=("Times New Roman", 30))
        button.bind("<1>",button_click)
        button.grid(row=r,column=c)
        c+=1
        if (i+1)%5==0:
            r+=1
            c = 0
       
    root.mainloop()