# Uses python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

def build_trie(patterns):
    tree = dict()
    print(patterns)
    count = 0
    c = 0
    for i in range(len(patterns)):
        for j in range(len(patterns[i])):
            if patterns[i][j] == '$':
                tree[j] = {patterns[i][j]: [j + 1, c]}
                count += 1
                continue
            tree[j] = {patterns[i][j]: [j + 1]}
            count += 1
        break
    count += 1
    c += 1
    for i in range(1, len(patterns)):
        curr = tree[0]
        for j in range(len(patterns[i])):
            if patterns[i][j] in curr.keys():
                curr = tree[curr[patterns[i][j]][0]]
            else:
                if patterns[i][j] == '$':
                    curr[patterns[i][j]] = [count, c]
                    tree[count] = {}
                    curr = tree[count]
                    count += 1
                    c += 1
                    continue
                curr[patterns[i][j]] = [count]
                tree[count] = {}
                curr = tree[count]
                count += 1

    return tree


def solve(text, n, li):
    result = []
    tree = build_trie(li)
    for i in range(n):
        word = text[i]
        curr = tree[0]
        for j in range(len(word)):
            if word[j] in curr.keys():
                curr = tree[curr[word[j]][0]]
            else:
                break
        w = []
        for a in curr.keys():
            w.append({a: curr[a]})
        while w:
            b = w[0]
            if '$' in b.keys():
                if b['$'][1] not in result:
                    result.append(b['$'][1])
                b.pop('$')
            else:
                for a in b.keys():
                    o = tree[b[a][0]]
                    b.pop(a)
                    for e in o.keys():
                        w.append({e: o[e]})
                    break
                if b == {}:
                    w.pop(0)
    return result


#print(build_trie(['AAA']))
# print(build_trie(['AT', 'AG', 'AC']))
# print(build_trie(['ATAGA', 'ATC', 'GAT']))
'''print(build_trie(
    ['panamabananas$', 'anamabananas$', 'namabananas$', 'amabananas$', 'mabananas$', 'abananas$', 'bananas$', 'ananas$',
     'nanas$', 'anas$', 'nas$', 'as$', 's$']))'''
print(solve(['ATCG', 'GGGT'], 2,
            ['AATCGGGTTCAATCGGGGT$', 'ATCGGGTTCAATCGGGGT$', 'TCGGGTTCAATCGGGGT$', 'CGGGTTCAATCGGGGT$',
             'GGGTTCAATCGGGGT$', 'GGTTCAATCGGGGT$', 'GTTCAATCGGGGT$', 'TTCAATCGGGGT$', 'TCAATCGGGGT$', 'CAATCGGGGT$',
             'AATCGGGGT$', 'ATCGGGGT$', 'TCGGGGT$', 'CGGGGT$', 'GGGGT$', 'GGGT$', 'GGT$', 'GT$', 'T$']))
print(solve(['AA'], 1, ['AAA$', 'AA$', 'A$']))
print(solve(['AT', 'A', 'AG'], 3, ['ACATA$', 'CATA$', 'ATA$', 'TA$', 'A$']))


if __name__ == '__main__':
    patterns = input()
    patterns += '$'
    li = []
    for i in range(len(patterns) - 1):
        li.append(patterns[i:])
    tree = build_trie(li)
