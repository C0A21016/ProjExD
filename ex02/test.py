
import tkinter as tk 
root = tk.Tk()
root.title("taitle")
root.geometry("500x200")
label = tk.Label(root,
                text = "ラベルを書いてみた件"
                )
button = tk.Button(root, text="押すな")
button.pack()
entry = tk.Entry(width=30)
entry.insert(tk.END, "fugapiyo")
entry.pack()
label.pack()
root.mainloop()