with open('Input_day_3.txt', 'r') as file:
    string_list = file.read().split('\n')[:-1]
dict = {
    'a' :  1 ,
    'b' :  2 ,
    'c' :  3 ,
    'd' :  4 ,
    'e' :  5 ,
    'f' :  6 ,
    'g' :  7 ,
    'h' :  8 ,
    'i' :  9 ,
    'j' :  10 ,
    'k' :  11 ,
    'l' :  12 ,
    'm' :  13 ,
    'n' :  14 ,
    'o' :  15 ,
    'p' :  16 ,
    'q' :  17 ,
    'r' :  18 ,
    's' :  19 ,
    't' :  20 ,
    'u' :  21 ,
    'v' :  22 ,
    'w' :  23 ,
    'x' :  24 ,
    'y' :  25 ,
    'z' :  26 ,
    'A' :  27 ,
    'B' :  28 ,
    'C' :  29 ,
    'D' :  30 ,
    'E' :  31 ,
    'F' :  32 ,
    'G' :  33 ,
    'H' :  34 ,
    'I' :  35 ,
    'J' :  36 ,
    'K' :  37 ,
    'L' :  38 ,
    'M' :  39 ,
    'N' :  40 ,
    'O' :  41 ,
    'P' :  42 ,
    'Q' :  43 ,
    'R' :  44 ,
    'S' :  45 ,
    'T' :  46 ,
    'U' :  47 ,
    'V' :  48 ,
    'W' :  49 ,
    'X' :  50 ,
    'Y' :  51 ,
    'Z' :  52
}

#part 1
prio = 0
for _, bag in enumerate(string_list):
    compartments = [set(bag[i:i + len(bag) // 2]) for i in range(0, len(bag), len(bag) // 2)]
    #comp0_no_dupes = set(compartments[0])
    for letter in compartments[0]:
        if letter in compartments[1]:
            prio += dict[letter]
        else:
            pass
print(prio)


#part 2
prio=0
for group in range(len(string_list)//3):
    bag1 = set(string_list[3*group])
    bag2 = set(string_list[3*group+1])
    bag3 = set(string_list[3*group+2])
    for letter in bag1:
        if letter in bag2 and letter in bag3:
            prio+=dict[letter]
        else:
            pass
print(prio)
file.close()
