math = int(input("math: "))
if math <0 or math > 100:
    print("invalid")
English = int(input("english: "))
if English <0 or English > 100:
    print("invalid")
kiswahili = int(input("kiswahili: "))
if kiswahili <0 or kiswahili > 100:
    print("invalid")
biology = int(input("biology: "))
if biology <0 or biology > 100:
    print("invalid")
geograph = int(input("geograph: "))
if geograph <0 or geograph > 100:
    print("invalid")

if sum/5 >= 71 and sum/5<=100:
    print("A")
elif sum/5 >=61 and sum/5<=70:
    print("B")
elif sum/5 >= 51 and sum/5<=60:
    print("C")
elif sum/5 >= 40 and sum/5<=50:
    print("D")
elif sum/5 >=0 and sum/5<=39:
    print("E")
else:
    print("invalid input")
