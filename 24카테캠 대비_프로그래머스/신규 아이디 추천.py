import re

def solution(new_id):
    new_id = new_id.lower() #1단계
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    while '..' in new_id:
        new_id = new_id.replace('..', '.')#3단계
    if new_id[0] == "." or new_id[-1] == ".":
        if new_id[0] == ".":
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
        while new_id[-1] == ".":
            new_id = new_id[:-1]
    while (len(new_id) < 3):
        new_id = new_id + new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"