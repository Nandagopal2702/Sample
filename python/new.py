# d = {"a":10, "z":20, "k":30, "d":40}
# d1 = sorted(d.keys())

# for i in d1:
#     print(i,d[i])

# l1 = [10, 20, 30, 40, 50, 60, 70]
# n = 3


# for i in range(n):
#     a = l1.pop()
#     l1.insert(0,a)

# print(l1)


# l = len(l1)
# a = l - n
# LS = l1[:a][::-1]
# RS = l1[a:][::-1]

# res = (LS + RS)[::-1]
# print(res)

# def count_alphabets(s):
#     result = ""
#     count = {}
#     for c in s:
#         if c.isalpha():
#             if c in count:
#                 count[c] += 1
#             else:
#                 count[c] = 1
#     for c in s:
#         if c.isalpha() and c in count:
#             result += c + str(count[c])
#             del count[c]
#     return result

# print(count_alphabets("abb24ccc8ddbbca1"))

# input = "1211"
# a = ""
# c = 0
# for i in input:
#     if i not in a:
#         a += i
#         c += int(i)
# print(c)

# S = input()
# k = input()

# SI = S.find(k)
# if SI == -1:
#     print(-1, -1)
# else:
#     EI = SI + len(k) - 1
#     print(SI, EI)
#     while True:
#         SI = S.find(k, SI + 1)
#         if SI == -1:
#             break
#         EI = SI + len(k) - 1
#         print(SI, EI)

# def valid_par(s):
#     l = []
#     for i in s:
#         if i in "({[":
#             l.insert(0,1)
#         else:
#             if l:
#                 if l[0]+1 in ["()","[]","{}"]:
#                     l.pop(0)
#                 else:
#                     return False
#             else:
#                 return False
#     if not l:
#         return True
#     else:
#         return False
    
# print(valid_par("()"))

# def isValid(s):
#     a = dict(('()', '[]', '{}'))
#     l = []
#     for i in s:
#         if i in '([{':
#             l.append(i)
#         elif len(l) == 0 or i != a[l.pop()]:
#             return False
#         else:
#             return len(l) == 0

# print(isValid("()"))


# import re

# data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
# for item in data:
#     result = re.sub(r'\([^)]*\)', '', item).strip()
#     print(result)


""" Write a program to send a mail notification to customers regarding the arrival of goods
    on a daily basis. The admin email has a separate domain email address owned by your
    company.Do not forget to add cc candidates in customer's mail."""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


email_from = 'moinalikhandevopser@gmail.com'
email_password = 'unhdjbkotyfzcbmx'
email_subject = 'Daily Goods Arrival Notification'
email_body = 'Hello,\n\nThis is to inform you that new goods have arrived in our store today.\n\nThank you for your continued patronage.\n\nBest regards,\nSender'

recipients = ['nandugopaldevji@gmail.com']
cc_recipients = ['rsrinivas@msystechnologies.com','meghumeghu3@gmail.com']


msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = ', '.join(recipients)
msg['Cc'] = ', '.join(cc_recipients)
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_from, email_password)

server.sendmail(email_from, recipients + cc_recipients, msg.as_string())
print('Email notification sent successfully!')

server.quit()