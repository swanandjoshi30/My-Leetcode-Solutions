class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Args:
            s (str): The input sentence.
            k (int): The number of words to keep.

        Returns:
            str: The truncated sentence containing the first 'k' words.
        """
        # Split the sentence into words, then join the first 'k' words
        return " ".join(s.split(" ")[:k])
