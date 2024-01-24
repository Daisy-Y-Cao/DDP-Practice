def split_and_join(line):
    # write your code here
    linelst = line.split(' ')
    new_line = '-'.join(linelst)
    return new_line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
