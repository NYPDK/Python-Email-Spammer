import smtplib, ssl, threading
#https://freecarrierlookup.com lets you format phone numbers as emails... spamming texts this way may be delayed

#Edit here to configure spam 
class Settings:
    target = "Example@gmail.com"
    message = "Example"
    amount = 15

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
                    
            except Exception:
                print(f"Error sending email from: {self.email}")
        
def init(target, message, amount):
    file = open("Emails.txt")
    content = file.readlines()
    print(f"Using {len(content)} email account(s)")
    for line in content:
        info = line.split(":")
        thread = Loop(info[0], info[1], target, message, amount)
        thread.start()

if __name__ == "__main__":
    init(Settings.target, Settings.message, Settings.amount)
