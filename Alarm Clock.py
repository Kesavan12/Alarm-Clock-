"""Done By P.R.Kesavan"""
"""Mini Project : Alaram Clock Using Python With GUI"""


from time import strftime       
from tkinter import * 
import time
import datetime
from pygame import mixer            #Importing Mixer from Pygame : For Loading and PLaying Sound 

root = Tk() 
root.title('My Alarm Clock')        

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 
        
def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 16, 'bold'),
            text="Time Up! Wake Up!",bg="Red",fg="white").grid(row=6,columnspan=3)
            print("wake up!")
            mixer.init()
            mixer.music.load(r'C:\Users\Asus\OneDrive\Documents\Python\Alaram Clock\Jack Sparrow.mpeg')
            mixer.music.play()
            break


hrs=StringVar()
mins=StringVar()
secs=StringVar()

titlename=Label(root, font = ('arial', 16, 'bold'),
text="Alarm:(Hr/Min/Sec)").grid(row=1,columnspan=3)

hour=Entry(root,textvariable=hrs,width=4,font =('arial', 20, 'bold'),bg="Yellow" ,fg="Red")
hour.grid(row=2,column=1)

min=Entry(root,textvariable=mins,
width=4,font = ('arial', 20, 'bold'),bg="Yellow" ,fg="Red").grid(row=2,column=2)

sec=Entry(root,textvariable=secs,
width=4,font = ('arial', 20, 'bold'),bg="Yellow" ,fg="Red").grid(row=2,column=3)

setbtn=Button(root,text="Set Alarm",command=setalarm,bg="Blue",
fg="white",font = ('arial', 16, 'bold')).grid(row=4,columnspan=3)

timeleft = Label(root,font=('arial', 16, 'bold')) 
timeleft.grid()
  
mainloop()