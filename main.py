with open('/Users/robin/Input_day_6.txt', 'r') as file:
    datastream=file.read()
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#part 1
z=4
for i in range(len(datastream)-3):
    a=set(datastream[i:i+z])
    b=datastream[i:i+z]
    if len(a)==len(b):
        print(i+z)
        break

#part 2
z=14
for i in range(len(datastream)-3):
    a=set(datastream[i:i+z])
    b=datastream[i:i+z]
    if len(a)==len(b):
        print(i+z)
        break