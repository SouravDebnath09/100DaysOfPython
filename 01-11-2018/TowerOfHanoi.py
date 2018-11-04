# This is the solution of tower of Hanoi problem
number = int(input("Please provide the number:"))
tower1 = []
tower2 = []
tower3 = []
for i in range(number):
    tower1.append(i + 1)

if number <= 0:
    print("Invalid input")
else:
    while len(tower3) != number:
        if (len(tower1) > 0) and (len(tower2) == 0):

            print("First block")
            tower3.append(tower1[0])
            tower1.pop(0)
            list.reverse(tower1)
            tower2 = tower1.copy()
            tower1.clear()
            print("Tower1:", tower1, "\n Tower2:", tower2, "\n Tower3:", tower3)

        elif (len(tower2) > 0) and (len(tower1) == 0):
            print("Second block")
            tower3.append(tower2[-1])
            tower2.pop(-1)
            list.reverse(tower2)
            tower1 = tower2.copy()
            tower2.clear()
            print("Tower1:", tower1, "\n Tower2:", tower2, "\n Tower3:", tower3)
        else:
            print("Third block")
            print("Tower1:", tower1, "\n Tower2:", tower2, "\n Tower3:", tower3)
