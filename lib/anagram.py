class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
      
        def is_anagram(w1, w2):
            return sorted(w1.lower()) == sorted(w2.lower())

        
        return [word for word in word_list if is_anagram(self.word, word) and self.word.lower() != word.lower()]
