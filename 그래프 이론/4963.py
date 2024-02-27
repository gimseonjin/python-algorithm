'''
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
'''

import sys

# 재귀 깊이 제한 증가
sys.setrecursionlimit(10000)

def dfs(island_map, is_visited, x, y):
    if is_visited[x][y] or island_map[x][y] == 0:
        return

    is_visited[x][y] = True

    dx = [0,0,-1,1,-1,1,-1,1]
    dy = [-1,1,0,0,-1,-1,1,1]

    for i in range(8):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if  0 <= next_x < len(island_map) and 0 <= next_y < len(island_map[0]):
            if island_map[next_x][next_y] == 1:
                dfs(island_map, is_visited, next_x, next_y)

while True:
    w, h = map(int, sys.stdin.readline().split())
    
    if w == 0 and h == 0:
        break

    island_map = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    is_visited = [[False for _ in range(w)] for _ in range(h)]

    cnt = 0
    for x in range(h):
        for y in range(w):
            if island_map[x][y] == 1 and not is_visited[x][y]:
                dfs(island_map, is_visited, x, y)
                cnt += 1
    print(cnt)