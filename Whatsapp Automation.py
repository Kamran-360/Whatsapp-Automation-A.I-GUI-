from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyttsx3
import datetime
from plyer import notification
from webdriver_manager.chrome import ChromeDriverManager
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    print("Driver Not installed Check your Internet connection")
root = Tk()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) you can also use Female version
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!Sir")

    else:
        speak("Good Evening!Sir")

def Whatsapp_Automation():
    if(namevalue.get()==""):
        speak("Sir first fill the entries")
    else:
     # # try:
     #  driver = webdriver.Chrome()
      driver.get("https://web.whatsapp.com/")
      Label(root, text="Please scan QR code for whatsapp Web", font=("Helvetica 13 bold")).grid(row=4, column=3)
      speak("Please scan the QR code for whatsapp web")
      time.sleep(15)
      p=driver.find_element_by_css_selector(f"span[title={namevalue.get()}]")
      p.click()
      time.sleep(timevalue.get())
      put=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
      put.send_keys(textvalue.get())
      put.send_keys(Keys.RETURN)
       # notification.notify(
       #     title='Whatsapp Automation Says',
       #     message='Message Successfully sent sir!\nThanks for using our service',#you can also prefer Nottify
       #     app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
       #     timeout=10,  # seconds
       # )
      messagebox.showinfo("Whatsapp Automation", "Message Sent Successfully!")
      speak("Message Sent Successfully!")

     # except:
     #   speak("message not sent!")
if __name__ == '__main__':
  wishMe()
  root.title("Whatsapp Automation")
  root.geometry("1400x1400")
  Label(root,text="Welcome to Whatsapp Automation\nCreated by KAMI-360",fg="black",font=("Helvetica 19 bold"),pady=15).grid(row=0 , column=3)
  name = Label(root, text="Enter your friend's name you want to send message :",font=("Helvetica 13 bold"))
  text = Label(root, text="Enter your text Message:",font=("Helvetica 13 bold"))
  tm = Label(root, text="Enter Delay time in Seconds :",font=("Helvetica 13 bold"))
  #Packing
  namevalue = StringVar()
  textvalue = StringVar()
  timevalue = IntVar()

  name.grid(row=1, column=2)
  text.grid(row=2, column=2)
  tm.grid(row=3, column=2)


  nameentry = Entry(root, textvariable=namevalue,borderwidth=3, relief=SUNKEN)
  textentry = Entry(root, textvariable=textvalue,borderwidth=3, relief=SUNKEN)
  timeentry = Entry(root, textvariable=timevalue,borderwidth=3, relief=SUNKEN)
  nameentry.grid(row=1, column=3)
  textentry.grid(row=2, column=3,ipady=80,ipadx=80)
  timeentry.grid(row=3, column=3,ipady=2,ipadx=1)

  Button(text="send text", command=Whatsapp_Automation).grid(row=16, column=3)
  def cancel():
     sys.exit()
  Button(text="Exit", command=cancel).grid(row=17, column=3)
  image=Image.open("1.jpg")
  image = image.resize((325, 325), Image.ANTIALIAS)
  photo =ImageTk.PhotoImage(image)
  l2=Label(image=photo,anchor="e")
  l2.grid(row=2,column=5)
  Label(text="Message from developer",font=("Helvetica 13 bold")).grid(row=16,column=5)
  Label(text="Hi,I am Kamran Rasheed.I am a computer Scientist in Lahore.\nI have created this whatsapp automation using A.I,GUI programming techniques.\nYou can find me on instagrame N facebook with name\n #kamran360.pk and #Kamran Rasheed (Resp.).\nSo,Enjoy and do contact me for web designing N Application development😊").grid(row=17,column=5)
  Label(text="https://github.com/Kamran-360",font=("Helvetica 16 bold")).grid(row=18,column=5)
  speak("just fill the entry widgets and press send text button")

  root.mainloop()
