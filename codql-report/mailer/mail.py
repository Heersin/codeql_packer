import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from . import shadow

def send_mail_with_pdf(title, pdf_path, txt="Attachment is the scan report"):
    ret = True
    try:
        msg = MIMEMultipart()
        msg.attach(MIMEText(txt, "plain"))
        msg['Subject'] = title
        msg['From'] = formataddr(["Sray Scanner", shadow.FROM])
        msg['To'] = formataddr(["Admin", shadow.DESTINATION])

        # construct attachment
        pdf_name = pdf_path.split('/')[-1]
        with open(pdf_path, 'rb') as f:
            pdf_attach = MIMEApplication(f.read(), _subtype="pdf")
        pdf_attach.add_header('Content-Disposition','attachment',filename=str(pdf_name))
        msg.attach(pdf_attach)

        server = smtplib.SMTP(shadow.SMTP_HOST, shadow.SMTP_PORT)
        server.login(shadow.SMTP_USERNAME, shadow.SMTP_PASSWORD)
        server.sendmail(shadow.FROM, shadow.DESTINATION, msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
        ret = False
    return ret


def send_mail(title, txt):
    ret = True
    try:
        msg = EmailMessage()
        msg.set_content(txt)
        msg['Subject'] = title
        msg['From'] = formataddr(["Sray Scanner", shadow.FROM])
        msg['To'] = formataddr(["Admin", shadow.DESTINATION])

        server = smtplib.SMTP(shadow.SMTP_HOST, shadow.SMTP_PORT)
        server.login(shadow.SMTP_USERNAME, shadow.SMTP_PASSWORD)
        server.sendmail(shadow.FROM, shadow.DESTINATION, msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

if __name__ == '__main__':
    print("[*]Sending Email ...")
    ret = send_mail_with_pdf("First Report", "/home/heersin/Workspace/mine/codeql_packer/reporter/export/output_test/socat_new_result.pdf")
    if ret:
        print("[v]Success !")
    else:
        print("[x]Failed !")
