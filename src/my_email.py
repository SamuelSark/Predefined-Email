#PROJECT 1
#sending email at predefined time and date via Yahoo email
import smtplib
import datetime as dt
import time
import configuration_file
import email_buildingblocks_file
from clrprint import *
#sends the email
def send_email():
    try:
        with smtplib.SMTP("smtp.mail.yahoo.com",587) as smtp:
            
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(configuration_file.senders_email, configuration_file.password)
            message = f"Subject: {email_buildingblocks_file.subject}\n\n{email_buildingblocks_file.body}"
            smtp.sendmail(configuration_file.senders_email, configuration_file.recievers_email, message)
            print('')
            clrprint("email has been successfully & safely sent", clr = 'green')
            smtp.quit()    
    except :
        print('')
        clrprint("email was not sent successfully", clr = 'red')

# waits the proper amount of time in terms of date and time before the sending the email
def waiting_time(year,month,day,hour,minute):
    # first 3 arugments are : date(year, month, day) and last 2 arguments are: time(hour, minute)
    predefined_date_time = dt.datetime(int(year),int(month),int(day),int(hour),int(minute))
    #program waits until the current time reaches the predefined_date_time,
    #which will lead to the program to send the email
    time.sleep(predefined_date_time.timestamp() - time.time())
    
# takes user input to know what date and what time to send the email
# then calls te waiting_time and send_email function
def main():
    print("predefine when you would like to send this email.")
    year = input("What year whould you like to send this? ")
    month = input("What month whould you like to send this? ")
    day = input("What day whould you like to send this? ")
    hour = input("What hour of the desired day whould you like to send this? ")
    minute = input("What minute of the desired hour whould you like to send this?")
    #calls waiting_time funciton with the arguments taken from user input
    waiting_time(year,month,day,hour,minute)
    # calls send_email function
    send_email()
main()


