# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.m = []
        for _ in range(bucket_count):
            self.m.append({})

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        self.m[ans % self.bucket_count][s] = ans
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            k = []
            if self.m[query.ind] == {}:
                print()
            else:
                for i in self.m[query.ind].keys():
                    k.append(i)
                k.reverse()
                for i in k:
                    print(i, end=' ')
                print()
            #self.write_chain(cur for cur in reversed(self.elems)
                             #if self._hash_func(cur) == query.ind)
        else:
            if query.type == 'add':
                self._hash_func(query.s)
            else:
                ans = 0
                count =0
                for c in reversed(query.s):
                    ans = (ans * self._multiplier + ord(c)) % self._prime
                y = ans % self.bucket_count
                if query.type == 'find':
                    for i in self.m[y].keys():
                        if self.m[y][i] == ans and query.s == i:
                            print('yes')
                            count = 1
                            break
                    if count == 0:
                        print('no')
                elif query.type == 'del':
                    for i in self.m[y].keys():
                        if self.m[y][i] == ans and query.s == i:
                            del self.m[y][i]
                            break


            '''try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)'''

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
