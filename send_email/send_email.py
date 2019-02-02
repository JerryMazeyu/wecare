from email.mime.text import MIMEText
import smtplib
import configparser
class SendEmail(object):
    def __init__(self, to_addr, msg_text, subject="你好，这是来自wecare的消息"):
        conf = configparser.ConfigParser()
        conf.read_file(open('sendemail_para.ini'))
        from_addr = conf.get("email", "from_addr")
        smtp_server = conf.get("email", "smtp_server")
        password = conf.get("email", "password")
        self.to_addr = to_addr
        self.from_addr = from_addr
        self.smtp_server = smtp_server
        self.password = password
        self.msg_text = msg_text
        self.subject = subject

    def send_email(self):
        msg = MIMEText(self.msg_text, 'plain', 'utf-8')
        msg['from'] = self.from_addr
        msg['to'] = self.to_addr
        msg['Subject'] = self.subject
        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, self.to_addr, msg.as_string())
        server.quit()
        print("send_email success!")

if __name__ == '__main__':
    text = "这条消息十分重要，我是一个真正的猪猪男孩哦"
    mail = SendEmail("jerry_mazeyu@163.com", text)
    mail.send_email()
