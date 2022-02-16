import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import playsound



import os, time



tts = gTTS(text="Project: Voice based Email for blind", lang='en')
ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/1.mp3") 

tts.save(ttsname)


playsound.playsound(ttsname)
os.remove(ttsname)


#login from os
login = os.getlogin
print ("You are logging from : "+login())





#if text == '1' or text == 'One' or text == 'one' or text == 'compose' or text == 'composed' :


r = sr.Recognizer() #recognize uname

mic=sr.Microphone()

with mic as source:
    print ("your username :")
    tts = gTTS(text="Please say your emailid or Username ", lang='en')
    ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/7.mp3") 
    tts.save(ttsname)
   
    playsound.playsound(ttsname)
    os.remove(ttsname)
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source,timeout=120)
    print ("ok done!!")
    
    try:
        text2=r.recognize_google(audio)
        print ("You said : "+text2)
        tts = gTTS(text="you said  "+text2, lang='en')
        ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/8.mp3") 
        tts.save(ttsname)
   
        playsound.playsound(ttsname)
        os.remove(ttsname)
        uname = text2.replace(" ","")
        print(uname)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#if text == '1' or text == 'One' or text == 'one' or text == 'compose' or text == 'composed' :
    
r = sr.Recognizer() #recognize uname

mic=sr.Microphone()

with mic as source:
    print ("your password :")
    tts = gTTS(text="Please say password ", lang='en')
    ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/90.mp3") 
    tts.save(ttsname)
   
    playsound.playsound(ttsname)
    os.remove(ttsname)
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source,timeout=120)
    print ("ok done!!")
    
    try:
        text3=r.recognize_google(audio)
        print ("You said : "+text3)
        tts = gTTS(text="you said  "+text3, lang='en')
        ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/101.mp3") 
        tts.save(ttsname)
   
        playsound.playsound(ttsname)
        os.remove(ttsname)
        pwd = text3.replace(" ","")
        print(pwd)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))        
        
        
            

#choices
print ("1. compose a mail.")
tts = gTTS(text="option 1. composed a mail.", lang='en')
ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/2.mp3") 
tts.save(ttsname)


playsound.playsound(ttsname)
os.remove(ttsname)


print ("2. Check your inbox")
tts = gTTS(text="option 2. Check your inbox", lang='en')
ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/3.mp3")
tts.save(ttsname)

playsound.playsound(ttsname)
os.remove(ttsname)

#this is for input choices

tts = gTTS(text="Your choice ", lang='en')
ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/4.mp3") 
tts.save(ttsname)


playsound.playsound(ttsname)
os.remove(ttsname)

#voice recognition part
r = sr.Recognizer()
mic=sr.Microphone()
with mic as source:
    print ("Your choice:")
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
    
    print ("ok done!!")

try:
    text=r.recognize_google(audio)
    print ("You said : "+text)
    tts = gTTS(text="you said "+text, lang='en')
    ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/5.mp3") 
    tts.save(ttsname)
   
    playsound.playsound(ttsname)
    os.remove(ttsname)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
     
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

#choices details
if text == '1' or text == 'One' or text == 'one' or text == 'compose' or text == 'composed' :
   
    r = sr.Recognizer() #recognize rmail
    mic=sr.Microphone()
    with mic as source:
        print ("Your receiver mail :")
        tts = gTTS(text="Say your receiver mail id", lang='en')
        ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/6.mp3") 
        tts.save(ttsname)
   
        playsound.playsound(ttsname)
        os.remove(ttsname)
        
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,timeout=120)
        print ("ok done!!")
    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        rmail = text1.replace(" ","")
        print(rmail)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#if text == '1' or text == 'One' or text == 'one' or text == 'compose' or text == 'composed' :
        
    r = sr.Recognizer() #recognize msg
    mic=sr.Microphone()
    with mic as source:
        print ("your message :")
        tts = gTTS(text="Please say your message", lang='en')
        ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/11.mp3") 
        tts.save(ttsname)
   
        playsound.playsound(ttsname)
        os.remove(ttsname)
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,timeout=60)
        print ("ok done!!")
    try:
        text4=r.recognize_google(audio)
        print ("You said : "+text4)
        tts = gTTS(text="you said  "+text4, lang='en')
        ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/12.mp3") 
        tts.save(ttsname)
   
        playsound.playsound(ttsname)
        os.remove(ttsname)
        msg = text4.replace(" "," ")
        print(msg)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        


    mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
    mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
    mail.starttls() #security connection
    mail.login(uname+"@gmail.com",pwd) #login part
    mail.sendmail(uname+"@gmail.com",rmail+"@gmail.com",msg) #send part
    print ("Congrats! Your mail has send. ")
    tts = gTTS(text="Congrats! Your mail has send. ", lang='en')
    ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/13.mp3") 
    tts.save(ttsname)
   
    playsound.playsound(ttsname)
    os.remove(ttsname)
    mail.close()






if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' or text== 'inbox' :
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
    

    mail.login(uname+"@gmail.com",pwd)  #login
    stat, total = mail.select('Inbox')  #total number of mails in inbox
    print ("Number of mails in your inbox :"+str(total))
    tts = gTTS(text="Total mails are :"+str(total), lang='en') #voice out
    ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/18.mp3")
    tts.save(ttsname)
    
    playsound.playsound(ttsname)
    os.remove(ttsname)
    
    #unseen mails
    unseen = mail.search(None, 'UnSeen') # unseen count
    print ("Number of UnSeen mails :"+str(unseen))
    tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
    ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/19.mp3") 
    tts.save(ttsname)
    playsound.playsound(ttsname)
    os.remove(ttsname)
    
    #search mails
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
    raw_email = email_data[0][1].decode("utf-8") #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/20.mp3") 
    tts.save(ttsname)
    
    playsound.playsound(ttsname)
    os.remove(ttsname)
    
    #Body part of mails
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    tts = gTTS(text="Body: "+txt, lang='en')
    ttsname=(r"C:\Users\MY PC\AppData\Local\Programs\Python\Python38/21.mp3") 
    tts.save(ttsname)
   
    playsound.playsound(ttsname)
    os.remove(ttsname)
    mail.close()
    mail.logout()
