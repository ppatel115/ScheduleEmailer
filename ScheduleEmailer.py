import datetime
import schedule
import request
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

pythonclasstime = [('Monday', '08:15'),
                   ('Wednesday', '08:15'), ('Friday', '08:15')]
digitallogictime = [('Tuesday', '08:15'), ('Thursday', '09:20')]
networkingclasstime = [('Monday', '10:40'),
                       ('Wednesday', '10:40'), ('Friday', '10:40')]


def job():
    global pythonclasstime
    global networkingclasstime
    date = datetime.datetime.now().strftime("%A %H:%M")
    for i in pythonclasstime:
        runTime = i[0] + " " + i[1]
        if i and date == str(runTime):
            fromaddr = "priyampatel115@gmail.com"
            toaddr = "priyampatel97@yahoo.com"

            msg = MIMEMultipart()

            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Python class time and location"

            body = "Class time and location"

            msg.attach(MIMEText(body, 'plain'))

            filename = "python_class.jpg"
            attachment = open("python_class.jpg", "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "lionKing21")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
    for j in networkingclasstime:
        runTime = j[0] + " " + j[1]
        if j and date == str(runTime):
            fromaddr = "priyampatel115@gmail.com"
            toaddr = "priyampatel97@yahoo.com"

            msg = MIMEMultipart()

            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Networking class time and location"

            body = "Class time and location"

            msg.attach(MIMEText(body, 'plain'))

            filename = "networking_class.jpg"
            attachment = open("networking_class.jpg", "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "lionKing21")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()


schedule.every().day.at("08:15").do(job)
schedule.every().day.at("09:20").do(job)
schedule.every().day.at("10:40").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
