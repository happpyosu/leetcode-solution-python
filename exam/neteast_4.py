males = list(map(int, input().split()))
females = list(map(int, input().split()))
n = int(input())

mapping = {}
for i in range(n):
    line = list(map(int, input().split()))
    mapping.setdefault(line[0], []) 
    mapping.setdefault(line[1], [])
    mapping[line[0]].append(line[1])
    mapping[line[1]].append(line[0])


def solution(mapping):
    ans = 0
    while mapping:
        a = sorted(mapping.keys(), key=lambda x: len(mapping[x]))[0]
        b = mapping[a].pop()
        del mapping[a]
        del mapping[b]
        for k, v in mapping.items():
            if a in v:
                mapping[k].remove(a)
            if b in v:
                mapping[k].remove(b)
        temp = []
        for k, v in mapping.items():
            if len(v) == 0:
                temp.append(k)

        for x in temp:
            del mapping[x]

        ans += 1
    return ans


print(solution(mapping))
