import random

if __name__ == '__main__':
    x = int(input()) + 1
    y = int(input()) + 1
    z = int(input()) + 1
    n = int(input())
    
    outcome = []
    
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i + j + k) != n:
                    outcome.append([i,j,k])
       
    print(outcome)
