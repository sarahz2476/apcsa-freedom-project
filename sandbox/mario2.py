from cs50 import get_int

height = get_int("Height: ")
for i in range(0, height, 1):
    for j in range(height-1,i, -1):
        print(" ", end = '')
    for k in range(-1, i, 1):  
        print("#", end = '')
    print ();
    
    
