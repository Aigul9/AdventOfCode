import string

with open('answers.txt', 'r') as f:
    answers = [line.splitlines() for line in f.read().split('\n\n')]

print(sum(len(set().union(*ans)) for ans in answers))
print(sum(len(set(string.ascii_lowercase).intersection(*ans)) for ans in answers))
