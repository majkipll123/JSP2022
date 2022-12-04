def czysamo(word):
    """czy samogloska czy spolgloska"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)
   

a=input()
print(czysamo(a))
