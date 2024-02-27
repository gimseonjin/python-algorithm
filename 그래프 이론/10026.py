'''
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

input
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

'''
from collections import deque
from dataclasses import astuple, dataclass
import sys
from typing import List, Tuple

input = sys.stdin.readline

@dataclass
class FindAreaParams:
    draw: List[List[int]]
    is_visited: bool
    cursor: Tuple[int, int]
    is_blindness: bool

def find_area(params: FindAreaParams):
    draw, is_visited, cursor, is_blindness = params.draw, params.is_visited, params.cursor, params.is_blindness
    x, y = cursor
    color = draw[x][y]

    queue = deque([(x, y)])
    is_visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < len(draw) and 0 <= ny < len(draw[0]) and not is_visited[nx][ny]:
                if not is_blindness:
                    if draw[nx][ny] == color:
                        queue.append((nx, ny))
                        is_visited[nx][ny] = True
                else:
                    if color in ["R", "G"] and draw[nx][ny] in ["R", "G"]:
                        queue.append((nx, ny))
                        is_visited[nx][ny] = True
                    elif color == "B" and draw[nx][ny] == "B":
                        queue.append((nx, ny))
                        is_visited[nx][ny] = True

    return 1

n = int(input().strip())

draw = [list(input().strip()) for _ in range(n)]

is_visited = [[False for _ in range(n)] for _ in range(n)]
is_visited_for_blindness = [[False for _ in range(n)] for _ in range(n)]

count, count_for_blindness = 0, 0

for i in range(n):
    for j in range(n):
        if not is_visited[i][j]:
            count += find_area(FindAreaParams(draw, is_visited, (i, j), False))

        if not is_visited_for_blindness[i][j]:
            count_for_blindness += find_area(FindAreaParams(draw, is_visited_for_blindness, (i, j), True))

print(count, count_for_blindness)