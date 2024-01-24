def merge_the_tools(string, k):
    # your code goes here
    length = len(string)//k
        
    for i in range(length):
        s = string[:k]
        string = string[k:]
        
        dup = ""
        for i in s:
            if i in dup:
                pass
            else:
                dup += i
        print(dup)
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
