# Enter your code here. Read input from STDIN. Print output to STDOUT
def loop_strings(s):
    odd_string = ""
    even_string =""
    for i in range(len(s)):
        if i % 2 == 0:
            even_string += s[i]
        else:
            odd_string += s[i]
    print(even_string + " " + odd_string)

if __name__ == "__main__":
    for i in range(int(input())): 
        loop_strings(input())
 
