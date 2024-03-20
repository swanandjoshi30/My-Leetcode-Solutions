class Solution:
    def reverseWords(self, s: str) -> str:
        b = s.split(" ")
        lst = []
        for word in b:
            lst.append(word[::-1])
        c = ' '.join(lst)
        return c
