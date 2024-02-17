def palindrome(text) :
    lenght = len(text)
    for i in range (0, lenght//2):
        if text[i] != text[lenght -i -1]:
            return "Kalimat Bukan Palindrome"
        return "Kalimat Palindrome"

print(palindrome("kasur rusak"))
