class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        start = True
        
        for digit in digits:
            if start:
                self.results = self.d[digit]
                start = False
            else:
                self.results = self.appendDigitLettersToAllInList(self.results, digit)
        
        return self.results

    def appendDigitLettersToAllInList(self, ls, digit):
        n = str(digit)
        tmp = []
        for s in ls:
            for letter in self.d[n]:
                tmp.append(s + letter)
        return tmp
            

    def __init__(self):
        self.d = dict()
        self.d['2'] = ['a','b','c']
        self.d['3'] = ['d','e','f']
        self.d['4'] = ['g','h','i']
        self.d['5'] = ['j','k','l']
        self.d['6'] = ['m','n','o']
        self.d['7'] = ['p','q','r', 's']
        self.d['8'] = ['t','u','v']
        self.d['9'] = ['w','x','y', 'z']
        self.results = []
        assert self.appendDigitLettersToAllInList(['a', 'b'], 3) == ['ad', 'ae', 'af', 'bd', 'be', 'bf']
        assert set(self.letterCombinations("2")) == set(['a','b','c'])
        assert set(self.letterCombinations("23")) == set(["ad", "ae", "af", 
                                                          "bd", "be", "bf", 
                                                          "cd", "ce", "cf"])
        
        