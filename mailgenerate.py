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
if __name__ == "__main__":
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
                print(messages[command])
                messageid = messages[command]["_id"]
                url = "https://tmail2.p.rapidapi.com/messages/"+messageid
                msgdata = json.loads(requests.get(url,headers=headers).content)
                #print(json.dumps(msgdata,indent=4))
                receivedAt = time.ctime(msgdata["receivedAt"])
                sender = msgdata["from"]
                subject = m["subject"]
                try:
                    bodyPreview = m["bodyHtml"]
                except:
                    bodyPreview = "<h2>No Body Content!</h2>"
                soup = BeautifulSoup(bodyPreview,"lxml")
                allinks=[]
                alllinks1 = soup.find_all("a")
                for a in alllinks1:
                    href = a.get("href")
                    text = a.get_text()
                    allinks.append(f"{href} ~ {text}")
                
                try:
                    print(f"========== \u001b[36mMAIL\u001b[0m by {sender.split('<')[0]} ~ \u001b[33m{sender.split('<')[1].split('>')[0]}\u001b[0m ==========")
                except:
                    print(f"========== MAIL by {sender} ==========")
                print(" \u001b[33m Time Sent\u001b[0m: {}".format(receivedAt))
                print(" \u001b[32mCONTENT START\u001b[0m")
                print(soup.get_text())
                print("\u001b[32mCONTENT END\u001b[0m")
                print("\u001b[35m======LINKS IN DOCUMENT======\u001b[0m")
                for link in allinks:
                    print(f"\u001b[36m {link.split('~')[0]}\u001b[0m - {link.split('~')[1]} ")
                print("\u001b[35m============================\u001b[0m")
                print("\u001b[31mSUBJECT\u001b[0m:",subject)

                

            except Exception as e:
                print(e)
                print(Fore.RED,"ERR ",Fore.RESET,"| Message not in the list.")
            
else:
    class TGAMail:
        def __init__(self,save=False):
            self.save= save
            self.headers={"X-RapidAPI-Key": "62343ab3edmshb82941f2a48ed4fp170497jsn361d447cd4ce","X-RapidAPI-Host": "tmail2.p.rapidapi.com"}
        def getemail(self):
            emaildata = json.loads(requests.get("https://tmail2.p.rapidapi.com/mailbox",headers=self.headers).content)

            self.token = emaildata["token"]
            self.email = emaildata["mailbox"]
            if self.save == True:
                try:
                    data = json.loads(open("data.json","r").read())
                except:
                    data = {}
                try:
                    data["emails"][self.email]= {"email":self.email,"token":self.token}
                except:
                    data["emails"] = {}
                    data["emails"][self.email]= {"email":self.email,"token":self.token}
                saver = open("data.json","w")
                saver.write(json.dumps(data,indent=4))

            else:
                pass 
            return {"email":self.email,"token":self.token}
        """
        def getinbox(self,email=None):
            if email == None:
                email = self.email
                token = self.token 
            else:
                alldata = json.loads(open("data.json","r").read())
                try:
                    alldata["emails"][email]
                    email = alldata["emails"][email]["email"]
                    token = alldata["emails"][email]["token"]
                except:
                    raise ValueError('The email you requested is not existing in the data.json file in your working directory')

            headers2= self.headers
            headers2["Authorization"] = token

            inboxofemail = json.loads(requests.get("https://tmail2.p.rapidapi.com/messages",headers=headers2).content)
            try:
                self.messages = inboxofemail["messages"]
            except:
                self.messages = []
            def details(self,emailindex=0):
                if emailindex > len(self.messages)-1:
                    raise IndexError("TGA disposable mail error | inbox out of range")
                else:
                    self.subject = messages[emailindex]


            return inboxofemail
        """

    class getinbox(TGAMail):
        def __init__(self,email=None):
            super().__init__()
            if email == None:
                email = self.email
                token = self.token 
            else:
                alldata = json.loads(open("data.json","r").read())
                try:
                    alldata["emails"][email]
                    email = alldata["emails"][email]["email"]
                    token = alldata["emails"][email]["token"]
                except:
                    raise ValueError('The email you requested is not existing in the data.json file in your working directory')

            headers2= self.headers
            headers2["Authorization"] = token

            inboxofemail = json.loads(requests.get("https://tmail2.p.rapidapi.com/messages",headers=headers2).content)
            try:
                self.messages = inboxofemail["messages"]
            except:
                self.messages = []
            #return inboxofemail



        def details(self,emailindex=0):
            if emailindex > len(self.messages)-1:
                raise IndexError("TGA disposable mail error | inbox out of range")
            else:
                self.email = self.messages[emailindex]




