# The included code stub will read an integer, n , from STDIN.
# Without using any string methods, try to print the following: 123...n

def diaplay(n):
    for i in range(n):
        print(i+1, end="")
        
if __name__ == '__main__':
    n = int(input())
    diaplay(n)
