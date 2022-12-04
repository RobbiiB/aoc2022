
with open('/Users/robin/Input_day_1.txt', 'r') as file:
    string_list = file.read().split('\n')
print(string_list)
total_cal=[]
a=0
for i,val in enumerate(string_list):
    if val=='':
        total_cal.append(a)
        a=0
    else:
        a += int(val)
total_cal.sort()
print('The elf carrying the most calories carries:',total_cal[-1])
print('The top 3 elfs carrying the most calories carry:',sum([total_cal[-1],total_cal[-2],total_cal[-3]]))

