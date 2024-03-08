'''
문제
세로 
$R$칸, 가로 
$C$칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (
$1$행 
$1$열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 
$R$과 
$C$가 빈칸을 사이에 두고 주어진다. (
$1 ≤ R,C ≤ 20$) 둘째 줄부터 
$R$개의 줄에 걸쳐서 보드에 적혀 있는 
$C$개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
'''
import sys
from typing import List, Set

input = sys.stdin.readline

DX = (1, 0, -1, 0)
DY = (0, 1, 0, -1)

def max_path_length(board: List[List[str]], x: int, y: int, visited: Set[str], n: int, m: int) -> int:
    max_length = 1
    for i in range(4):
        next_x, next_y = x + DX[i], y + DY[i]
        
        if 0 <= next_x < n and 0 <= next_y < m:
            next_char = board[next_x][next_y]
            if next_char not in visited:
                visited.add(next_char)
                max_length = max(max_length, max_path_length(board, next_x, next_y, visited, n, m) + 1)
                visited.remove(next_char)
    
    return max_length

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

initial_visited = {board[0][0]}
max_length = max_path_length(board, 0, 0, initial_visited, n, m)

print(max_length)