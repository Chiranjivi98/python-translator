from tkinter import *
from tkinter import ttk
from methods import MyTranslator


app=Tk()
app.geometry('350x520')
app.title('Google Translate')
app.resizable(0,0)
app.config(bg='#2B3856')
app.wm_iconbitmap('icon.ico')

def get():
    s=srcLangs.get()
    d=destLangs.get()
    message=sourceText.get(1.0,END)
    translator=MyTranslator()
    text=translator.run(txt=message,src=s,dest=d)
    destText.delete(1.0,END)
    destText.insert(END,text)

appName=Label(app,text='Translator',font=('arial',20),
              bg='#151B54',fg='goldenrod1',height=2)
appName.pack(side=TOP,fill=BOTH,pady=0)
version=Label(app,text='Cherry',bg='#000080').place(x=150,y=45)
frame=Frame(app).pack(side=BOTTOM)
sourceText=Text(frame,font=('arial',10),height=11,wrap=WORD)
sourceText.pack(side=TOP,padx=5,pady=5)


transBtn=Button(frame,text='Translate',font=('arial',10,'bold'),
                fg='Cyan',bg='#95B9C7',activebackground='#6495ED',
                relief=GROOVE,command=get)
transBtn.pack(side=TOP,pady=15)

langs=MyTranslator().langs

srcLangs=ttk.Combobox(frame,values=langs,width=10)
srcLangs.place(x=30,y=280)
srcLangs.set('english')

destLangs=ttk.Combobox(frame,values=langs,width=10)
destLangs.place(x=240,y=280)
destLangs.set('german')

destText=Text(frame,font=('arial',10),height=11,wrap=WORD)
destText.pack(side=TOP,padx=5,pady=5)
app.mainloop()
