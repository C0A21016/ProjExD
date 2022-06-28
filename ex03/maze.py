import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as ml
def key_down(event):
    global key
    key= event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy,mx,my
    if key == "Up" and maze_bg[my-1][mx]==0: my -= 1
    if key == "Down" and maze_bg[my+1][mx]==0: my += 1
    if key == "Left" and maze_bg[my][mx-1]==0: mx -= 1
    if key == "Right" and maze_bg[my][mx+1]==0: mx += 1
    cx,cy = mx*100+50,my*100+50
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)

def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    key=event.keysym
    jid=root.after(1000,count_up)

def count_up():
        global tmr, jid
        tmr = tmr+1
        label["text"]=tmr
        jid = root.after(1000,count_up)

def button_click(event):
    btn= event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"諦めるな！！")
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")
    canvas = tk.Canvas(root, width=1500,height=900, bg ="black")
    label = tk.Label(root,
            font=("Times New Roman",80)
            )
    label.pack()
    tmr=0
    jid = None
    button= tk.Button(root, text="もうむりだ",command=button_click)
    button.bind("<1>", button_click)
    button.pack()

    canvas.pack()
    maze_bg = ml.make_maze(15,9)
    ml.show_maze(canvas,maze_bg)
    tori = tk.PhotoImage(file="ex03/fig/3.png")

    mx, my = 1,1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag ="tori")
    key=""

    root.bind("<KeyPress-T>,<t>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()