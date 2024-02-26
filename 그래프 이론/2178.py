'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

input:
4 6
101111
101010
101011
111011

output:
15
'''
from collections import deque
import sys
input = sys.stdin.readline


def find_path(node_map, start, end):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 시작점에서부터의 거리를 저장할 맵 생성, 초기값은 -1 (방문하지 않음)
    distance_map = [[-1 for _ in range(len(node_map[0]))] for _ in range(len(node_map))]
    
    queue = deque()
    queue.append(start)
    distance_map[start[0]][start[1]] = 1  # 시작점의 거리는 0

    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            return distance_map[x][y]  # 종료점에 도달했을 때의 거리 반환
        
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            # 맵 범위 내에 있고, 방문하지 않았으며, 이동할 수 있는 위치인지 확인
            if 0 <= next_x < len(node_map) and 0 <= next_y < len(node_map[0]) and node_map[next_x][next_y] == 1 and distance_map[next_x][next_y] == -1:
                queue.append((next_x, next_y))
                distance_map[next_x][next_y] = distance_map[x][y] + 1  # 거리 업데이트

    return -1


n, m = map(int, input().split())

node_map = [list(map(int, input().strip())) for _ in range(n)]

start = (0,0)
end = (n-1, m-1)

print(find_path(node_map, start, end))