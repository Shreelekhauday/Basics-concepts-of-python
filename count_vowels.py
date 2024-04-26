def count_vowels(string):
    vowels = "a,e,i,o.,u,A,E,I,O,U"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
string=input('enter  string:')
print(count_vowels(string))




    