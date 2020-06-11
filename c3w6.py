# # # # # # # import json
# # # # # # # data = '''{
# # # # # # # "name" : "Chuck",
# # # # # # # "phone" : {
# # # # # # # "type" : "intl",
# # # # # # # "number" : "+1 734 303 4456"
# # # # # # #
# # # # # # # },
# # # # # # # "email" : {
# # # # # # # "hide" : "yes"
# # # # # # #
# # # # # # # }
# # # # # # # }'''
# # # # # # #
# # # # # # # info = json.loads(data)
# # # # # # # print('Name:',info["name"])
# # # # # # # print('Hide:',info["email"]["hide"])
# # # # # #
# # # # # #
# # # # # # #
# # # # # # # import json
# # # # # # # input = '''[
# # # # # # # {
# # # # # # # "id" : "001",
# # # # # # # "x"  : "2",
# # # # # # # "name" : "Chuck"
# # # # # # #
# # # # # # # },
# # # # # # # {
# # # # # # # "id" : "009",
# # # # # # # "x"  : "7",
# # # # # # # "name":"chuck"
# # # # # # #
# # # # # # # }
# # # # # # #
# # # # # # # ]'''
# # # # # # # info = json.loads(input)
# # # # # # # print('User count :',len(info))
# # # # # # # for item in info:
# # # # # # #     print('Name',item['name'])
# # # # # # #     print('Id',item['id'])
# # # # # # #     print('Attribute', item['x'])
# # # # # # #
# # # # # #
# # # # # # import  json
# # # # # #
# # # # # # {
# # # # # # "status" : "OK",
# # # # # # "results": [
# # # # # # {
# # # # # # "geometry": {
# # # # # # "location_type" : "APPROXIMATE",
# # # # # # "location": {
# # # # # # "lat": 42.2808256,
# # # # # # "lng" : -83.7430378
# # # # # #
# # # # # # }
# # # # # # },
# # # # # # "address_components": [
# # # # # # {
# # # # # # "long_name": "Ann Arbor",
# # # # # # "types": [
# # # # # # "locality",
# # # # # # "political"
# # # # # # ],
# # # # # # "short_name": "Ann Arbor"
# # # # # #
# # # # # # }
# # # # # #
# # # # # # ],
# # # # # # "formatted_address": "Ann Arbor, MI, USA",
# # # # # # "types": [
# # # # # # "locality",
# # # # # # "political"
# # # # # # ]
# # # # # # }
# # # # # # ]
# # # # # # }
# # # # #
# # # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # import urllib.request, urllib.parse, urllib.error
# # # # # import json
# # # # #
# # # # # serviceurl = "http://maps.googleapis.com/maps/api/geocode/json"
# # # # #
# # # # # while True:
# # # # #     address = input('Enter Location: ')
# # # # #     if len(address) < 1: break
# # # # #
# # # # #     url = serviceurl + urllib.parse.urlencode({'address':address})
# # # # #
# # # # #
# # # # #     print('Retrieving',url)
# # # # #     uh = urllib.request.urlopen(url)
# # # # #     data = uh.read().decode()
# # # # #     print('Retrieved',len(data),'characters')
# # # # #
# # # # #     try:
# # # # #         js = json.loads(data)
# # # # #     except:
# # # # #         js = None
# # # # #
# # # # #     if not js or 'status' not in js or js['status']!='OK':
# # # # #         print('===Failure to Retrieve===')
# # # # #         print(data)
# # # # #         continue
# # # # #     lat = js["results"][0]["geometry"]["location"]["lat"]
# # # # #     lng = js["results"][0]["geometry"]["location"]["lng"]
# # # # #     print('lat',lat,'lng',lng)
# # # # #     location = js['results'][0]['formatted_address']
# # # # #     print(location)
# # # #
# # # #
# # # #
# # # #
# # # # import urllib.request, urllib.parse, urllib.error
# # # # import json
# # # # import ssl
# # # #
# # # # api_key = False
# # # # # If you have a Google Places API key, enter it here
# # # # # api_key = 'AIzaSy___IDByT70'
# # # # # https://developers.google.com/maps/documentation/geocoding/intro
# # # #
# # # # if api_key is False:
# # # #     api_key = 42
# # # #     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# # # # else :
# # # #     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# # # #
# # # # # Ignore SSL certificate errors
# # # # ctx = ssl.create_default_context()
# # # # ctx.check_hostname = False
# # # # ctx.verify_mode = ssl.CERT_NONE
# # # #
# # # # while True:
# # # #     address = input('Enter location: ')
# # # #     if len(address) < 1: break
# # # #
# # # #     parms = dict()
# # # #     parms['address'] = address
# # # #     if api_key is not False: parms['key'] = api_key
# # # #     url = serviceurl + urllib.parse.urlencode(parms)
# # # #
# # # #     print('Retrieving', url)
# # # #     uh = urllib.request.urlopen(url, context=ctx)
# # # #     data = uh.read().decode()
# # # #     print('Retrieved', len(data), 'characters')
# # # #
# # # #     try:
# # # #         js = json.loads(data)
# # # #     except:
# # # #         js = None
# # # #
# # # #     if not js or 'status' not in js or js['status'] != 'OK':
# # # #         print('==== Failure To Retrieve ====')
# # # #         print(data)
# # # #         continue
# # # #
# # # #     print(json.dumps(js, indent=4))
# # # #
# # # #     lat = js['results'][0]['geometry']['location']['lat']
# # # #     lng = js['results'][0]['geometry']['location']['lng']
# # # #     print('lat', lat, 'lng', lng)
# # # #     location = js['results'][0]['formatted_address']
# # # #     print(location)
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # #TWITTER API
# # # #
# # #
# # #
# # # import urllib.request, urllib.parse, urllib.error
# # # import twurl
# # # import ssl
# # #
# # # # https://apps.twitter.com/
# # # # Create App and get the four strings, put them in hidden.py
# # #
# # # TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
# # #
# # # # Ignore SSL certificate errors
# # # ctx = ssl.create_default_context()
# # # ctx.check_hostname = False
# # # ctx.verify_mode = ssl.CERT_NONE
# # #
# # # while True:
# # #     print('')
# # #     acct = input('Enter Twitter Account:')
# # #     if (len(acct) < 1): break
# # #     url = twurl.augment(TWITTER_URL,
# # #                         {'screen_name': acct, 'count': '2'})
# # #     print('Retrieving', url)
# # #     connection = urllib.request.urlopen(url, context=ctx)
# # #     data = connection.read().decode()
# # #     print(data[:250])
# # #     headers = dict(connection.getheaders())
# # #     # print headers
# # #     print('Remaining', headers['x-rate-limit-remaining'])
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # ASSIGNMENT 1
# # import urllib.request, urllib.parse, urllib.error
# # import json
# #
# # url = input("enter URL:")
# #
# # print('Retrieving', url)
# # uh = urllib.request.urlopen(url)
# # data = uh.read()
# # print('Retrieved', len(data), 'characters')
# #
# #     # Converts the json to a dictionary
# # tree = json.loads(data)
# #
# # iterations = 0
# # total = 0
# #
# #     #This tree has 2 nodes in the first level: "note" and "comments"
# #     #This loop is only for the 'comments'
# # for item in tree['comments']:
# #
# #       iterations = iterations + 1
# #       total = total + int(item['count'])
# #
# # print("Count:",iterations)
# # print("Sum:",total)
#
#
#
# # ASS 2
#
#
# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl
#
# # api_key = False
# # If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro
#
# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# address = input("Enter Location:")
#
# url = serviceurl+ urllib.parse.urlencode({'address':address})
# print("Retrieving",url)
# uh = urllib.request.urlopen(url)
# data = uh.read().decode()
# print('Retrieved',len(data),'characters')
# try:
#     js = json.loads(data)
#     print("Place id",js["results"][0]["place_id"])
# except:
#     js = None
#     print('===Failue To Retrieve===')
#
#
#
# #
# # import urllib.request, urllib.parse, urllib.error
# # import json
# #
# # serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# #
# # address = input('Enter location: ')
# #     #address = "South Federal University"
# #     #address = "University of Chicago"
# #
# # url = serviceurl + urllib.parse.urlencode({'address': address})
# #
# # print('Retrieving', url)
# # uh = urllib.request.urlopen(url)
# # data = uh.read().decode()
# # print('Retrieved', len(data), 'characters')
# #
# # try:
# #     js = json.loads(data)
# #     print("Place id",js["results"][0]["place_id"])
# #
# # except:
# #
# #     js = None
# #     print('==== Failure To Retrieve ====')




import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
        print("Place id",js["results"][0]["place_id"])
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
