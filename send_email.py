
from email.message import EmailMessage
import smtplib
from scraper.scrape import mega_links, mega_subtext, create_custom_hn


articles = create_custom_hn(mega_links, mega_subtext)

email = EmailMessage()
email['from'] = 'Addison Frei'
email['to'] = 'afrei2005@gmail.com'
email['subject'] = 'Hacker News Top Reads'

email.set_content(str(articles))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # encryption method
    smtp.login('ztmtest34@gmail.com', 'cnor jyzq evzz opqa')
    smtp.send_message(email)