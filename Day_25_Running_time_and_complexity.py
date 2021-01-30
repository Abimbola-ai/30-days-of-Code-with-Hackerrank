for i in range(int(input())):
    n = int(input())
    
    if n==1 or n==0 or (n % 2 == 0 and n > 2):
        print("Not prime")
    else:
        # Not prime if divisable by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n%i == 0:
                print("Not prime")
                break
        else:
            print("Prime")