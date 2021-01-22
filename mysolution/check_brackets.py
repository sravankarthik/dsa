from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    li = []
    dicty={}
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            li.append(next)
            dicty[len(li)-1]=i
        if len(li)==0 and next in ")]}":
            return i+1
        if next in ")]}":
            # Process closing bracket, write your code here
            y = len(li) - 1
            count = 0
            if li[y] == "(" and next == ")":
                x = li.pop(y)
                count += 1
                q=dicty.pop(y)
            elif li[y] == "[" and next == "]":
                x = li.pop(y)
                count += 1
                q = dicty.pop(y)
            elif li[y] == "{" and next == "}":
                x = li.pop(y)
                count += 1
                q = dicty.pop(y)
            if count == 0:
                return i+1


    if len(li) == 0:
        return -1
    else:
        return max(dicty.values())+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
