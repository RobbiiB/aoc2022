with open('/Users/robin/Input_day_2.txt', 'r') as file:
    string_list = file.read().split('\n')[:-1]
print(string_list)
dict = {
        'A X' : 4,    #RR
        'A Y' : 8,    #RP
        'A Z' : 3,    #RS
        'B X' : 1,    #PR
        'B Y' : 5,    #PP
        'B Z' : 9,    #PS
        'C X' : 7,    #SR
        'C Y' : 2,    #SP
        'C Z' : 6     #SS
    }
dict_2={
        'A X': 3,  # RS
        'A Y': 4,  # RR
        'A Z': 8,  # RP
        'B X': 1,  # PR
        'B Y': 5,  # PP
        'B Z': 9,  # PS
        'C X': 2,  # SP
        'C Y': 6,  # SS
        'C Z': 7   # SR
    }
score1,score2=0,0
for _,val in enumerate(string_list):
    score1+=dict[val]
    score2+=dict_2[val]
print(score1)
print(score2)