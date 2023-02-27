import yagmail
import os
import config
PASSWORD = config.PASSWORD

sender = 'it.sunil77@gmail.com'
receiver = 'trk7777@bencidarn.store'
smtp = yagmail.SMTP(user=sender, password=PASSWORD)

subject = 'Hi'
mail_body = f"""
hi,
how are you doing today.add()

regards,
{sender}
"""

smtp.send(to=receiver, subject=subject, contents=mail_body, prettify_html=True)
print(f'mail sent to {receiver}')
