import schedule
import datetime
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

pythonclasstime = ['Monday', 'Wednesday', 'Friday']
digitallogictime = ['Tuesday', 'Wednesday', 'Thursday']
networkingclasstime = ['Monday', 'Wednesday', 'Friday']
fromaddr = ""
toaddr = ""
password = ""

# Run on scheduled cloud server, below code was for testing

# def job():
#     global pythonclasstime
#     global digitallogictime
#     global networkingclasstime

date = datetime.date.today().strftime("%A")
if date in pythonclasstime:
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
        part.add_header('Content-Disposition', "attachment; filename= %s"
                        % filename)
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
if date in networkingclasstime:
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
        part.add_header('Content-Disposition', "attachment; filename= %s"
                        % filename)
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
if date in digitallogictime:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Digital Logic class time and location"

        body = "Class time and location"

        msg.attach(MIMEText(body, 'plain'))

        filename = "digital_logic.jpg"
        attachment = open("digital_logic.jpg", "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s"
                        % filename)
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

# schedule.every().day.at("07:00").do(job)
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
