import smtplib

to = input("Add receivers email address plez: - ")

message = input('Enter your message:  - ')

def send_Email(to, message):
    server = smtplib.smtp('smtp.gmail.com', '587')
    server.starttls()
    server.login('nabbtest123@gmail.com', 'Nabking123 ')
    server.sendmail('sendermail', to  , message)
    server.close() 


    send_Email(to, message)


    #nabbtest123@gmail.com
    #Nabking123