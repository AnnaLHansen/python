"""
Introduktion til Python.
Scriptet kan afvikles fra terminalen med:
  python3 ~/python_intro.py

"""

"""
Der findes i Python forskellige datatypes. 
Integer, floats (real numbers), strings og booleans

Man kan konvertere datatyper om til andre datatyper med de
indbyggede funktioner float, int og str.
Hvis man konvertere en float til en integer, vil man midste information
der ligger i decimal tallene. Her vil den se helt bort fra decimaltallene.
(Der bliver ikke rundet op eller ned).

int(True) giver 1, mens int(False) giver 0. 
bool(1) giver True, mens bool(0) giver False.

"""

print(type(0))
print(type(11))
print(type(11.5))
print(type(""))
print(type(True))

print(type(int(11.9)))
print(int(11.9))
print(type(float(11)))
print(type(str(11)))


"""
Ligesom i R, kan man lave simple matematiske operationer. 
Ligesom i R, kan man også gemme værdier inde i variable og bruge
variablene til at lave matematiske operationer med.

Når man dividere to integers resulterer de altid i en float, også
selvom tallet er et hel tal.
De øvrige operatorer som plus, minus og gange resultere i integers.
"""

x = 10
print(x)
y = 5
print(y)
z = x + y
print(z)

print(x/y)
print(type(x))
print(type(y))
print(type(x+y))
print(type(x/y))
print(type(x*y))

"""
Strings kan være bogstaver, tal symboler og mellemrum. 
Med strings kan man udtage enkelt elementer fra strengen, og man kan 
også kombinere strings eller gange en string, som resultere strengen som 
bliver gentaget flere gange. 
Strings er immutable, men man kan godt tilføje noget til en string med +.

Metoder kan anvendes på strings. Metoder anvendes ved at angive variablen efterfulgt
af metoden. eksmeplevis variabel.upper

Metoder angiver at man skal gøre noget bestemt (hvad end metoden er) og anvende
det på den variabel man har givet som input. 

"""

print("Anna Hansen"*3)
print(len("Anna Hansen"))
print("Anna Hansen \ er den bedste")
print("Anna Hansen \n er den bedste")
print("Anna Hansen \t er den bedste")
print(r"Anna Hansen \t er den bedste")
var = "Anna Hansen"
print(var)
var = "hej " + var
print(var)

A = "Hej hej"
B = A.upper()
print(A)
print(B)
C = A.replace('hej', "Anna")
print(C)
D = C.find("Anna")
print(D)


"""
List and tuples
List og Tuples er nogle af de vigtige datatyper i Python.
Tuples er defineret som elementer inden i en parantes, og det samlede
element har typen 'tuples'. De enkelte elementer inde i en tuple er str, int, ell
float, og en tuple kan sagtens indeholde flere forskellige element typer.
Hvert element inde i en tuple kan tilgåes via elementets index. Lidt ligesom i en 
string, bortset fra at hele streng elementet i en tuple er et index.

"""
tupel_test = (1, 2, 3.0, "hej")
print(tupel_test)
print(type(tupel_test))
print(tupel_test[3])

