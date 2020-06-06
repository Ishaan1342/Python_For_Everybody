# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)

# RE IS REGULAR EXPRESSION LIBRARY
# import re
# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line) :
#         print(line)

# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From:') >= 0:
#         print(line)


# RE IS REGULAR EXPRESSION LIBRARY
# import re
# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:', line) :
#         print(line)

# import re
# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X.*:', line) :
#         print(line)

# import re
# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X-\S+:', line) :
#         print(line)

# import re
# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#     line= re.findall('[0-9]+',line) #finds all the nos in text
#     print(line)


# import re
# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#     line= re.findall('[AEIOU]+',line) #finds all the uppercase vowels in text
#     print(line)


#GREEDY MATCHING

# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+:',x)
# print(y)



#NON-GREEDY MATCHING
# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+?:',x)
# print(y)



# import re
# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#
#     line = re.findall('\S+@\S+',line)
#     print(line)



# import re
# hand = open('text.txt')
# for line in hand:
#     line = line.rstrip()
#
#     line = re.findall('^From (\S+@\S+)',line)
#     print(line)







# data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:312:83 2008"
# atpos = data.find('@')
# print(atpos)
# sppos = data.find(' ',atpos)
# print(sppos)
# host = data[atpos+1 : sppos]
# print(host)

# import re
# data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:312:83 2008"
# y  = re.findall('@([^ ]*)',data) #those square brackets indicate non-blank char and ^ in brackets means everything but space
# print(y)



# import re
# data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:312:83 2008"
# y  = re.findall('^From .*@([^ ]*)',data)
# print(y)
#
#




# import re
# hand = open('text.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
#     if len(stuff) != 1 : continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Maximum:',max(numlist))





# import re
# x  = 'WE just received $10.00 for cookies'
# y = re.findall('\$[0-9.]+',x)
# print(y)


# CODE BELOW NOT WORKING

# import re
# hand = open('text1.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('[0-9]+',line)
#     if len(stuff) != 1 : continue
#     numlist = numlist.append(int(stuff))
# print(sum(numlist))





# import re
#
# hand = open("text1.txt")
# x=list()
# for line in hand:
#    y = re.findall('[0-9]+',line)
#    x = x+y
#
# sum=0
# for z in x:
#    sum = sum + int(z)
#
# print(sum)





import re
print(sum([int(i) for i in re.findall('[0-9]+',open("text1.txt").read())]))
