import requests,time,smtplib
from bs4 import BeautifulSoup as bs
from email.message import EmailMessage
from datetime import datetime


url = 'http://grades.must.edu.eg/'
grades = 'http://grades.must.edu.eg/ViewStudentGrades/Student_SemesterGrades'


datalogin = {'Username': '81062',
                'Password': '3cca5'}


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
            sender = 'smilelife444@gmail.com'
            reciever = 'osamasaid2009@gmail.com'
            msg = EmailMessage()
            msg.set_content(results)
            msg['Subject'] = 'New Results is Here...'
            msg['From'] = 'smilelife444@gmail.com'
            msg['To'] = 'osamasaid2009@gmail.com'
            with smtplib.SMTP_SSL('smtp.gmail.com', 465 ) as server :
                server.login(sender,'Smile@Life444')
                server.sendmail(sender,reciever, msg.as_string())
                print('Email was sent to ', reciever)
    else: print( "No Changes "+ str(datetime.now()))
    time.sleep(150)
    continue








