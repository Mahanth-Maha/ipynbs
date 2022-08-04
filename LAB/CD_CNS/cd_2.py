class DFA:
    def __init__(self,Q,S,D,q0,F) -> None:
        self.Q = Q
        self.S = S # Sigma - Alphabets
        self.D = D # Delta 
        self.s = q0
        self.F = F
    
    def check(self,inp):
        if inp == '' and self.s == 0 :
            return 'ACCEPTED'
        state = self.s
        for i in inp:
            if i not in self.S:
                return 'Rejected - Not an Alphabet'
            state = self.D[(state,i)]
        if state in self.F:
            return 'ACCEPTED'
        return 'Rejected - Not in Language'

class NFA(DFA):

    def check(self,inp):
        if inp == '' and self.s == 0 :
            return 'ACCEPTED'
        state = [self.s]
        for i in inp:
            if i not in self.S:
                return 'Rejected - Not an Alphabet'
            newstate = []
            for j in state:
                if (j,i) in self.D:
                    tempstate = self.D[(j,i)]
                    for k in tempstate:
                        newstate.append(k)
            state = list(set(newstate))
        for s in state:
            if s in self.F:
                return 'ACCEPTED'
        return 'Rejected - Not in Language'


dfa = DFA(3,('a','b'),{(0,'a'):1,(0,'b'):0,(1,'a'):2,(1,'b'):1,(2,'a'):0,(2,'b'):2},0,{0})
dfa.check('aababaaab')
dfa.check('aabbaa')

nfa = NFA(2,('a','b'),{(0,'a'):[1],(1,'b'):[0]},0,{1})
nfa.check('abababa')
nfa.check('abab')