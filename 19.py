from tkinter import*
tk=Tk()
tk.geometry("600x600")
canvas=Canvas(tk,width=400,height=350)
canvas.pack()
flower_image=PhotoImage(file="images.png")
lbl2=Label(text="")
lbl2.place(x=150,y=150)
def btn1_click():
    select =list.curselection()
    lbl2.config(text= ent.get()+" "+list.insert(END, i))
    canvas.create_image(200,175,image=flower_image)
def btn2_click():
    print("прощавай ", ent.get(),"!",sep="")
btn1=Button(text="привітання",command=btn1_click)
btn1.place(x=75,y=75,width=100,height=50)
btn2=Button(text="вихід",command=tk.destroy)
btn2.place(x=225,y=75,width=100,height=50)
ent=Entry(bd=1)
ent.place(x=225,y=25,width=100,height=30)
lbl1=Label(text="ваше імя:") 
lbl1.place(x=75,y=25,width=100,height=30)

def f():
    print(list.get(list.curselection()))         

list = Listbox(tk, selectmode=SINGLE, width=15, height=3)           
list.pack(side=LEFT, padx=20)
for i in ['з новим роком', 'з днем народження', 'з іменинами']:                              #     
    list.insert(END, i)
lbl1.pack()
btn1.pack()
ent.pack()
btn2.pack()