# python3
import sys


def btw(text):
    li = []
    #li.append(text)
    x = len(text)
    for i in range(x):
        text = text[x-1]+text[:x-1]
        li.append(text)
    li.sort()
    print(li)
    result = ""
    for i in li:
        result += i[-1]

    return result

print(btw('ACACACAC$'))
print(btw('AGACATA$'))
print(btw('AA$'))
if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(btw(text))
