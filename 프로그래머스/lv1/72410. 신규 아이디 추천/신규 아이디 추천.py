def solution(new_id):
    new_id = list(new_id.lower())
    print(new_id)
    for i in range(len(new_id)):
        if new_id[i].isalpha() == True: continue
        elif new_id[i].isdecimal() == True: continue
        elif new_id[i] in ['-','_','.'] : continue
        else: new_id[i] = ''
    print(''.join(new_id))
    new_id = ''.join(new_id)
    while True:
        if '..' in new_id:
            new_id = new_id.replace('..', '.')
        else: break
    print(new_id)
    new_id = list(new_id)
    print(new_id)
    if new_id[0] == '.':
        new_id.pop(0)

    if new_id != [] and new_id[-1] == '.':
        new_id.pop()

    
    if new_id == []:
        new_id = ['a']

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop()
    print(new_id)      
    if len(new_id) <= 2:
        while True:
            if len(new_id) == 3: break
            new_id.append(new_id[-1])
            
    return ''.join(new_id)