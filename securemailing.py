from PyQt5 import QtWidgets, QtGui
import smtplib
import sqlite3
import sys
from base64 import b64encode
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QDialog, QTextEdit

class Window1(QDialog):
    def __init__(self):
        super(Window1, self).__init__()
        self.initUI()

    def initUI(self):
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0, 0, 640, 480)
        self.background.setPixmap(QtGui.QPixmap("background.jpg"))

        self.title = QtWidgets.QLabel(self)
        self.title.setText("SECURE EMAIL")
        self.title.move(220, 30)
        self.title.setFont(QFont('Arial', 20))
        self.title.setStyleSheet("color: white;")



        self.login_btn = QtWidgets.QPushButton(self)
        self.login_btn.setText("LOGIN")
        self.login_btn.setGeometry(220, 250, 100, 100)
        self.login_btn.clicked.connect(self.login)
        #self.login_btn.resize(100, 100)

        self.register_btn = QtWidgets.QPushButton(self)
        self.register_btn.setText("REGISTER")
        self.register_btn.move(420, 250)
        self.register_btn.clicked.connect(self.register)
        self.register_btn.resize(100, 100)

    def login(self):
        self.title.setText("this a new title")
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("LOGIN")

    def register(self):
        register = Register()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("REGISTER")


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.initUI()

    def initUI(self):
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0, 0, 640, 480)
        self.background.setPixmap(QtGui.QPixmap("background.jpg"))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("USERNAME")
        self.label1.move(250, 90)
        self.label1.setStyleSheet("color: white;")

        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(370, 90)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("PASSWORD")
        self.label2.move(250, 180)
        self.label2.setStyleSheet("color: white;")

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit2.move(370, 180)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.move(220, 30)

        self.login_btn1 = QtWidgets.QPushButton(self)
        self.login_btn1.setText("LOGIN")
        self.login_btn1.move(300, 280)
        self.login_btn1.clicked.connect(self.loggedin)

        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setText("BACK")
        self.back_btn.move(500, 20)
        self.back_btn.clicked.connect(self.back)

    def loggedin(self):

        user = self.lineedit1.text()
        pwd = self.lineedit2.text()
        if len(user) == 0 or len(pwd) == 0:
            self.label3.setText("Please input all fields.")
            self.label3.adjustSize()
        else:
            conn = sqlite3.connect("network.db")
            cur = conn.cursor()
            query = 'SELECT password FROM logins WHERE name =\'' + user + "\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == pwd:
                print("Successfully logged in.")
                self.label3.setText("")
                loggedin = ECD()
                widget.addWidget(loggedin)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                widget.setWindowTitle("DETECTION")
            else:
                self.label3.setText("Invalid username or password")
                self.label3.adjustSize()

    def back(self):
        back = Window1()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("SECURE EMAIL")


