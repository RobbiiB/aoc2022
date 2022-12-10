import numpy as np
with open('/Users/robin/Input_day_8.txt','r') as file:
    string = file.read().split('\n')
trees_str = []
for val in string:
    trees_str.append([*val])
np_trees = np.array(trees_str).astype(int)


#part1
np_tree_visible = np.zeros(np.shape(np_trees),dtype=bool)
for i,tree_line in enumerate(np_trees):
    for j,tree in enumerate(tree_line):
        if np.shape(np_trees[i,j+1:])==(0,) or np.shape(np_trees[i,:j])==(0,) or\
                np.shape(np_trees[i+1:,j])==(0,) or np.shape(np_trees[:i,j])==(0,):
            np_tree_visible[i,j]=True
        elif np.max(np_trees[i,:j])<tree:
            np_tree_visible[i, j] = True
        elif np.max(np_trees[i, j+1:]) < tree:
            np_tree_visible[i, j] = True
        elif np.max(np_trees[i+1:,j])<tree:
            np_tree_visible[i, j] = True
        elif np.max(np_trees[:i,j]) < tree:
            np_tree_visible[i, j] = True
#print(np_tree_visible)
visibility=0
for i,tree_line in enumerate(np_tree_visible):
    for x,tree in enumerate(tree_line):
        if tree:
            visibility+=1
print(visibility)

#part2
tree_vs = np.zeros(np.shape(np_trees))
for i,tree_line in enumerate(np_trees):
    for j,tree in enumerate(tree_line):
        r=0
        l=0
        t=0
        b=0
        if i==0 or i==len(tree_line)-1 or j==0 or j==len(np_trees[0,:])-1:
            tree_vs[i,j]=0
        else:
            vr=True
            vl=True
            vt=True
            vb=True
            while vr:
                if np_trees[i,j+1:][r]>=tree or r==len(np_trees[i,j+1:])-1:
                    r += 1
                    vr=False
                else:
                    r+=1
            while vl:
                if np_trees[i,:j][::-1][l]>=tree or l==len(np_trees[i,:j])-1:
                    l += 1
                    vl=False
                else:
                    l+=1
            while vt:
                if np_trees[:i,j][::-1][t]>=tree or t==len(np_trees[:i,j])-1:
                    t += 1
                    vt=False
                else:
                    t+=1
            while vb:
                if np_trees[i+1:,j][b]>=tree or b==len(np_trees[i+1:,j])-1:
                    b += 1
                    vb=False
                else:
                    b+=1
            tree_vs[i, j] = r*l*t*b
print(np.max(tree_vs))
