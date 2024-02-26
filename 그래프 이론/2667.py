'''
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

input:
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

output:
3
7
8
9
'''

from collections import deque
import sys
input = sys.stdin.readline

def check_danji(x, y, n, road_map, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and road_map[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1
    return count

n = int(input().strip())
road_map = [list(map(int, input().strip())) for _ in range(n)]
is_visisted = [[False for _ in range(n)] for _ in range(n)]

danji = []
for i in range(n):
    for j in range(n):
        if road_map[i][j] == 1 and not is_visisted[i][j]:
            danji.append(check_danji(i, j, n, road_map, is_visisted))

print(len(danji))
for d in danji:
    print(d)