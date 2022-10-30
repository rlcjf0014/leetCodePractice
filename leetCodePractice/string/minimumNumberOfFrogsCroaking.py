class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        next_letter = {
            'c' : 'r',
            'r' : 'o',
            'o' : 'a', 
            'a' : 'k',
            'k' : 'f'
        }
        
        count = {
            'c' : 0,
            'r' : 0,
            'o' : 0,
            'a' : 0,
            'k' : 0,
            'f' : 0
        }
        
        for letter in croakOfFrogs:
            if letter != 'c' and count[letter] < 1:
                return -1
            if letter == 'c' and count['f'] > 0:
                count['f'] -= 1

            count[letter] -= 1
            count[next_letter[letter]] += 1
        
        for check in ['r', 'o', 'a', 'k']:
            if count[check] != 0:
                return -1 
            
        return count['f']

        