import requests,time,smtplib
from bs4 import BeautifulSoup as bs
from email.message import EmailMessage
from datetime import datetime


url = 'http://grades.must.edu.eg/'
grades = 'http://grades.must.edu.eg/ViewStudentGrades/Student_SemesterGrades'

senderEmail = ''
senderPassword = ''
receiverEmail = ''

uni_id = ''
uni_password = ''

checking_rate = 150     #Check every 150 ms

datalogin = {'Username': uni_id,
                'Password': uni_password}


PrevVersion = ""
FirstRun = True
while True:
    session = requests.Session()
    r = session.post(url, data = datalogin)
    o = session.post(grades, data={'DDLSemesters': '202210'})
    soup = bs(o.content, 'html.parser')
    results = ''
    for div in soup.find_all(class_ ='col-lg-11'):
        results = div.text.strip()
    # compare the page text to the previous version
    results = "".join([s for s in results.strip().splitlines(True) if s.strip()])
    results = results.replace("                                                                        ", "")
    if PrevVersion != results:
        # on the first run - just memorize the page
        if FirstRun == True:
            PrevVersion = results
            FirstRun = False
            print ("Start Monitoring "+ url+ ""+ str(datetime.now()))
        else:
            print ("Changes detected at: "+ str(datetime.now()))
            PrevVersion = results
            #Sending Email
            msg = EmailMessage()
            msg.set_content(results)
            msg['Subject'] = 'New Results is Here...'
            msg['From'] = senderEmail
            msg['To'] = receiverEmail
            with smtplib.SMTP_SSL('smtp.gmail.com', 465 ) as server :
                server.login(senderEmail,senderPassword)
                server.sendmail(senderEmail,receiverEmail, msg.as_string())
                print('Email was sent to ', reciever)
    else: print( "No Changes "+ str(datetime.now()))
    time.sleep(checking_rate)
    continue








