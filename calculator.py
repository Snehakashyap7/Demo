from tkinter import *
# from tkinter import messagebox
def on_click(event):
    text=event.widget.cget("text")
    if text =="=":
        try:
            result=eval(str(scvalue.get()))
            scvalue.set(result)
        except Exception as e:
             scvalue.set("Error")
    elif text=="C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get()+text)

  
root=Tk()
root.title("Calculator")
root.geometry('257x320') h
root.config(bg='black')
# root.wm_iconbitmap("cal.icon.png")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font='arial 34 bold',background='orange').pack(fill=X ,ipadx=10,pady=10,padx=10)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

frame = Frame(root)
frame.pack()
for row in buttons:
    row_frame = Frame(frame)
    row_frame.pack()
    for btn_text in row:
        btn = Button(row_frame, text=btn_text, font=("Arial", 14), padx=20, pady=10)
        btn.pack(side=LEFT, expand=True, fill=BOTH)
        btn.bind("<Button-1>", on_click)


       

       


 

root.mainloop()