# print("Hello from atom")
# print("abc" + "123")
# hrs = input("Enter Hours:")
# rate = input("Enter Rate")
# pay = float(hrs)*float(rate)
#
# print("Pay:",pay)



#
# hrs = input("Enter Hours:")
# h = float(hrs)
# hrate = input("Rate:")
# r = float(hrate)
#
# if h<40 :
#     print(h*r)
# elif h>40 :
#     print(h*r + (h-40)*r*1.5)


#LAST ASSIGNMENT COURSE 1
largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break;
        n = int(num)
        largest = n if largest < n or largest == None else largest
        smallest = n if smallest > n or smallest == None else smallest
    except:
            print ("Invalid input")

print ("Maximum is", largest)
print ("Minimum is", smallest)
