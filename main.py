class node:
    def __init__(self):
        self.positionx = 0
        self.positiony = 0
        self.pos_log = set()
        self.new_pos = 0

def move_head(head,direction):
    if direction=='U':
        head.positiony+=1
    elif direction=='D':
        head.positiony-=1
    elif direction=='L':
        head.positionx-=1
    else:
        head.positionx+=1

def move_node(node1,node2):
    if abs(node1.positionx-node2.positionx) <= 1 and abs(node1.positiony-node2.positiony) <= 1:
        pass
    elif node1.positionx==node2.positionx:
        node2.positiony+=int(node1.positiony>node2.positiony)*2 - 1
    elif node1.positiony==node2.positiony:
        node2.positionx+=int(node1.positionx>node2.positionx)*2 - 1
    else:
        node2.positionx+=int(node1.positionx>node2.positionx)*2 - 1
        node2.positiony+=int(node1.positiony>node2.positiony)*2 - 1

def update_pos_log(node1):
    node1.pos_log.add((node1.positionx,node1.positiony))

def move_all_nodes(rope2):
    for i in range(len(rope2)-1):
        move_node(rope2[i],rope2[i+1])

def update_all_pos_log(rope2):
    for i in range(len(rope2)):
        update_pos_log(rope2[i])

def code_for_different_lengths(length):
    rope = [node() for _ in range(int(length))]
    with open('/Users/robin/Input_day_9.txt', 'r') as instructions:
        for movement in instructions:
            direction, distance = movement.rstrip().split()
            for _ in range(int(distance)):
                move_head(rope[0], direction)
                move_all_nodes(rope)
                update_all_pos_log(rope)

    rope[-1].new_pos = len(rope[-1].pos_log)
    print((rope[-1].new_pos))


code_for_different_lengths(2)
code_for_different_lengths(10)