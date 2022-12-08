from time import time as t
t1=t()

with open('/Users/robin/Input_day_7.txt','r') as file:
    string_list = file.read().replace('\n$ ls','').split('\n$ cd ')

class direct:
    def __init__(self,input_str,parent=''):
        self.name=input_str.split('\n')[0]
        self.parent = parent
        self.dirs=[]
        self.file_sizes=0
        self.total_size=0
        self.level = 0
        if self.name == '..':
            self.id = -1
        else:
            self.id = 1

        for _,val in enumerate(input_str.split('\n')[1:]):
            if val.split(' ')[0]=='dir':
                self.dirs.append(val.split(' ')[1])
            else:
                self.file_sizes+=int(val.split(' ')[0])



directors = [direct(value,i) for i,value in enumerate(string_list)]

a=0
for i,val in enumerate(directors):
    a+=val.id
    val.level = a
    verifyer=True
    if val.name == '..':
        j = i - 1
        while verifyer:
            if directors[j].level <= val.level:
                val.name=directors[j].name
                verifyer = False
            else:
                j+=-1

for i,val in enumerate(directors):
    val.parent = directors[i - 1].name
directors = directors[::-1]

for i,val in enumerate(directors):
    #print(val.level,i)
    verifyer=True
    val.total_size+=val.file_sizes
    if val.dirs:
        j=i-1
        while verifyer:
            if val.level>directors[j].level:
                verifyer=False
            else:
                val.total_size+=directors[j].file_sizes
                j+=-1
                pass

#part1
big_number_chan=0
for _,val in enumerate(directors):
    if val.total_size==0:
        pass
    elif val.total_size<=100000:
        big_number_chan+=val.total_size
print(big_number_chan)


#part 2
directors=directors[::-1]
total_space_needed=directors[1].total_size-40000000
free_space=[]
for i,val in enumerate(directors):
    #print(val.total_size)
    if val.total_size-total_space_needed>=0:
        free_space.append(val.total_size)
print(min(free_space))
t2=t()
print(t2-t1)

