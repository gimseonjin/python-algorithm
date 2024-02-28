'''
문제
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

예를 들어, 다음과 같은 트리가 있다고 하자.



현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.



이제 리프 노드의 개수는 1개이다.

입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

input
5
-1 0 0 1 1
2

output
2

'''

from dataclasses import dataclass, field
from typing import List, Dict
import sys

input = sys.stdin.readline

@dataclass
class TreeNode:
    value: int
    children: List['TreeNode'] = field(default_factory=list)

def build_tree(parents: List[int]) -> Dict[int, TreeNode]:
    nodes = {i: TreeNode(i) for i in range(len(parents))}
    root = None
    for i, p in enumerate(parents):
        if p == -1:
            root = nodes[i]
        else:
            nodes[p].children.append(nodes[i])
    return root

def delete_subtree(root: TreeNode, delete_value: int) -> None:
    queue = [root]
    while queue:
        current = queue.pop(0)
        current.children = [child for child in current.children if child.value != delete_value]
        queue.extend(current.children)

def count_leaf_nodes(node: TreeNode) -> int:
    if not node.children:
        return 1
    return sum(count_leaf_nodes(child) for child in node.children)

# 예제 입력 처리
n = int(input())
parents = list(map(int, input().split()))
delete_node = int(input())

root = build_tree(parents)
if root.value == delete_node:
    print(0)
else:
    delete_subtree(root, delete_node)
    print(count_leaf_nodes(root))
