import sys

# reads a text file     
# returns a list of tokens 
def tokenize(TextFilePath):
# Time: O(n), n is the number of characters in the file. Each character is
# visited exactly once and appending to a list is O(1).
# Space: O(t), where t is the number of tokens stored in the list
    token_list = []
    with open(TextFilePath, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            current = ""

            for character in line: 
                if character.isalnum():
                    current += character.lower()
                else:
                    if current: 
                        token_list.append(current)
                        current = ""

            if current:
                token_list.append(current)

    return token_list
            

def Map<Token,Count> computeWordFrequencies(List<Token>):
# takes a list of tokens 
# counts how many tokens in the list
# returns a dict (token, count)

def void print(Frequencies<Token, Count>)
