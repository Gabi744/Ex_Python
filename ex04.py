import random
maliste = [random.randint(1, 15) for _ in range (5)]

print(maliste)
def fonction(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list [j+1]:

                list[j], list[j+1] = list[j+1], list[j]

fonction(maliste)

print("dans l'ordre:")
for num in maliste:
    print(num)