if __name__ == '__main__':
    s =input()
    one=False
    two=False
    three=False
    four=False
    five=False

    for c in s:
        if not one:
            one=c.isalnum()
        if not two:
            two=c.isalpha()
        if not three:
            three=c.isdigit()
        if not four:
            four=c.islower()
        if not five:
            five=c.isupper()

    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
