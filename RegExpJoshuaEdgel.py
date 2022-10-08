import re
#Joshua Edgel
#10/18/2021
search_file = 'warpeace.txt'

phone = re.compile("([1]?[(-]?[0-9]{3}[)\s-]+[0-9]{3}[-]+[0-9]{4})") # finds 12

accountNum = re.compile("([A-Z]{2}-[0-9]{3}-[A-Z][0-9]{5})") # finding none?

sSN = re.compile("([0-9]{3}-[0-9]{2}-[0-9]{4})") # finds 4

date11 = re.compile("((?:(?:0[13578]|10|12)[\/-](?:0[1-9]|1[0-9]|2[0-9]|3[01])[\/-][0-9]{4}|(?:0[469]|11)[\/-](?:0[0-9]|1[0-9]|2[0-9]|30)[\/-][0-9]{4})|(?:02)[\/-](?:0[1-9]|1[0-9]|2[0-9])[\/-][0-9]{4})") # finds 16
date1 = re.compile("([0-9]{2}/[0-9]{2}/[0-9]{4})") # basic dates search i was using for testing. 

total = 0

#the code is pretty ugly looking. I just copy/pasted the same search through the whole book. Definetly not ideal or the fastest. It gets the job done though. 
#searches phone numbers
with open(search_file, 'r') as sf:
    b = False
    i = 0
    reg_ex = re.compile("([1]?[(-]?[0-9]{3}[)\s-]+[0-9]{3}[-]+[0-9]{4})")
    for line in sf:
        m = re.findall(reg_ex, line)
        if m:
            print("\nFound it!")
            print(line.strip())
            for item in m:
                print(item)
                i += 1
                total += 1
            b = True
    if not b:
        print("Didn't find it.")
    else:
        print(f"Found {i} phone number instances.")
#searches account numbers
with open(search_file, 'r') as sf:
    b = False
    ii = 0
    reg_ex = re.compile("([A-Z]{2}-[0-9]{3}-[A-Z][0-9]{5})")
    for line in sf:
        m = re.findall(reg_ex, line)
        if m:
            print("\nFound it!")
            print(line.strip())
            for item in m:
                print(item)
                ii += 1
                total += 1
            b = True
    if not b:
        print("Didn't find it.")
    else:
        print(f"Found {ii} account number instances.")
#searches SSN
with open(search_file, 'r') as sf:
    b = False
    iii = 0
    reg_ex = re.compile("([0-9]{3}-[0-9]{2}-[0-9]{4})")
    for line in sf:
        m = re.findall(reg_ex, line)
        if m:
            print("\nFound it!")
            print(line.strip())
            for item in m:
                print(item)
                iii += 1
                total += 1
            b = True
    if not b:
        print("Didn't find it.")
    else:
        print(f"Found {iii} SSN instances.")
#searches dates
with open(search_file, 'r') as sf:
    b = False
    iiii = 0
    reg_ex = re.compile("((?:0[13578]|10|12)[\/-](?:0[1-9]|1[0-9]|2[0-9]|3[01])[\/-]([0-9]{2}){1,2})|((?:0[469]|11)[\/-](?:0[0-9]|1[0-9]|2[0-9]|30)[\/-]([0-9]{2}){1,2})|((?:02)[\/-](?:0[1-9]|1[0-9]|2[0-9])[\/-]([0-9]{2}){1,2})")
    for line in sf:
        m = re.findall(reg_ex, line)
        if m:
            print("\nFound it!")
            print(line.strip())
            for item in m:
                print(item)
                iiii += 1
                total += 1
            b = True
    if not b:
        print("Didn't find it.")
    else:
        print(f"Found {iiii} date instances.")
#prints results is a decently readable format.
print(f"")
print(f"Total Summary")
print(f"Found {i} phone number instances.")
print(f"Found {ii} account number instances.")
print(f"Found {iii} SSN instances.")
print(f"Found {iiii} date instances.")
print(f"Found {total} total instances.")