from collections import defaultdict
def fight(monster, character):
    count = 0
    hp = character['hp']
    name, point, m_hp, m_gong, m_bang = monster.split()
    point, m_hp, m_gong, m_bang = int(point), int(m_hp), int(m_gong), int(m_bang)

    while m_hp > 0 or character['hp'] > 0:
        m_hp -= character['gong'] - m_bang
        count += 1
        if character['gong'] - m_bang <= 0:
            return [False, 0]
        if m_hp <= 0:
            return [False, 0]

        character['hp'] -= m_gong - character['bang']
        if character['hp'] < 0:
            return [False, 0]
        character['hp'] = hp

    return [True, count]

def solution(character, monsters):
    character = character.split()
    character_dict = {'hp': int(character[0]), 'gong':int(character[1]), 'bang':int(character[2])}
    monster_dict = defaultdict(list)

    for monster in monsters:
        name, point, m_hp, m_gong, m_bang = monster.split()
        point, m_hp, m_gong, m_bang = int(point), int(m_hp), int(m_gong), int(m_bang)
        win, count = fight(monster, character_dict)

        if win == True:
            monster_dict[name] = [point/count, point]

    print(monster_dict)
    # res = sorted(monster_dict.items(), key = lambda x:(x[0], x[1]))
    # return res[0][0]


print(solution(
"10 5 2", ["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"]
))