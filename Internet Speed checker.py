from tkinter import *
import tkinter
from tkinter import ttk
import speedtest

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+ "Mbps"
    up= str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp=Tk()
sp.title("Speed Tester")
sp.config(bg='#B7CEEC')
sp.geometry("700x900")


lab=Label(sp,text="Speed Test", font=("Times New Roman", 40 ,"bold"), bg="#B7CEEC")
lab.place(x=200,y=10,anchor=NW)

lab=Label(sp,text="Downloading speed:", font=("Times New Roman", 25 ,"bold"), bg="#B7CEEC")
lab.place(x=0,y=200,height=70,width=350,anchor=NW)

lab_down=Label(sp,text="00", font=("Times New Roman", 25 ,"bold"), bg="#B7CEEC")
lab_down.place(x=350,y=200,height=70,width=350,anchor=NW)

lab=Label(sp,text="Uploading speed:", font=("Times New Roman", 25 ,"bold"), bg="#B7CEEC")
lab.place(x=30,y=300)

lab_up=Label(sp,text="00", font=("Times New Roman", 25 ,"bold"), bg="#B7CEEC")
lab_up.place(x=350,y=300,height=70,width=350)

button=Button(sp,text="Check Speed",font=("Times New Roman", 30 ,"bold"),relief=RAISED , command=speedcheck)
button.place(x=200,y=600,height=70,width=310)

lab=Label(sp,text="Note: Please wait for sometime after pressing Check Speed Button", font=("Times New Roman", 15 ,"bold"), fg="red",bg="#B7CEEC")
lab.place(x=80,y=720,anchor=NW)
sp.mainloop()
