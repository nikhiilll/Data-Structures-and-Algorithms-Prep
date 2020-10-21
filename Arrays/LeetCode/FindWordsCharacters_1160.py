def countCharacters(words, chars):

    result_length = 0
    chars_freq = [0] * 26

    for c in chars:
        chars_freq[ord(c) - ord('a')] += 1
    
    for word in words:
        word_freq = [0] * 26

        for w in word:
            word_freq[ord(w) - ord('a')] += 1

        for i in range(26):
            if word_freq[i] > chars_freq[i]:
                break
        
        else:
            result_length += len(word)
    
    return result_length

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(countCharacters(words, chars))            


"""
def countCharacters(self, words: List[str], chars: str) -> int:
        sum, chars_counter = 0, collections.Counter(chars)
        for word in words:
            word_counter = collections.Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                sum += len(word)
        return sum



"""
