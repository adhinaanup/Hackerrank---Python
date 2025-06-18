if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score=max(arr)
    sec=-1
    arr.sort(reverse=True)
    for i in arr:
        if i<max_score:
            sec=i
            break
    print(sec)
