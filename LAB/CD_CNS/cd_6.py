g = {'S': 'ABC', 'A': ['abA', 'ab'], 'B': ['b', 'BC'], 'C': ['c', 'cC']}
# G = (V,T,P,S)
G = (('S', 'A', 'B', 'C'), ('a', 'b', 'c', '$'), g, 'S')

Items = 11

pt_action = {
    (0, 'a'): 'S3',
    (1, '$'): 'ACC',
    (2, 'b'): 'S4',
    (3, 'b'): 'S6',
    (4, 'c'): 'R4',
    (5, 'c'): 'S8',
    (6, 'a'): 'S3',
    (6, 'b'): 'R3',
    (7, 'c'): 'R5',
    (7, '$'): 'R1',
    (8, 'c'): 'S8',
    (8, '$'): 'R6',
    (9, 'c'): 'R7',
    (9, '$'): 'R7',
    (10, 'b'): 'R2'
}
pt_goto = {
    (0, 'S'): 1,
    (0, 'A'): 2,
    (2, 'B'): 5,
    (5, 'C'): 7,
    (6, 'A'): 10,
    (8, 'C'): 9
}

R = {
    'R1': ['S', 'ABC'],
    'R2': ['A', 'abA'],
    'R3': ['A', 'ab'],
    'R4': ['B', 'b'],
    'R5': ['B', 'BC'],
    'R6': ['C', 'c'],
    'R7': ['C', 'cC']
}


def SRParser(s: str):
    s = s + '$'
    stack = ['$', 0]
    sptr = 0
    print('STACK\t\t\tISUT\t\t\tACTION')
    while(stack[-1] != 'ACC' or sptr < len(s)):
        if stack[-1] in range(Items):
            if s[sptr] in G[1]:
                if (stack[-1], s[sptr]) not in pt_action:
                    break
                act = pt_action[(stack[-1], s[sptr])]
                if 'S' in act:
                    stack.append(s[sptr])
                    stack.append(int(act[1]))
                    sptr += 1
                    print(f'{stack}    \t\t{s[sptr:]}    \t\tSHIFT {act}')
                elif 'R' in act:
                    red_move = R[act]
                    popnum = len(red_move[1]) * 2
                    for i in range(popnum):
                        stack.pop()
                    stack.append(red_move[0])
                    print(f'{stack}    \t\t{s[sptr:]}    \t\tREDUCE {act}')
                elif 'ACC' in act:
                    popnum = 2 * 2
                    for i in range(popnum):
                        stack.pop()
                    stack.append('ACC')
                    print(f'{stack}    \t\t{s[sptr:]}    \t\tACCEPT {act}')
                else:
                    break
        elif stack[-1] in G[0]:
            stack.append(pt_goto[(stack[-2], stack[-1])])
            print(f'{stack}    \t\t{s[sptr:]}    \t\tGOTO {stack[-1]}')
        else:
            break
    if stack[0] == 'ACC':
        return "Accepted"
    return "Rejected"


SRParser('abbc'),SRParser('abbbcc')
#SRParser('abbcc'),SRParser('ababbcc')
