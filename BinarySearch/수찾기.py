# 1920번 : 수 찾기 
# https://www.acmicpc.net/problem/1920

import sys
sys.stdin = open("input.txt", 'r')

def BinarySearch(n):
    low = 0
    high = len(m_arr)-1
    while low <= high:
        mid = (low + high) // 2
        if n_arr[mid] == n:
            return True
        else:
            if n_arr[mid] < n:
                low = mid + 1
            elif n_arr[mid] > n:
                high = mid - 1
    return False

if __name__=="__main__":
    n, n_arr = int(input()), list(map(int,input().split()))
    m, m_arr = int(input()), list(map(int,input().split()))
    n_arr.sort()
    for num in m_arr:
        # 존재하면 1 존재 하지 않으면 0
        if BinarySearch(num):
            print(1)
        else:
            print(0)




