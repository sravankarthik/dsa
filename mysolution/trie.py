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
    for i in range(len(patterns)):
        for j in range(len(patterns[i])):
            tree[j] = {patterns[i][j]: j+1}
            count += 1
        break
    count += 1
    for i in range(1, len(patterns)):
        curr = tree[0]
        for j in range(len(patterns[i])):
            if patterns[i][j] in curr.keys():
                curr = tree[curr[patterns[i][j]]]
            else:
                curr[patterns[i][j]] = count
                tree[count] = {}
                curr = tree[count]
                count += 1

    return tree


print(build_trie(['ATA']))
print(build_trie(['AT', 'AG', 'AC']))
print(build_trie(['ATAGA', 'ATC', 'GAT']))
print(build_trie(
    ['panamabananas$', 'anamabananas$', 'namabananas$', 'amabananas$', 'mabananas$', 'abananas$', 'bananas$', 'ananas$',
     'nanas$', 'anas$', 'nas$', 'as$', 's$']))

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))