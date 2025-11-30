from tkinter import *
pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("270x250+300+100")
pencere.resizable(FALSE,FALSE) #BOYUTUNU DEĞİŞTİRMEK İSTEMİYORUM.

depo = ""

def hesapla(tus):
    global depo
    if tus in "0123456789": # Tuslara tıklanıldı mı?
        ekran.insert(END,tus)
        depo = depo + tus

    if tus in "+-/*": #Simgeye tıkladıktan sonra depoya gönderdim;
        ekran.insert(END,tus)
        depo = depo + tus 

    if tus == "=":
        ekran.delete(0,END)
        hesap = eval(depo,{"__builtins__":None},{})#Hesaplamayı artık görmesi gerekiyor. #10/2 eval matematiksel işlemde sonuclandırıyor.
        depo =str(hesap)
        ekran.insert(END,depo) #artık sonucu gösterdim.

    if tus == "C":
        ekran.delete(0,END) #depoyu silelim.
        depo = ""





ekran = Entry(width=40,justify=RIGHT)
ekran.grid(row=0,column=0,columnspan=3,ipady=4)

#BUTTONS

liste = ["1","2","3","4","5","6","7","8","9","0","+","-","/","*","=","C"]

sira = 1
sutun = 0

for i in liste:
    komut = lambda x=i : hesapla(x)
    Button(text=i,font="verdana 8 bold",bg="#FFFACD",width=10,height=2,relief=GROOVE,command=komut).grid(row=sira,column=sutun)
    sutun += 1 #Her seferinde 1 arttırdım.0-1-2 
    if sutun >2: #2 den fazla artmasını istemiyorum.
        sutun = 0
        sira +=1 #Sırada her seferinde 1 artması gerekiyor ki alt satıra geçsin.


mainloop()


