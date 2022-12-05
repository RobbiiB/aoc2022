with open('Input_day_4.txt','r') as file:
    input=file.read().split('\n')

#part1
input_a=[input[i].split(',')[0] for i in range(len(input))]
input_a_low,input_a_high = [[int(val.split('-')[i]) for _,val in enumerate(input_a)] for i in [0,1]]

input_b=[input[i].split(',')[1] for i in range(len(input))]
input_b_low,input_b_high = [[int(val.split('-')[i]) for _,val in enumerate(input_b)] for i in [0,1]]


count1=0
for val_a_l,val_a_h,val_b_l,val_b_h in zip(input_a_low,input_a_high,input_b_low,input_b_high):
    if (val_a_l-val_b_l)*(val_a_h-val_b_h)<=0:
        count1+=1
    else:
        pass
print(count1)

#part2
count2=0
for val_a_l,val_a_h,val_b_l, val_b_h in zip(input_a_low,input_a_high,input_b_low,input_b_high):
    if val_a_l<=val_b_h and val_a_h>=val_b_l:
        count2+=1
    else:
        pass
print(count2)
