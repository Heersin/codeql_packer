import argparse
import generator
import mailer.mail
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True, help='project name')
    parser.add_argument(
        '-s', '--sarif', 
        action='append', 
        help='read sarif format file, can set multiple times')
    parser.add_argument(
        '-j', '--json',
        help='read from remote json server'
    )
    parser.add_argument(
        '-c', '--csv',
        action='append',
        help='read csv format file, can set multiple times')
    parser.add_argument(
        '-m', '--mail',
        action='store_true',
        help='mail this report to your configed mailbox'
    )
    
    args = parser.parse_args()
    pdf_path = generator.generate(args)
    title = f"PROJECT*[{args.name}] Scan Report"

    if (args.mail):
        print("[*]Send Report to configed mailbox ...")
        ret = mailer.mail.send_mail_with_pdf(title ,pdf_path)
        if ret:
            print("[v]Success !")
        else:
            print("[x]Failed !")