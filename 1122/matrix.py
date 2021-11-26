# 행렬 테두리 회전하기
def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(1, rows * columns + 1):
        matrix[(i - 1) // columns][(i - 1) % columns] = i
    # 판을 다 만들어 둔 상태
    # x1, y1부터 이동해서 x2, y1가 되면 방향 전환 .. 이런 식
    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        moveflag = False  # True일 때 가로로 이동하도록
        vertex = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
        start_x, start_y = x1, y1
        backup = matrix[start_x][start_y]
        minimum = backup

        for _ in range((x2 - x1) * 2 + (y2 - y1) * 2):
            if (start_x, start_y) in vertex:  # 방향 전환
                moveflag = not moveflag

            if moveflag == True:  # 가로로 이동할때
                now = backup
                backup = matrix[start_y][start_x + 1]
                matrix[start_y][start_x + 1] = now
                start_x += 1

            else:
                now = backup
                backup = matrix[start_y + 1][start_x]
                matrix[start_y + 1][start_x] = now
                start_y += 1

            if backup < minimum:
                minimum = backup

        answer.append(minimum)
        print(matrix)

    return answer

print(solution(
    6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
))