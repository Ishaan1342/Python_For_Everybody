# # # #Representing Simple Strings using ASCII character
# # #
# # # # print(ord('H'))
# # # # print(ord('h'))
# # # import socket
# # # mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # mysock.connect(('data.pr4e.org', 80))
# # # cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# # # mysock.send(cmd)
# # #
# # # while True:
# # #     data = mysock.recv(512)
# # #     if (len(data) < 1) :
# # #         break
# # #         mystring = data.decode()
# # #         print(mystring)
# #
# #
# #
# #
# # #USING URLLIB IN PYTHON
# # # import urllib.request,urllib.parse,urllib.error
# # #
# # # fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# # # for line in fhand:
# # #     print(line.decode().strip())
# #
# #
# #
# #
# # # import urllib.request,urllib.parse,urllib.error
# # #
# # # fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# # # counts = dict()
# # # for line in fhand:
# # #     words = line.decode().split()
# # #     for word in words:
# # #         counts[word] = counts.get(word,0)+1
# # # print(counts)
# #
# #
# #
# #
# # # USING BEAUTIFUL SOUP
# # # import urllib.request,urllib.parse,urllib.error
# # # from bs4 import BeautifulSoup
# # # url = input('Enter -')
# # # html = urllib.request.urlopen(url).read()
# # # soup = BeautifulSoup(html,'html.parser')
# # #
# # # #Retrieve all of the anchor tags
# # # tags = soup('a')
# # # for tag in tags:
# # #     print(tag.get('href',None))
# #
# #
# #
# import urllib.request,urllib.parse,urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# #IGNORE SSL CERTIFICATE ERRORS
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
#
# url = input('Enter -')
# html = urllib.request.urlopen(url, context = ctx).read()
# soup = BeautifulSoup(html,'html.parser')
#
# #Retrieve all of the anchor tags
# tags = soup('img')
# for tag in tags:
#     print(tag.get('src',None))
#
#
#
#
#
#     # To run this, download the BeautifulSoup zip file
# # http://www.py4e.com/code3/bs4.zip
# # and unzip it in the same directory as this file
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
#
# #
#
#
#
#
# # print(ord("^"))
# # print(ord("*"))
# # print(ord("+"))
# # print(ord("!"))
# # print(ord("/"))


#ASSIGNMENT WEEK 4

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
#
# # Retrieve all of the anchor tags
# count = 0
# tags = soup('span')
# for tag in tags:
#     count = count + int(tag.contents[0])
#
#     print('Contents:', tag.contents[0])
#     print(count)







#ASSIGNMENT 2 WEEK 4
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input('Position - '))
repeats = int(input('Repeats - '))
count = 0


# Retrieve all of the anchor tags
while(count + 1)<= repeats :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


    tags = soup('a')
    url = str(tags[position-1].get('href',None))
    count = count + 1
    print("Retrieving:",url)
