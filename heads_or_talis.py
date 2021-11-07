import random 
test_seed = int(input("create a seed namber : "))
random.seed(test_seed)
r = random.randint(0,1)
if (r==0):
    print("Tail")
else:
    print("Head")


