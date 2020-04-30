

def palindrome(word):
    if word ==  word[::-1]:
        return True
    else:
        return False


a = "My NmN is sandeep"


words = a.split()

for word in words:
    if palindrome(word):
        palin = word
        break

print(palin)
    
