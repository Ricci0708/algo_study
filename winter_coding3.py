def solution(cookie):
    answer = 0

    for i in range(len(cookie) - 1):
        left = i
        right = i + 1
        l = cookie[i]
        r = cookie[i+1]
        while True:
            if l == r and l > answer:
                answer = l
                left -= 1
                if left in range(len(cookie)):
                    l += cookie[left]
                else:
                    break
            elif l < r:
                left -= 1
                if left in range(len(cookie)):
                    l += cookie[left]
                else:
                    break
            else:
                right += 1
                if right in range(len(cookie)):
                    r += cookie[right]
                else:
                    break
                    
    return answer


print(solution([1,1,2,3,1,1,1,1,9]))