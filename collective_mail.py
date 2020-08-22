import smtplib
import webbrowser
import sys
import time
import getpass

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('collective_mail.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('\nBanner File not found!!!')


userid = input("\nEnter your G-Mail id :\t")
passwd = getpass.getpass("\nEnter your Password :\t")
subj = input("\nEnter the Subject (optional) :\n\n")
body = input("\nEnter the Message :\n\n")
count = int(input("\nEnter no. of Mails to send :\t"))
message = ("From :\t" + userid + "\nSubject :\t" + subj + "\n" + body)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

try:
	server.login(userid, passwd)
except smtplib.SMTPAuthenticationError:
	print("\nYour G-Mail id or Password maybe incorrect!!!\n") 
	print("\nOr maybe you have disablead Less-Secure-Apps on your G-Mail account!!!\n")
	resp = int(input("\nEnter 1 to enable Less-Secure-Apps now or Enter 0 to ignore :\n\n"))
	if (resp == 1):
		webbrowser.open('http://myaccount.google.com/lesssecureapps', new=2) 
		sys.exit()

n = int(input("\nEnter no. of G-Mail accounts you want to send this mail to :\t"))

for i in range (0,n):
	target = input("\nEnter G-Mail id no." + i + " :\t")
	try:
		server.sendmail(userid, target, message)
		print ("\nSuccessfully sent Mail to " + i + " Account !!!\n")
		time.sleep(1)
	except KeyboardInterrupt:
		print ("\nCanceled!!!\n")
		sys.exit()
	except:
		print ("\nFailed to Send!!!\n")