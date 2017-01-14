# Top News Stories (Automated Outlook Email)

A Batch triggered Py Code that can send an Outlook email with **Top New Stories** from [YourStory](https://yourstory.com/) and [HackerNews](https://news.ycombinator.com/). The idea is present this simple solution which can be used by other news lovers working in offices with Outlook to get it delivered in their inbox. 

Email Screenshot:

![Screenshot](/top_news_stories.PNG)

### How to use the code:

* Download both the Py and .bat (Batch) file
* Install required Packages
* Update your Email details
  SERVER = "your smtp server"
  FROM = "your from email id"
  TO = "your to email ids" # can be a list
  PASS = "your email id's password"
* Make sure your file path in the .bat file is rightly referenced to the Py file
* Use Windows Task Scheduler to automate the email as per your wish 

### Further Improvements:

* Adding Links along with the Stories Headlines
