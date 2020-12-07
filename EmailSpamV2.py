import smtplib, ssl, time

print('\nTo use this to spam texts go here and format the persons number as an email (only works for top cellular carriers)\nhttps://freecarrierlookup.com/\n\nIt is also recommended that you use an alt gmail\n')

port = 465  # For SSL
smtp_server = 'smtp.gmail.com'

emails = input('Enter gmail accounts you wish to use as spammers seperated by spaces (one or more needed): ')
passwords = input('Enter gmail passwords for accounts seperated by spaces: ')
receiver_email = input('Enter the email you wish to spam: ')  # Enter receiver address
message = input('Enter the body message of the email: ')
count = int(input('How many times would you like the process to repeat? (numbers only): '))

context = ssl.create_default_context()

sep_mails = emails.split(' ')
sep_pass = passwords.split(' ')

for x in range(count):
    sent = x + 1
    for y in range(len(sep_mails)):
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sep_mails[y], sep_pass[y])
            server.sendmail(sep_mails[y], receiver_email, message)
    print(f'{sent}/{count} cycles complete!')


input('\nPress enter to close the application!')