import urllib, urllib2
from bs4 import BeautifulSoup, Comment
import sys
# Send the mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email import Encoders
import datetime
now = datetime.datetime.now()
 
 

content = ''


#extracting YourStory Stories

print('Extracting YourStory Stories...')

url='https://yourstory.com/news/'
url_content = urllib2.urlopen(url).read()

soup = BeautifulSoup(url_content, "html.parser")

site_name = soup.find("meta",  property="og:site_name")
title = soup.find("meta",  property="og:title")
desc = soup.find("meta",  property="og:description")

 
content += ('<b>YS Top Stories</b> </br>'+'-'*50+'</br>')
for i,row in enumerate(soup.find_all('div',attrs={"class" : "title-small"})):
    if i > 9:
        break
    content += (str(i+1)+'. '+row.text.encode("utf-8").strip() + '</br>')
      
    #print '-'*(len(row.text.strip())/3)

content += '</br>------</br>'


#extracting Hacker News Stories


def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'</br>'+'-'*50+'</br>')
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text.encode("utf-8") + '\n' + '</br>') if tag.text!='More' else '')
        #print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
    return(cnt) 
    
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('</br>------</br>')
content +=('</br></br>End of Message')    


#lets send the email  

print('Composing Email...')

#update your email details

SERVER = "your smtp server"
FROM = "your from email id"
TO = "your to email ids" # can be a list
PASS = "your email id's password"


#fp = open(file_name, 'rb')
# Create a text/plain message
#msg = MIMEText('')
msg = MIMEMultipart()    

#msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top News Stories YS & HN [Automated Email]'+' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO

 
msg.attach(MIMEText(content, 'html'))
#fp.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER)
#server.set_debuglevel(1)
#server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()

 





