A = [1,2,3,4,5,6,7,8,9,10]
B = ['Tjasi','tjasi','tanana']
sum = 0
for item in B:
    print(item)

for item in A:
    sum += item # sum = sum + item
print(sum)

for i in range(1,9): # i gonna have values 1 - 8
    print(i)

for i in range(1,10):
    if i == 3:
        break
    print(i)

for i in range(1,10):
    if i == 3:
        continue
    print(i)

i = 0
while i < len(B):
    print(B[i])
    i = i + 1

while True:
    answer = input("Start typing...")
    if answer == "quit":
        print('Exiting...\n')
        break
    print("Your answer was " + answer)

counter = 0
while counter <= 11:
    print(counter)
    counter = counter + 2

for x in range(1, 3):  #2
    print('for loop 1')
    for y in range(1, 4):  #1
        print('for loop 2')
        for z in range(1, 5):
            print('for loop 3')
            print('%d * %d * %d = %d' % (x, y, z, x*y))
