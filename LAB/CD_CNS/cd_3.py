class DPDA:
    
    def __init__(self, trf, input, state):
        
        self.head = 0
        self.trf = {}
        self.state = str(state)
        self.input = input
        self.trf = trf
        self.stack = ['Z']
        
    def step(self):
        
        a = self.input[self.head]
        s = self.stack.pop()
        state, ss = self.trf.get((self.state, a, s))
        if ss != 'ε':
            for s in ss[::-1]:
                self.stack.append(s)
        self.state = state
        print('{:20s} [{:10s}] {:5s}'.format(self.input[self.head:], 
                       ''.join(self.stack), self.state))        
        self.head += 1
    
    def run(self):
        
        print('{:20s} [{:10s}] {:5s}'.format(self.input[self.head:], 
                              ''.join(self.stack), self.state))
        
        while self.head  < len(self.input):
            self.step()

        s = self.stack.pop()        
        if self.trf.get((self.state, 'ε', s)):
            state, ss = self.trf.get((self.state, 'ε', s))
            self.state = state        
            print('{:20s} [{:10s}] {:5s}'.format('ε', 
                 ''.join(self.stack), self.state))
        if self.state == 'acc':
            return "Accepted"
        return "Rejected"
        
# run DPDA to accept the input string a^9b^9
DPDA({('q', 'a', 'Z'): ('q', 'XZ'),
     ('q', 'a', 'X'): ('q', 'XX'),
     ('q', 'b', 'X'): ('p', 'ε'),
     ('p', 'b', 'X'): ('p', 'ε'),
     ('p', 'ε', 'Z'): ('acc', 'Z'),
    }, 
    'aaaaabbbbb', 'q').run()