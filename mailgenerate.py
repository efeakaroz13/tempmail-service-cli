#By TheGreenAnarchist
#20 November 2022
# For ethical purposes(!)
import requests
from colorama import Fore
import json 
import os
import time 
from bs4 import BeautifulSoup
def printf(x):
    print(x)
art = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((( @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((( ((((((((((((((( @@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@((((((((@@/((((@@*(((((@@@(((((((((@@@@@@@ @@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@(((((((@@@@ (((((@@@ (((((@@@@@((((((((((((((/@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@((((((@@@@@ (((((@@@@@,(((((@@((((((((((((( @@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@((((((@@@@@@(((((@@@@@@@((((((((((((((((((@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@((((((@@@@@@((((((((((((((((((((.@@@@@(((((@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@((((((@@@@((((((((((((((((( ((((((@@@@@(((((@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@(((((((((((((((((@@@@@@@@@@@/(((((@@@@(((((@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@ (((((((((((((((@@@@@@@@@@@@@@(((((@@@((((((@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@ (((((((((@@*(((((@@@@@@@@@@@@@@@@(((((@*(((((@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@((((.@@(((((( (((((@@@@@@@@@@@@@@@@@@(((((((((( @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@((((((((( @@@@@@@@@@@@@@@@@@@(((((((*@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@.(((((((((((( @@@@@@@@*(((((((((((@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@((((@((((((((((((((((((((((( ((((@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@(((@@@@@@@@&((((((((((.@@@@@@@/(((@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@ ((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(( @@@@@@@@@@@@@@@@@@@
"""
os.system("clear")
print(Fore.LIGHTGREEN_EX,art.replace("@"," "),Fore.RESET)
print("Temp-Mail CLI by ",Fore.GREEN,"THEGREENANARCHIST",Fore.RESET)
print("Loading your mail...")
emailgot  = json.loads(requests.get("https://tmail2.p.rapidapi.com/mailbox",headers={"X-RapidAPI-Key": "62343ab3edmshb82941f2a48ed4fp170497jsn361d447cd4ce","X-RapidAPI-Host": "tmail2.p.rapidapi.com"}).content)
token = emailgot["token"]
email = emailgot["mailbox"]
os.system("clear")
print(Fore.LIGHTGREEN_EX,art.replace("@"," "),Fore.RESET)
print("Temp-Mail CLI by ",Fore.GREEN,"THEGREENANARCHIST",Fore.RESET)
print("Mail ",Fore.GREEN,"LOADED",Fore.RESET," : ",email)
while True:
    headers = {
        "Authorization": token,
        "X-RapidAPI-Key": "62343ab3edmshb82941f2a48ed4fp170497jsn361d447cd4ce",
        "X-RapidAPI-Host": "tmail2.p.rapidapi.com"
    }

    inbox = json.loads(requests.get("https://tmail2.p.rapidapi.com/messages",headers=headers).content)

    try:
        messages = inbox["messages"]
    except:
        messages = []
    for m in messages:
        recievedat = m["receivedAt"]
        msid = m["_id"]
        whois = m["from"]
        subject = m["subject"]
        bodyPreview = m["bodyPreview"]
        attachmentsCount = m["attachmentsCount"]
        toprint = f"""

        |     **{messages.index(m)}**
        |     From \u001b[34m{whois}\u001b[0m  - \u001b[33m{time.ctime(recievedat)}\u001b[0m
        |     
        |     \u001b[35mTitle\u001b[0m : {subject}
        |     
        |     \u001b[35mPreview \u001b[0m:{bodyPreview}
        |
        |     {attachmentsCount} 📎
        |
        \\---------------------------------------------------------
        """
        print(toprint)




    print("")
    print("Type R to reload inbox - write the number to get message details")
    command = input("Type>")
    command = command.lower().strip()
    if command.lower().strip() == "r":
        os.system("clear")
        print(Fore.LIGHTGREEN_EX,art.replace("@"," "),Fore.RESET)
        print("Temp-Mail CLI by ",Fore.GREEN,"THEGREENANARCHIST",Fore.RESET)
        print("Mail ",Fore.GREEN,"LOADED",Fore.RESET," : ",email)
    else:
        try:
            command = int(command)
        except:
            if command == "e" or command =="q" or command=="quit":
                exit()
            else:
                print("INVALID COMMAND")

        try:
            messages[command]
            messageid = messages[command]["_id"]
            url = "https://tmail2.p.rapidapi.com/messages/"+messageid
            msgdata = json.loads(requests.get(url,headers=headers).content)
            #print(json.dumps(msgdata,indent=4))
            receivedAt = time.ctime(msgdata["receivedAt"])
            sender = msgdata["from"]
            subject = m["subject"]
            bodyPreview = m["bodyHtml"]
            soup = BeautifulSoup(bodyPreview,"lxml")
            allinks=[]
            alllinks1 = soup.find_all("a")
            for a in alllinks1:
                href = a.get("href")
                text = a.get_text()
                allinks.append(f"{href} ~ {text}")
            attachments = m["attachments"]
            try:
                print(f"========== \u001b[36mMAIL\u001b[0m by {sender.split('<')[0]} ~ \u001b[33m{sender.split('<')[1].split('>')[0]}\u001b[0m ==========")
            except:
                print(f"========== MAIL by {sender} ==========")
            print(" \u001b[33m Time Sent\u001b[0m: {}".format())
            print(" \u001b[32mCONTENT START\u001b[0m")
            print(soup.get_text())
            print("\u001b[32mCONTENT END\u001b[0m")
            print("\u001b[35m======LINKS IN DOCUMENT======\u001b[0m")
            for link in allinks:
                print(f"\u001b[36m {link.split('~')[0]}\u001b[0m - {link.split('~')[1]} ")
            print("\u001b[35m============================\u001b[0m")
            print("\u001b[31mSUBJECT\u001b[0m:",subject)

            

        except Exception as e:
            print(Fore.RED,"ERR ",Fore.RESET,"| Message not in the list.")
        
