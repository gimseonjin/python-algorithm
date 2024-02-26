'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

input:
4 5 1
1 2
1 3
1 4
2 4
3 4

output:
1 2 4 3
1 2 3 4
'''

from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, cur_v, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(cur_v)
    result.append(str(cur_v + 1))  # 인덱스를 1 기반으로 출력 조정

    for next_v in sorted(graph[cur_v]):
        if next_v not in visited:  # 여기서는 인덱스 조정 없이 바로 사용
            dfs(graph, next_v, visited, result)

    return ' '.join(result)

def bfs(graph, start_v):
    q = deque()
    q.append(start_v - 1)
    visited = {start_v - 1: True}

    result_str = []
    while q:
        cur_v = q.popleft()
        result_str.append(str(cur_v+1))
        for next_v in sorted(graph[cur_v]):
            if next_v not in visited:  # 여기서는 인덱스 조정 없이 바로 사용
                q.append(next_v)
                visited[next_v] = True

    return ' '.join(result_str)

n, m, start = map(int, input().split())
node_map = [[] for _ in range(n)]

for _ in range(m):
    start_node, end_node = map(int, input().split())
    node_map[start_node-1].append(end_node-1)  # 인접 리스트 구성
    node_map[end_node-1].append(start_node-1)  # 양방향 연결 고려

# BFS와 DFS 실행
dfs_result = dfs(node_map, start-1)
bfs_result = bfs(node_map, start)

print(dfs_result)
print(bfs_result)
