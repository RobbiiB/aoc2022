with open('Input_day_6.txt', 'r') as file:
    datastream=file.read()

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
