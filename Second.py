# # # # # # # # # # # # # # # # # # # # # # # # # fruit = "pineapple"
# # # # # # # # # # # # # # # # # # # # # # # # # x = len(fruit)
# # # # # # # # # # # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # # # # # # # # # # # # index = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # while index<len(fruit) :
# # # # # # # # # # # # # # # # # # # # # # # # # #     letter = fruit[index]
# # # # # # # # # # # # # # # # # # # # # # # # # #     print(index+1,letter)
# # # # # # # # # # # # # # # # # # # # # # # # # #     index = index + 1
# # # # # # # # # # # # # # # # # # # # # # # # # for letter in fruit:
# # # # # # # # # # # # # # # # # # # # # # # # #     print(letter)
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # word = "acknowledgementaaaaaa"
# # # # # # # # # # # # # # # # # # # # # # # # count = 0
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # for letter in word:
# # # # # # # # # # # # # # # # # # # # # # # #     if letter == "a":
# # # # # # # # # # # # # # # # # # # # # # # #         count = count+1
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # print(count)
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # s = "Monty Python"
# # # # # # # # # # # # # # # # # # # # # # # print(s[0:4])
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # x = '40'
# # # # # # # # # # # # # # # # # # # # # # # # y = int(x) + 2
# # # # # # # # # # # # # # # # # # # # # # # # print(y)
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # x = 'From marquard@uct.ac.za'
# # # # # # # # # # # # # # # # # # # # # # # print(x[8])
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # for letter in 'banana' :
# # # # # # # # # # # # # # # # # # # # # #     print(letter)
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #     data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# # # # # # # # # # # # # # # # # # # # # # pos = data.find('.')
# # # # # # # # # # # # # # # # # # # # # # print(data[pos:pos+3])
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # QUESTION: 6.5 Write code using find() and string slicing (see section 6.10) to extract the number
# # # # # # # # # # # # # # # # # # # # # # # at the end of the line below.
# # # # # # # # # # # # # # # # # # # # # # # Convert the extracted value to a floating point number and print it out.
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #ANSWER
# # # # # # # # # # # # # # # # # # # # # # text = "X-DSPAM-Confidence:    0.8475";
# # # # # # # # # # # # # # # # # # # # # # pos = text.find("0")
# # # # # # # # # # # # # # # # # # # # # # slice = text[pos:pos+10]
# # # # # # # # # # # # # # # # # # # # # # finaltext = float(slice)
# # # # # # # # # # # # # # # # # # # # # # print(finaltext)
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # stuff = 'hello\nworld'
# # # # # # # # # # # # # # # # # # # # # stuff
# # # # # # # # # # # # # # # # # # # # # print(stuff)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # file = open("text.txt")
# # # # # # # # # # # # # # # # # # # # # for cheese in file:
# # # # # # # # # # # # # # # # # # # # #     print(cheese)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # yo = file.read()
# # # # # # # # # # # # # # # # # # # # # print(len(yo))
# # # # # # # # # # # # # # # # # # # # # print(yo[:20])
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # file = open("text.txt")
# # # # # # # # # # # # # # # # # # # # # for line in file:
# # # # # # # # # # # # # # # # # # # # #     line = line.rstrip()
# # # # # # # # # # # # # # # # # # # # #     # if line.startswith('So'):
# # # # # # # # # # # # # # # # # # # # #     if not line.startswith('So'):
# # # # # # # # # # # # # # # # # # # # #         continue
# # # # # # # # # # # # # # # # # # # # #     print(line)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # fname = input('enter the filename: ' )
# # # # # # # # # # # # # # # # # # # # # fhand = open(fname)
# # # # # # # # # # # # # # # # # # # # # count = 0
# # # # # # # # # # # # # # # # # # # # # for line in fhand:
# # # # # # # # # # # # # # # # # # # # #     if line.startswith('Subject:'):
# # # # # # # # # # # # # # # # # # # # #         count = count + 1
# # # # # # # # # # # # # # # # # # # # #         print("there were", count,'subject line in ', fname)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # fname = input('enter the filename: ' )
# # # # # # # # # # # # # # # # # # # # try:
# # # # # # # # # # # # # # # # # # # #     fhand = open(fname)
# # # # # # # # # # # # # # # # # # # # except:
# # # # # # # # # # # # # # # # # # # #     print("File cannot be opened:",fname)
# # # # # # # # # # # # # # # # # # # #     quit()
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # count = 0
# # # # # # # # # # # # # # # # # # # # for line in fhand:
# # # # # # # # # # # # # # # # # # # #     if line.startswith('Subject:'):
# # # # # # # # # # # # # # # # # # # #         count = count + 1
# # # # # # # # # # # # # # # # # # # #         print("there were", count,'subject line in ', fname)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # friends = ["Ross", "Monica", "Chandler", "phoebe","joey", "rachel"]
# # # # # # # # # # # # # # # # # # # for friend in friends:
# # # # # # # # # # # # # # # # # # #     print("I'll be there for you",friend)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # friends = ["Ross", "Monica", "Chandler", "phoebe","joey", "rachel"]
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # for i in range(len(friends)):
# # # # # # # # # # # # # # # # # #     friend = friends[i]
# # # # # # # # # # # # # # # # # #     print("I'll be there for you",friend)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # //Concatenating Lists Using +
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # A = [1,2,3,2,3,2,32,3]
# # # # # # # # # # # # # # # # # B = [1,2,3,32,3,23,23,2,32,32,3,2,32,3,2,3,43,546]
# # # # # # # # # # # # # # # # # C = A + B
# # # # # # # # # # # # # # # # # print(len(C))
# # # # # # # # # # # # # # # # # print(A[1:4])
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # x = list()
# # # # # # # # # # # # # # # # type(x)
# # # # # # # # # # # # # # # # print(dir(x))
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # stuff = list()
# # # # # # # # # # # # # # # stuff.append('chocolate')
# # # # # # # # # # # # # # # print(stuff)
# # # # # # # # # # # # # # # stuff.append(192012)
# # # # # # # # # # # # # # # print(stuff)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # Stuff = [1,2,3,4,3,2,3,43,45,4,4]
# # # # # # # # # # # # # # print(3 in Stuff)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # Stuff = [1,2,3,4,3,2,3,43,45,4,4]
# # # # # # # # # # # # # Stuff.sort()
# # # # # # # # # # # # # print(Stuff)
# # # # # # # # # # # # # print(max(Stuff))
# # # # # # # # # # # # # print(min(Stuff))
# # # # # # # # # # # # # print(float(sum(Stuff)))
# # # # # # # # # # # # # print(sum(Stuff)/len(Stuff))
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # numlist = list()
# # # # # # # # # # # # while True:
# # # # # # # # # # # #
# # # # # # # # # # # #     inp = input("enter a number:")
# # # # # # # # # # # #     if inp == "done": break
# # # # # # # # # # # #     value = float(inp)
# # # # # # # # # # # #     numlist.append(value)
# # # # # # # # # # # #
# # # # # # # # # # # # average = sum(numlist)/len(numlist)
# # # # # # # # # # # # print(average)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # total =0
# # # # # # # # # # # count =0
# # # # # # # # # # # while True:
# # # # # # # # # # #     inp = input("entera a number:")
# # # # # # # # # # #     if inp == "done" : break
# # # # # # # # # # #     value = float(inp)
# # # # # # # # # # #     total += value
# # # # # # # # # # #     count += 1
# # # # # # # # # # # average = total/count
# # # # # # # # # # # print("average",average)
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # abc = "With my blessings you can do anything in life"
# # # # # # # # # # stuff = abc.split()
# # # # # # # # # # print(stuff)
# # # # # # # # # # print(len(stuff))
# # # # # # # # # # print(stuff[0])
# # # # # # # # # #
# # # # # # # # # # for w in stuff:
# # # # # # # # # #     print(w)
# # # # # # # # # #
# # # # # # # # #
# # # # # # # # # x = split()
# # # # # # # # # type(x)
# # # # # # # # # print(dir(x))
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # line = "A lot       of spaces"
# # # # # # # # etc = line.split()
# # # # # # # # print(etc)
# # # # # # # #
# # # # # # # #
# # # # # # # line = "first;second;third;lmao"
# # # # # # # thing = line.split()
# # # # # # # print(thing)
# # # # # # # print(len(thing))
# # # # # # # thing = line.split(";")
# # # # # # # print(thing)
# # # # # # # print(len(thing))
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # line = 'From gillishaan@gmail.com'
# # # # # # # words = line.split()
# # # # # # # print(words)
# # # # # #
# # # # # #
# # # # # # fhand = open('Text.txt')
# # # # # # for line in fhand:
# # # # # #     line = line.rstrip()
# # # # # #     if not line.startswith('From ') : continue
# # # # # #     words = line.split()
# # # # # #     print(words[2])
# # # # # #
# # # # # #
# # # # # #     print(words[1])
# # # # # #     email = words[1]
# # # # # #     pieces = email.split("@")
# # # # # #     print(pieces)
# # # # # #     final = pieces[1]
# # # # # #     lastpiece = final.split(".")
# # # # # #     print(lastpiece)
# # # # #
# # # # # # CHAPTER 8 ASSIGMENT 1&2
# # # # #
# # # # # # fname = input("Enter file name: ")
# # # # # # fh = open(fname)
# # # # # # lst = list()
# # # # # # for line in fh:
# # # # # #     word = line.rstrip().split()
# # # # # #     for element in word:
# # # # # #         if element in lst:
# # # # # #             continue
# # # # # #         else:
# # # # # #             lst.append(element)
# # # # # # lst.sort()
# # # # # # print(lst)
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # fname = input("Enter file name: ")
# # # # # if len(fname) < 1 : fname = "mbox-short.txt"
# # # # #
# # # # #
# # # # # fh = open(fname)
# # # # # lst = list()
# # # # # count = 0
# # # # # for line in fh:
# # # # #     if not line.startswith("From:"): continue
# # # # #     count += 1
# # # # #     email = line.split()
# # # # #     print(email[1])
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # print("There were", count, "lines in the file with From as the first word")
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # # DICTIONAIRY
# # # #
# # # # # purse = dict()
# # # # # purse['money'] = 21
# # # # # purse['candy'] = 2
# # # # # purse['tissue'] = 2
# # # # # print(purse)
# # # # # purse['candy'] = purse['candy'] +12
# # # # # print(purse)
# # # # #
# # # # # jjj = {'duck':1,'yuck':2,'luck':100}
# # # # # print(jjj)
# # # # #
# # # # #
# # # # #
# # # # # counts = dict()
# # # # # names = ['csev','sdfdsf','sdfdsfsdf','sgsgsgsg']
# # # # # for name in names:
# # # # #     if name not in counts:
# # # # #         counts[name]=1
# # # # #     else :
# # # # #         counts[name] = counts[name] + 1
# # # # #     print(counts)
# # # #
# # # #
# # # #
# # # # counts = dict()
# # # # names = ['csev','sdfdsf','sdfdsfsdf','sgsgsgsg','csev']
# # # #
# # # # for name in names:
# # # #     counts[name]=counts.get(name,0)+1
# # # # print(counts)
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # counts = dict()
# # # print('enter a line of text:')
# # # line = input('')
# # # words = line.split()
# # # print('words',words)
# # # print('counting...')
# # # for word in words:
# # #     counts[word]= counts.get(word,0) + 1
# # # print('Counts',counts)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # counts = {'chuck':1,'duck':2,'jeff':12}
# # # # for key in counts:
# # # #     print(key,counts[key])
# # #
# # # # print(list(counts)
# # # print(list(counts))
# # # print(counts.keys())
# # # print(counts.values())
# # # print(counts.items())
# # #
# #
# #
# #
# # # jjj = {'chuck':1,'duck':2,'jeff':12}
# # # for aaa,bbb in jjj.items():
# # #     print(aaa,bbb)
# #
# #
# #
# #
# #
# # name = raw_input("Enter file:")
# # if len(name) < 1 : name = "mbox-short.txt"
# # handle = open(name)
# #
# # lst = list()
# # for line in handle:
# #     line = line.strip()
# #     if line.startswith("From:"):
# #         words = line.split()
# #         email = words[1]
# #         lst.append(email)
# #
# # dct = dict()
# # for email in lst:
# #     dct[email] = dct.get(email,0)+1
# #
# # bigcount = None
# # email_address = None
# # for key,value in dct.items():
# #     if bigcount is None or value > bigcount:
# #         bigcount = value
# #         email_address = key
# #
# # print(email_address, bigcount)
#
#
#
#
# # TUPLE
# # t = tuple()
# # print(dir(t))
#
# # (x,y) = (23,'fred')
# # print(y)
# # (a,b) = (878,43)
# # print(a)
# #
# # #tuples are compareable
# # print((0,1,2)<(5,1,3))
#
#
# # d = {'a':10,'b':12,'c':2}
# # print(d.items())
# # print(sorted(d.items()))
#
#
# d = {'a':10,'b':12,'c':2}
# for k,v in sorted(d.items()):
#     print(k,v)



# c = {'a':10,'b':12,'c':2}
# tmp = list()
# for k,v in c.items() :
#     tmp.append((v,k))
# print(tmp)
# tmp = sorted(tmp,reverse=True)
# print(tmp)


# fhand = open('text.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0)
# lst = list()
# for key,val in counts.items():
#     newtup = (val,key)
#     lst.append(newtup)
# lst = sorted(lst,reverse = True)
# for val,key in lst[:10] :
#     print(key,val)




# LIST COMPREHENSION
# c = {'a':10,'b':12,'c':2}
# print(sorted([ (v,k) for k,v in c.items()]))







# ASSIGNMENT


name = raw_input("Enter file:")
if len(name) < 1 : name = "text.txt"
handle = open(name)

hcount = dict()                                     #create empty dictionary
hlst = []                                           #create empty list

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       #Select lines with 'From'
        hr = words[5].split(':')                    #Select hour (5th index) and split string with colon
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1    #increase count for each hour
    else:
        continue

for k,v in hcount.items():                           #k = hour, v = count
    hlst.append((k,v))                               #append tuples to list

hlst.sort()                                         #sort list by hour
for k,v in hlst:                                    #loop through list of tuples
    print k,v                                       #print counts sorted by hour
