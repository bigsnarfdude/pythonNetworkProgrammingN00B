
import smtpd
import smtplib
import asyncore
import dns.resolver # pip install dnspython

PORT = 8025
HOST = ""
# code from dnspython examples
def get_mx_record(domain):
    records = dns.resolver.query(domain, 'MX')
    return str(records[0].exchange)

# code from http://www.doughellmann.com/PyMOTW/smtpd/
class SimpleMailServer(smtpd.SMTPServer):
                
    def process_message(self, peer, mailfrom, rcpttos, data):
        for rcptto in rcpttos:
            domain = rcptto.split('@')[1]
            mx = get_mx_record(domain)
            server = smtplib.SMTP(mx, 25)
            try:
                server.sendmail(mailfrom, rcptto, data)
            finally:
                server.quit()

server = SimpleMailServer((HOST, PORT), None)
print 'Server listening on port {0}'.format(PORT)
asyncore.loop()
