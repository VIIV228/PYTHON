s = str(input())

def double_word(s):
    double = ''.join([x+x for x in s])
    return double

print(double_word(s))