#!/bin/python
"""
pyphishing.py

Purpose: Python-powered automatic phishing email program.
This program is based on PyPhisher by sneakerhax (https://github.com/sneakerhax/PyPhisher).

Author: Cody Jackson

Date: 2/20/2018
########################
Version 0.1
    Initial build
"""
import argparse
import smtplib
import re

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def argument_parser():
    """Allow user to specify target host and port."""
    parser = argparse.ArgumentParser(description="Takes a pre-crafted HTML email, automatically replaces the links with"
                                                 "the desired address, and sends the email.")
    parser.add_argument("server", help="SMTP server that will send the email")
    parser.add_argument("port", help="SMTP server port number")
    parser.add_argument("username", help="Username for the SMTP server")
    parser.add_argument("password", help="Password for the SMTP server")
    parser.add_argument("email", help="Pre-crafted email location")
    parser.add_argument("url", help="URL that will replace all links in the email")
    parser.add_argument("subject", help="Email subject")
    parser.add_argument("sender", help="Email sender")
    parser.add_argument("sendto", help="Target email address")
    parser.add_argument("--tls", default=False, help="Attempt to use SSL/TLS")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary

    return var_args


def open_email_file(email_file):
    """Open the HTML-formatted email file."""
    with open(email_file, 'r') as open_email:
        email_html = open_email.read()

    return email_html


def replace_links(url, message):
    """Replace the visible email links with the desired URL."""
    html_regex = re.compile(r'href=[\'"]?([^\'" >]+)')
    html_output = html_regex.sub("href=\"{}".format(url), message)

    return html_output


def mime_message(email_subj, send_to, send_from, html_email):
    """Format the email message"""
    msg = MIMEMultipart('alternative')
    msg['To'] = send_to
    msg['From'] = send_from
    msg['Subject'] = email_subj
    message = MIMEText(html_email, 'html')
    msg.attach(message)

    return msg.as_string()


def send_email(server, port, username, password, send_from, send_to, message, tls):
    """Send the email to the email server."""
    print("[+] Attempting to connect to server")
    start_server = smtplib.SMTP(server, port)
    if tls:
        print("[+] Attempting to use STARTTLS")
        start_server.starttls()
    print("[+] Attempting to say ehlo")
    start_server.login(username, password)
    print("[+] Attempting to send mail")
    start_server.sendmail(send_from, send_to, message)
    print("[+] Done...")
    start_server.quit()


def go_phishing(server, port, username, password, email_loc, url_replace, subj, send_from, send_to, tls):
    """Tie everything together."""
    html_email = open_email_file(email_loc)
    html_output = replace_links(url_replace, html_email)
    message = mime_message(subj, send_to, send_from, html_output)
    send_email(server, port, username, password, sender, send_to, message, tls)


if __name__ == '__main__':
    try:
        user_args = argument_parser()
        email_server = user_args["server"]
        smtp_port = user_args["port"]
        login = user_args["username"]
        pword = user_args["password"]
        email_path = user_args["email"]
        new_url = user_args["url"]
        email_subject = user_args["subject"]
        sender = user_args["sender"]
        receiver = user_args["sendto"]
        use_tls = user_args["tls"]

        go_phishing(email_server, smtp_port, login, pword, email_path, new_url, email_subject, sender, receiver, use_tls)
    except AttributeError:
        print("Error. Please provide the command-line arguments before running.")
