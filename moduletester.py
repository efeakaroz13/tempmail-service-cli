#Developed by The GreenAnarchist
import mailgenerate
from colorama import Fore

print(Fore.RED,"Welcome to the TGA disposable email example",Fore.RESET)
gen = mailgenerate.TGAMail(save=True)
inbox = mailgenerate.getinbox("jipefi4166@kuvasin.com")
print(inbox.messages)
