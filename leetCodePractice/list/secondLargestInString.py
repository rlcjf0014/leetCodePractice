class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers= []
        for letter in s:
             if letter.isdigit():
                    target = int(letter)
                    if target not in numbers:
                        numbers.append(target)
        numbers.sort(reverse=True)
        return numbers[1] if len(numbers) > 1 else -1