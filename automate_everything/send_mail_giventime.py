import time
import yagmail
import config
from datetime import datetime as dt

PASSWORD = config.PASSWORD
sender = 'it.sunil77@gmail.com'
sender_name = "Sunil"
receiver = 'trk7777@bencidarn.store'

smtp = yagmail.SMTP(user=sender, password=PASSWORD)
# hour = dt.now().hour
# minute = dt.now().minute

subject = "Not again"
email_body = f"""
<b>Hi there</b>

i am here again...

regards,
<i>{sender_name}</i>
sent on {dt.now()}
"""

while True:
    hour = dt.now().hour
    minute = dt.now().minute
    if hour == 14 and minute == 56:
        smtp.send(to=receiver, subject=subject,
                  contents=email_body, prettify_html=True)
        print('mail sent')
        break

    print(f"{hour},{minute},")
    time.sleep(60)
