d = {}
with open("zoo.txt") as file:
    for line in file:
        key, value = line.split()
        d[key] = value
print ("Please write animal from the list:")
print(d.keys())
animal=input()
print("In our zoo you can see", d[animal], animal)