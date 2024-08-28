def Anagram(string,dup):
    sorted(string.lower())
    string = string[::-1]
    print(f"After sorting the string {string}")
    if (string == dup):
        return "Anagram"
    return "Not Anagram"
string = input("Enter the  anagram String : ")
dup   = string[::]
Anagram(string,dup)
    
