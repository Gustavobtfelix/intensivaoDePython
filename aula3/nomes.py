import unidecode 
string = "orčpžsíáýd"
print('\nOriginal String:', string) 
outputString = unidecode.unidecode(string) 
print('\nNew String:', outputString)