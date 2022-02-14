# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    strings = input().strip()

    alpha = [-1 for _ in range(26)]
    for index, string in enumerate(strings):
        string_num = ord(string) - ord('a')
        if alpha[string_num] == -1:
            alpha[string_num] = index
    
    for alpha_num in alpha:
        print(alpha_num, end=" ")