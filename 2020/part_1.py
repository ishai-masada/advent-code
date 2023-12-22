import itertools

with open("data.txt", 'r') as f:
    sample = f.read().splitlines()

def product(iterator):
    prodo = 1
    for elem in iterator:
        prodo *= elem
    return prodo

true_sample = [int(num) for num in sample if num!= '']
answer = 0
break_notice = False

for combo in itertools.combinations(true_sample, 3):
    if sum(combo) == 2020:
        answer = product(combo)
        print(answer)
        break
