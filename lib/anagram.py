# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word =word.lower()
        self.word_sorted = sorted(self.word)
    def match(self,word_list):
        anagrams = []
        for word in word_list:
            if self.word_sorted == sorted(word.lower()) and self.word != word.lower():
                anagrams.append(word)
        return anagrams
# Example usage:
anagram = Anagram("listen")
print(anagram.match(["enlist", "google", "inlets", "banana"]))
# Output: ['enlist', 'inlets']