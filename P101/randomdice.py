import random
roll = input("do you want to roll a dice?")
while roll == "y":
    n = random.randint(1,6)
    if n==1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif n == 2:
        print("[0    ]")
        print("[     ]")
        print("[    0]") 
    elif n == 3:
        print("[0    ]")
        print("[  0  ]")
        print("[    0]") 
    elif n == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]") 
    elif n == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]") 
    else:
        print("[0   0]")
        print("[0   0]")
        print("[0   0]") 
    roll = input("do you want to roll a dice again?")
