class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = list(zip(heights, names))
        paired.sort(reverse=True)
        return [name for height, name in paired]
