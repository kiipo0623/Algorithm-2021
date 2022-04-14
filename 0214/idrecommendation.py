def solution(new_id):
    new_id = new_id.lower()

    r2 = ''
    for word in new_id:
        if word.isalpha() or word.isdigit() or word in '-_.':
            r2 += word
    new_id = r2

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    if len(new_id) > 1 and new_id[0] == '.':
        new_id = new_id.lstrip('.')
    if new_id[-1] == '.':
        new_id = new_id.rstrip('.')
    # 1개 이상인 경우를 고려해서 : 이렇게 세심한 부분을 내가 챙길 수 있을까?

    if len(new_id) == 0:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')

    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3-len(new_id))

    return new_id
print(solution("=.="))