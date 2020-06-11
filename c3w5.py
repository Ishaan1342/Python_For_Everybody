# # <!-- <receipe name = "bread" prep_time = "5 mins" cook_time = "3 hours">
# #   <title>Basic bread</title>
# #   <ingredient amount="8" unit="DL">Flour</ingredient>
# #   <ingredient amount = "10" unit ="grams">Yeast</ingredient>
# #   <instructions>
# #     <step>Mix all ingredients together.</step>
# #     <step>Knead thoroughly.</step>
# #     <step>Cover with a cloth.</step>
# #     <step>Knead again.</step>
# #     <step>Place in a bread baking.</step>
# #     <step>Another step for baking.</step>
# #   </instructions>
# # </receipe>
# #
# #
# #
# #
# #
# # <xs:element name="person">
# #   <xs:complexType>
# #     <xs:sequence>
# #       <xs:element name="full_name" type = "xs:string"
# #         minOccurs="1" maxOccurs ="1"/>
# #         <xs:element name = "child_name" type="xs:string"
# #           minOccurs="0" maxOccurs ="10"/>
# #     </xs:sequence>
# #   </xs:complexType>
# # </xs:element> -->
# #
# #
# #
# # import xml.etree.ElementTree as ET
# # data = '''<person>
# # <name>Barry</name>
# # <phone type="intl">
# # +1 7343034456
# # </phone>
# # <email hide = "yes" />
# # </person>'''
# #
# # tree = ET.fromstring(data)
# # print('Name:',tree.find('name').text)
# # print('Attr:',tree.find('email').get('hide'))
#
#
#
#
#
# import xml.etree.ElementTree as ET
# input = '''<stuff>
# <users>
# <user x = "2">
# <id>001</id>
# <name>chuck</name>
# </user>
# <user x ="7">
# <id>009</id>
# <name>Brent</name>
# </user>
# </users>
# </stuff>'''
#
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:',len(lst))
# for item in lst:
#     print('Name',item.find('name').text)
#     print('Id',item.find('id').text)
#     print('Attribute',item.get("x"))



#ASSIGNMENT

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_615328.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

    #Converts the xml to a string
tree = ET.fromstring(data)

    #filters by .//count same as comments/comment/count
results = tree.findall('.//count')
iterations = 0
total = 0

    #Loop all items in the list
for item in results:

    iterations = iterations + 1

        #Gets the text value from the tag count
    total = total + int(item.text)

print("Count:",iterations)
print("Sum:",total)
