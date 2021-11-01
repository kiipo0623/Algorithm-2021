# 호텔 방 배정

def binary_search(arr, target):
    start, end = 0, len(arr)

    while start<=end:
        mid = (start + end) // 2
        if len(arr)>mid:
            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else: #있다는 뜻
                return (False, mid+1)
    return (True, 1)


#0부터 k까지 len = K+1
def solution(k, room_number):
    answer = [room_number[0]]
    rooms = [room_number[0]]
    for client in room_number[1:]:
        TF, order = binary_search(rooms, client)
        if TF: # True인 경우
            answer.append(client)
            rooms.insert(order, client)
        else:
            while True:
                client += 1
                if binary_search(rooms, client):
                    answer.append(client)
                    rooms.insert(order, client)
                    break
    return answer

print(solution(10, [1,3,4,1,3,1]))

