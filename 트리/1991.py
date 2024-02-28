'''
문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.



예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

input
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

output
ABDCEFG
DBAECFG
DBEGFCA

'''

from dataclasses import dataclass, field
from typing import Optional, Dict
from enum import Enum, auto
import sys

input = sys.stdin.readline

@dataclass
class TreeNode:
    value: int
    left: Optional['TreeNode'] = field(default=None, repr=False)
    right: Optional['TreeNode'] = field(default=None, repr=False)

def initialize_tree(input_lines: list[str]) -> TreeNode:
    nodes: Dict[str, TreeNode] = {}
    
    # 먼저 모든 노드 인스턴스를 생성합니다.
    for line in input_lines:
        root, left, right = line.split()
        if root not in nodes:
            nodes[root] = TreeNode(value=root)
        if left != '.' and left not in nodes:
            nodes[left] = TreeNode(value=left)
        if right != '.' and right not in nodes:
            nodes[right] = TreeNode(value=right)
    
    # 이제 각 노드에 대해 자식 노드를 설정합니다.
    for line in input_lines:
        root, left, right = line.split()
        if left != '.':
            nodes[root].left = nodes[left]
        if right != '.':
            nodes[root].right = nodes[right]
    
    # 루트 노드를 반환합니다 (여기서는 첫 번째 노드를 루트로 가정합니다).
    return nodes[input_lines[0].split()[0]]

def preorder(node: Optional[TreeNode]):
    if node is None:
        return
    print(node.value, end='')
    preorder(node.left)
    preorder(node.right)

def inorder(node: Optional[TreeNode]):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end='')
    inorder(node.right)

def postorder(node: Optional[TreeNode]):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end='')

class TraversalOrder(Enum):
    PREORDER = auto()
    INORDER = auto()
    POSTORDER = auto()

def traverse_tree(node: Optional[TreeNode], order: TraversalOrder):
    if order == TraversalOrder.PREORDER:
        preorder(node)
        print()
    elif order == TraversalOrder.INORDER:
        inorder(node)
        print()
    elif order == TraversalOrder.POSTORDER:
        postorder(node)
        print()
    else:
        print("Unknown order")

n = int(input().strip())
input_lines = [input().strip() for _ in range(n)]

root_node = initialize_tree(input_lines)

traverse_tree(root_node, TraversalOrder.PREORDER)
traverse_tree(root_node, TraversalOrder.INORDER)
traverse_tree(root_node, TraversalOrder.POSTORDER)