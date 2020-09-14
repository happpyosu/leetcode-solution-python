# 网易笔试第一题 樱桃串

m, n = list(map(int, input().split()))
mapping = {}

for i in range(n):
    line = input().split()
    mapping.setdefault(line[0], {})
    mapping[line[0]].update({line[1]: line[2]})

def solution(mapping: dict):
    cnt = 0
    for node, child in mapping.items():
        if len(child) < 2:
            continue
        flag = True
        for c in child.values():
            if c in mapping:
                flag = False
                break
        if flag:
            cnt += 1

    return cnt


