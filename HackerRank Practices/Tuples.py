if __name__ == '__main__':
    n = int(input())
    lst = input().split()
    lst = [int(x) for x in lst]
    t = tuple(lst)
    print(hash(t))
