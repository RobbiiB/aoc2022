with open('Input_day_5.txt','r') as file:
    start = file.read(323)
    instruct = file.read().split('\n')[2:]

start_stack = start[1:-35].split('\n')
start_stack = start_stack[::-1]


class stack:
    def __init__(self,num):
        self.num=num
        self.collum=4*int(num)-3
        self.contents=[]
    def add_contents(self,content):
        for val in content:
            self.contents.append(val)
    def remove_content(self,i):
        for _ in range(i):
            self.contents.pop()

st=[stack(val) for i,val in enumerate(start[290:].split('   '))]
st2=[stack(val) for i,val in enumerate(start[290:].split('   '))]
#part1


for i,val in enumerate(st):
    val.add_contents([unit[val.collum] for _,unit in enumerate(start_stack) if unit[val.collum]!=' '])
#print(st[8].contents[-5:][::-1])

for _,val in enumerate(instruct):
    i=int(val.split(' ')[1])
    old=int(val.split(' ')[3])-1
    new=int(val.split(' ')[5])-1
    st[new].add_contents(st[old].contents[-i:][::-1])
    st[old].remove_content(i)

end_state=""
for _,stack in enumerate(st):
    end_state+=stack.contents[-1]
print(end_state)

#part2
for i,val in enumerate(st2):
    val.add_contents([unit[val.collum] for _,unit in enumerate(start_stack) if unit[val.collum]!=' '])
#print(st[8].contents[-5:][::-1])

for _,val in enumerate(instruct):
    i=int(val.split(' ')[1])
    old=int(val.split(' ')[3])-1
    new=int(val.split(' ')[5])-1
    st2[new].add_contents(st2[old].contents[-i:])
    st2[old].remove_content(i)

end_state2=""
for _,stack in enumerate(st2):
    end_state2+=stack.contents[-1]
print(end_state2)
