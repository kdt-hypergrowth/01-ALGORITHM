import sys
sys.stdin = open('행복한지슬픈지.txt')

n = input()                  # How are you :-) doing :-( today :-)?
happy = n.count(':-)')
sad = n.count(':-(')

if happy == 0 and sad == 0:
    print('non')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')