import yagmail

from mail_header import receivers
from mail_header import sender_id, sender_password
from mail_header import subject, in_copy
from email_body import body_txt

yagmail.register(sender_id, sender_password)
yag = yagmail.SMTP(sender_id)

if __name__ == "__main__":

    for receiver in receivers:

        yag.send(to=receiver,
                 cc=in_copy,
                 subject=subject,
                 contents=body_txt)
