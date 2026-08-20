import smtplib# Replace these with your email and password
sender_email = 'logsecure@yandex.com'
sender_password = 'eiqxwcptwjswpksv'
recipient_email = 'anumodanu906@gmail.com'

# Create an encrypted message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Secure Email Example'
print("works")
# Encrypt your email content using AES
message_text = 'This is a secure email.'
key = get_random_bytes(16)  # 128-bit AES key
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(message_text.encode())
print(ciphertext, tag)
# Attach the encrypted message, the nonce, and the tag as MIME parts
message.attach(MIMEText(b64encode(ciphertext).decode(), 'plain'))
message.attach(MIMEText(b64encode(cipher.nonce).decode(), 'plain'))
message.attach(MIMEText(b64encode(tag).decode(), 'plain'))

# Connect to the SMTP server (in this case, Gmail)
smtp_server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
smtp_server.login(sender_email, sender_password)

# Send the email
smtp_server.sendmail(sender_email, recipient_email, message.as_string())


# Disconnect from the SMTP server
smtp_server.quit()
print("works1")
print("works1")
print('Email sent securely with AES encryption using pycryptodome.')

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

