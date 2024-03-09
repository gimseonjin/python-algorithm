'''
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.
'''
import sys

input = sys.stdin.readline

class BitMaskSet:
    def __init__(self):
        self.mask = 0

    def add(self, x: int):
        self.mask |= (1 << x)

    def remove(self, x: int):
        self.mask &= ~(1 << x)

    def check(self, x: int):
        print(1 if self.mask & (1 << x) else 0)
    
    def toggle(self, x: int):
        self.mask ^= (1 << x)

    def all(self):
        self.mask = (1 << 20) - 1

    def empty(self):
        self.mask = 0

def parse_and_execute_command(bitmask_set: BitMaskSet, command: str):
    parts = command.split()
    operation = parts[0]
    if operation in {"add", "remove", "check", "toggle"}:
        x = int(parts[1]) - 1
        getattr(bitmask_set, operation)(x)
    else:
        getattr(bitmask_set, operation)()

bitmask_set = BitMaskSet()
n = int(input().strip())
for _ in range(n):
    command = input().strip()
    parse_and_execute_command(bitmask_set, command)
