# 널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
# class3+
import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    min_heap = []
    for _ in range(int(input())):
        order = int(input())
        if order:
            heapq.heappush(min_heap, order)
        else:
            if min_heap:
                print(heapq.heappop(min_heap))
            else:
                print(0)
