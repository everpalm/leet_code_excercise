'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
  //... your code
  return strs;
}
 

So Machine 1 does:

string encoded_string = encode(strs);
 

and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
 

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
'''
def encode(strs):
    encoded_string = ''
    for s in strs:
        encoded_string += str(len(s)) + '#' + s
    return encoded_string

def decode(s):
    strs = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j]) #s[i:j] is the characters representing the integer number
        i = j + 1
        strs.append(s[i:i+length])
        i += length
    return strs

# Example encode and decode usage:
strs = ["Hello", "world", "this#is#an#example", "including, punctuation! and#symbols#like#%"]
encoded = encode(strs)
print("Encoded:", encoded)
decoded = decode(encoded)
print("Decoded:", decoded)

# Ensure the decoding matches the original list of strings
if decoded == strs:
    print('PASS')
else:
    print("Decoded list does not match the original")
