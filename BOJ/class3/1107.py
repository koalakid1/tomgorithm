# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 

# 수빈이가 지금 보고 있는 채널은 100번이다.
# # class 3++
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    broken = list(map(int, input().split()))
    
    min_count = abs(100 - n)
    n_length = len(str(n))
    
    for num in range(0, 1000001):
        num_checks = str(num)

        check = True
        for num_check in num_checks:
            if int(num_check) in broken:
                check = False
                break
        
        
        if check:
            min_count = min(min_count, abs(num - n) +  len(num_checks))

    print(min_count)