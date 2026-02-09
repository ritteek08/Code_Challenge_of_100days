#Check pangram
def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(s.lower()) >= alphabet

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))
sentence = input("Enter a sentence: ")
print(is_pangram(sentence))