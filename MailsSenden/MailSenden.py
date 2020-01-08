import smtplib
from sprachassistent import Sprachassistent

assistent = Sprachassistent("assistent","german") #Assistent erstellen 

        
# Deine Daten muessen hier hin
name = ''
senderaddr = ''
user = ''
password = ''
mailBeginning = "Hallo,\n\n"
mailEnding = ".\n\nMit freundlichen Gruessen\n" + name + "\n\n\nDiese Nachricht wurde mit meinem Sprachassistenten erstellt und enthaelt moeglicherweise katastrophale Fehler"
         
# Gib an, an wen die Mail gesendet werden soll
assistent.startListener()   #Listener starten
assistent.say("An wen soll die mail gesendet werden")
while not assistent.listenerFinished() :    #Warten bis der listener fertig ist
    pass
answer = assistent.getListener() #Antwort zu Gesprochenem in Variable speichern
receiveraddr  = ''

         
# Betreff ermitteln
assistent.say("Der Betreff der Mail")
assistent.startListener()   #Listener starten
while not assistent.listenerFinished() :    #Warten bis der listener fertig ist
    pass
answer = assistent.getListener() #Antwort zu Gesprochenem in Variable speichern
subject = answer

# Nachricht ermitteln
assistent.say("Die Nachricht der Mail")
assistent.startListener()   #Listener starten
while not assistent.listenerFinished() :    #Warten bis der listener fertig ist
    pass
answer = assistent.getListener() #Antwort zu Gesprochenem in Variable speichern
message = mailBeginning + answer + mailEnding

# Ueberpruefen
assistent.say("Hier nochmal der Inhalt der Mail")
assistent.say(message)
assistent.say("Bestätige bitte mit ja")
assistent.startListener()   #Listener starten
while not assistent.listenerFinished() :    #Warten bis der listener fertig ist
    pass
answer = assistent.getListener() #Antwort zu Gesprochenem in Variable speichern
if answer == "ja":
    assistent.say("Ich sende die Nachricht")
    # Mail senden
    mailbody = 'Subject: %s\n\n%s' % (subject, message)
    server = smtplib.SMTP('smtp.googlemail.com:587')
    server.starttls()
    server.login(user,password)
    server.sendmail(senderaddr, receiveraddr, mailbody)
    server.quit()
    assistent.say("Mail wurde gesendet")




