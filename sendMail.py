import requests
from bs4 import BeautifulSoup as bs
import time
from smtplib import SMTP

# Simple Mail Transfe Protocol
try:
    url = 'https://altin.doviz.com/gram-altin'
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    gold_value = soup.find(class_='value').contents
    lowThreshold = '410'
    highThreshold = '430'
    x = True
    while x:
        if gold_value[0] < lowThreshold:
            x = False
            subject = "Altın düştü."
            message = gold_value[0] + ' Altın Alınız.'
            content = "Subject: {0}\n\n{1}".format(subject, message)

            # Hesap Bilgileri#
            mail_adress = "example@example.com"
            password = "passwordexample"

            # Kime gönderileceği#

            sent = "sentexample@emple.com"

            mail = SMTP("smtp.gmail.com", 587)

            mail.ehlo()
            mail.starttls()
            mail.login(mail_adress, password)
            mail.sendmail(mail_adress, sent, content.encode("utf8"))
            print("Mail Has Been Sent")
        if gold_value[0] > highThreshold:
            x = False
            subject = "Altın çıktı."
            message = gold_value[0] + ' Altınızı Satınız'
            content = "Subject: {0}\n\n{1}".format(subject, message)

            # Hesap Bilgileri#
            mail_adress = "example@example.com"
            password = "passwordexample"

            # Kime gönderileceği#

            sent = "sentexample@emple.com"

            mail = SMTP("smtp.gmail.com", 587)

            mail.ehlo()
            mail.starttls()
            mail.login(mail_adress, password)
            mail.sendmail(mail_adress, sent, content.encode("utf8"))
            print("Mail Has Been Sent")
        else:
            print(gold_value[0])
            time.sleep(5)



except Exception as e:
    print("hata olustu\n {0}".format(e))

