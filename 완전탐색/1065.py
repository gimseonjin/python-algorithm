'''
문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1
보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

input
110

output
99
'''

import sys

input = sys.stdin.readline

def is_hansu(number: int) -> bool:
    previous_difference = None
    while number >= 10:
        last_digit = number % 10
        number //= 10
        next_to_last_digit = number % 10
        current_difference = last_digit - next_to_last_digit
        
        if previous_difference is None:
            previous_difference = current_difference
        elif previous_difference != current_difference:
            return False
    return True

n = int(input().strip())

hansu_counts = sum(list(is_hansu(i) for i in range(1, n+1)))

print(hansu_counts)
