from tkinter import *
from tkinter import ttk
from googletrans import Translator

root = Tk()

root.title("Translator")
root.geometry("500x500")
root.configure(bg="#eb74a8")

languages = ["English","Hindi"]

label = Label(root,text="LANGUAGE TRANSLATOR")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label1 = Label(root,text="ENTER TEXT")
label1.place(relx=0.2,rely=0.3,anchor=W)

text_area = Text(root,background="white",height=7,wrap=WORD,width=55,padx=3,pady=3,bd=0)
text_area.place(relx=0.2,rely=0.4,anchor=W)

dropdown_give = ttk.Combobox(root,state="readonly",values=languages)
dropdown_give.place(relx=0.3,rely=0.3,anchor=W)
dropdown_give.set("English")

label2 = Label(root,text="OUTPUT")
label2.place(relx=0.8,rely=0.3,anchor=E)

text_area1 = Text(root,background="white",height=7,wrap=WORD,width=55,padx=3,pady=3,bd=0)
text_area1.place(relx=0.8,rely=0.4,anchor=E)

dropdown_take = ttk.Combobox(root,state="readonly",values=languages)
dropdown_take.place(relx=0.7,rely=0.3,anchor=E)
dropdown_take.set("Choose Language")


def Translate():
    try:
        translator = Translator()
        translating = translator.translate(text = text_area.get(1.0, END),src=dropdown_give.get(),dest=dropdown_take.get())
        text_area1.delete(1.0, END)
        text_area1.insert(END, translating.text)
    except:
        print("TRY AGAIN")
        
        
btn = Button(root,text="TRANSLATE",command=Translate)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()