class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        self.initUI()

    def initUI(self):
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0, 0, 640, 480)
        self.background.setPixmap(QtGui.QPixmap("background.jpg"))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("USERNAME")
        self.label1.move(250, 90)
        self.label1.setStyleSheet("color: white;")

        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(370, 90)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("PASSWORD")
        self.label2.move(250, 180)
        self.label2.setStyleSheet("color: white;")

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit2.move(370, 180)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("PASSWORD")
        self.label3.move(250, 270)
        self.label3.setStyleSheet("color: white;")

        self.lineedit3 = QtWidgets.QLineEdit(self)
        self.lineedit3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit3.move(370, 270)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.move(220, 30)
        self.label4.setStyleSheet("color: white;")

        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setText("BACK")
        self.back_btn.move(500, 20)
        self.back_btn.clicked.connect(self.back)

        self.r_btn = QtWidgets.QPushButton(self)
        self.r_btn.setText("REGISTER")
        self.r_btn.move(300, 350)
        self.r_btn.clicked.connect(self.register)

    def back(self):
        back = Window1()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("SECURE EMAIL")

    def register(self):
        user = self.lineedit1.text()
        pwd = self.lineedit2.text()
        cpwd = self.lineedit3.text()
        if len(user) == 0 or len(pwd) == 0 or len(cpwd) == 0:
            self.label4.setText("Please fill in all inputs.")
            self.label4.adjustSize()

        elif pwd != cpwd:
            self.label4.setText("Passwords do not match.")
            self.label4.adjustSize()
        else:
            conn = sqlite3.connect("network.db")
            cur = conn.cursor()

            user_info = [user, pwd]
            cur.execute('INSERT INTO logins (name, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()
            self.label4.setText("Created user please login to continue")
            self.label4.adjustSize()

class ECD(QDialog):
    def __init__(self):
        super(ECD, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Send Secure Email")
        self.setGeometry(100, 100, 400, 200)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(20, 20)
        self.label1.setText("Enter Email Message:")
        self.label1.setStyleSheet("color: black")

        self.message = QtWidgets.QLineEdit(self)
        self.message.setGeometry(20, 50, 360, 30)
        self.message.setPlaceholderText("Enter your email message here")

        self.send_button = QtWidgets.QPushButton("SEND", self)
        self.send_button.setGeometry(20, 100, 160, 40)
        self.send_button.clicked.connect(self.send)

        self.decrypt_button = QtWidgets.QPushButton("DECRYPT", self)
        self.decrypt_button.setGeometry(220, 100, 160, 40)
        self.decrypt_button.clicked.connect(self.show_decrypt_window)

    def send(self):
        sender_email = 'logsecure@yandex.com'
        sender_password = 'eiqxwcptwjswpksv'
        recipient_email = 'anumodanu906@gmail.com'

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = 'Secure Email Example'

        # Encrypt your email content using AES
        message_text = self.message.text()
        key = get_random_bytes(16)
        with open('encryption_key.txt', 'wb') as key_file:
            key_file.write(key)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(message_text.encode())

        # Attach the encrypted message, the nonce, and the tag as MIME parts
        message.attach(MIMEText(b64encode(ciphertext).decode(), 'plain'))
        message.attach(MIMEText(b64encode(cipher.nonce).decode(), 'plain'))
        message.attach(MIMEText(b64encode(tag).decode(), 'plain'))

        try:
            # Connect to the SMTP server (in this case, Gmail)
            smtp_server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
            smtp_server.login(sender_email, sender_password)

            # Send the email
            smtp_server.sendmail(sender_email, recipient_email, message.as_string())
            with open('encrypted_message.txt', 'wb') as encrypted_file:
                encrypted_file.write(cipher.nonce + ciphertext)

            # Disconnect from the SMTP server
            smtp_server.quit()

            # Show a message box to indicate that the email has been sent
            QMessageBox.information(self, "Email Sent", "Email has been sent successfully!")

        except Exception as e:
            print(f'Error sending email: {e}')

    def show_decrypt_window(self):
        decrypt_window = DecryptWindow()
        decrypt_window.exec_()

class DecryptWindow(QDialog):
    def __init__(self):
        super(DecryptWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Decrypt Secure Email")
        self.setGeometry(100, 100, 400, 200)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(20, 20)
        self.label1.setText("Decrypted Message:")
        self.label1.setStyleSheet("color: black")

        self.decrypted_message = QTextEdit(self)
        self.decrypted_message.setGeometry(20, 50, 360, 100)
        self.decrypted_message.setReadOnly(True)

        self.decrypt_button = QtWidgets.QPushButton("DECRYPT", self)
        self.decrypt_button.setGeometry(20, 160, 160, 40)
        self.decrypt_button.clicked.connect(self.decrypt)

    def decrypt(self):
        try:
            with open('encryption_key.txt', 'rb') as key_file:
                key = key_file.read()

            with open('encrypted_message.txt', 'rb') as encrypted_file:
                encrypted_text = encrypted_file.read()
            nonce = encrypted_text[:16]
            ciphertext = encrypted_text[16:]
            cipher = AES.new(key, AES.MODE_EAX, nonce=encrypted_text[:16])
            decrypted_message_bytes = cipher.decrypt(ciphertext)
            decrypted_message = decrypted_message_bytes.decode('utf-8')
            self.decrypted_message.setPlainText(decrypted_message)
        except Exception as e:
            print(f'Error decrypting email: {e}')

app = QApplication(sys.argv)
welcome = Window1()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(400)
widget.setFixedWidth(640)
widget.setWindowTitle("SECURE EMAIL")
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")

