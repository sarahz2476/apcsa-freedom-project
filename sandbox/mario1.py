from cs50 import get_int

def main():
    height = get_int()
    for i in range(height):
        print("#")
        
def get_height():
    while True:
        try: 
            n = get_int("Height: ")
            if n > 0:
                break        
        except ValueError:
            print ("That's not an integer!")
    return n
main ()