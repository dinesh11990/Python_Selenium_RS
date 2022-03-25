it = 4

#while loop check the condition first and keep on executing until fail
while it>1:
    if it !=3:
        print(it)
    it=it-1

print('while loop execution is done')

print("************************************")

# while loop 2nd part
while it > 1:
    if it == 3:
        break
    print(it)
    it = it - 1

print('while loop execution is done')


print("************************************")

it1=10

# while loop 3rd part
while it1 > 1:
    if it1 == 3:
        break
    print(it1)
    it1 = it1 - 1

print('while loop execution is done')


print("************************************")

it2=10

while it2 > 1:

    if it2 == 9:

        it2= it2 -1

        continue
    if it2 == 3:
        break

    print(it2)

    it2 = it2 - 1

print('while loop execution is done')