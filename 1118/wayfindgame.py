# 길 찾기 게임
from collections import defaultdict

def solution(nodeinfo):
    answer = [[]]
    # 부모:자식으로 저장해야 하는지 아니면 level별로 저장해야 하는지 : 전위/후위 탐색방법을 보니 부모자식(좌,우구분)
    node_tree = defaultdict(list) # 노드번호 = [leftnode, rightnode]
    idx_nodeinfo = [] # idx 포함 : 나중에 sort해서 반복문 돌릴 때 사용
    node_dict = defaultdict(list) # 노드 번호 : [x좌표, y좌표]

    for idx, node in enumerate(nodeinfo):
        x, y = node
        idx_nodeinfo.append((idx, x, y))
        node_dict[idx] = [x, y]

    # y좌표가 큰 순서대로 배치
    sorted_nodeinfo = sorted(idx_nodeinfo, key=lambda x: (-x[1], -x[0]))

    root = sorted_nodeinfo[0]
    # 어떻게 노드마다 좌우 leaf를 설정할지
    # 어떻게 하면 효율적으로 x,y 좌표와 노드 번호 둘 다를 고려할지
    for idx, node in enumerate(sorted_nodeinfo):
        num, x, y = node
        for leaf in sorted_nodeinfo[idx+1:]:
            node_tree[num].append()






    # 순회 : 그냥 구글링해서 코드 보고 하면 됨



    return answer

print(solution(
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
))