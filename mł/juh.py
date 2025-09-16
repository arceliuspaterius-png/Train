
#a = 10
#b = "leje"
#c = False

#if a == 10: # or b == "ejel":
#    print(b)
#elif a == 132:
#    print ("lmao")
#else:
#    print (c)



for i in range(1, 101): # range 0 - 9
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

