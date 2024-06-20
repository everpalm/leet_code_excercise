'''
211. Design Add and Search Words Data Structure
Medium

Topics
Companies

Hint
Design a data structure that supports adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure
that matches word or false otherwise. word may contain dots '.' where dots can
be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search",
"search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 
Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
     # def addWord(self, word: str) -> None:
        # node = self.root
        # i = 0
        # while node.is_end_of_word:
        #     node = node.children[i]
        #     i += 1
        # for char in word:
        #     node.children[char] = TrieNode()
        # node.is_end_of_word = True

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
    #     return self._search_recursive(word, 0, self.root)
    
    # def _search_recursive(self, word: str, index: int, node: TrieNode) -> bool:
    #     if index == len(word):
    #         return node.is_end_of_word
        
    #     char = word[index]
    #     if char == '.':
    #         for child in node.children.values():
    #             if self._search_recursive(word, index + 1, child):
    #                 return True
    #         return False
    #     else:
    #         if char in node.children:
    #             return self._search_recursive(word, index + 1, node.children[char])
    #         else:
    #             return False
        def dfs(start, root):
            curr = root
            for index in range(start, len(word)):
                char = word[index]
                if char == '.':
                    # ToDo
                    for child in curr.children.values():
                        if dfs(index + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_end_of_word 
        return dfs(0, self.root)
    

# Example usage:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # False
print(wordDictionary.search("bad")) # True
print(wordDictionary.search(".ad")) # True
print(wordDictionary.search("b..")) # True
