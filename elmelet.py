import random
import string
from tkinter import *
print(string.digits)
print(random.randint(1,8))

ablak=Tk()
ablak.title('Próba')
ablak.minsize=(200,100)

szoveg=Label(ablak,text='Szia!')
gomb=Button(ablak,text='Ok',command=ablak.destroy)

szoveg.pack()
gomb.pack()
mainloop()