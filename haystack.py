import random

# for x in range(10):
#    print(random.randint(1,100))

hay = 'hay hay hay hay hay hay hay hay hay hay\n'
needle = 'needle\n'

f = open('haystack', 'w')

needle_line = random.randint(1, 30000)

for x in range(30000):
    if (x == needle_line):
        print("Needle Line")
        f.write("needle\n")
    else:
        f.write(hay + "\n")

f.close()
