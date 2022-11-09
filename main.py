#jelszógenerátor
'''import fuggveny
print(fuggveny.jelszogenerator(8,True,True))
'''
from objektum import *
p=Jelszoobjektum()
print(p.jelszogeneralas_alap())
import fuggveny
from tkinter import *

def jelszokiiras():
    fuggveny.jelszogenerator(10, True, True)
    jelszocimke.pack()
ablak=Tk()
ablak.title('Jelszógenerálás')
cimke=Label(ablak,text='A jelszó:',fg='red')
jelszocimke=Label(ablak,text=fuggveny.jelszogenerator(10,True,True))
ok_gomb=Button(ablak,text='Ok',command=ablak.destroy)
jelszogomb=Button(ablak,text='Generálás',command=jelszokiiras())
cimke.pack()
ok_gomb.pack()
jelszogomb.pack()
mainloop()

