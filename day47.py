#Check anagram
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# Example usage
word1 = "listen"
word2 = "silent"
print(f"Are '{word1}' and '{word2}' anagrams? {are_anagrams(word1, word2)}")
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(f"Are '{word1}' and '{word2}' anagrams? {are_anagrams(word1, word2)}")