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
Man kan også lægge to tuples sammen med +

Tuples er immutable hvilket er en vigtig egenskab. Man kan kun manipulere en 
tupel ved at assigne sin tupel til en ny variabel.
En tupel kan også indeholde nestede tupels. Man kan tilgå de nestede tupels med
firkantede brackets (ligesom i R). 

List er på mange måde ligesom tupels, bortset fra at de er mutabels. 
Slicing foregår på samme måde som tuples.
For lister kan man også tilføje elementer til en allerede eksisterende liste med 
+ operatoren.
Man kan ligesom med tupels, godt have lister med nestede lister i.
For at tilføje en nested liste til en liste kan man bruge .append
metoden.

Der findes også en metode som spliter en string til en liste. .split
hvis man ikke giver metoden et split-argument, tager den 
pr default mellemrum som split-argument.

Når man har to variable som henviser til samme liste, vil man ændre 
begge variable når man ændrer listen. 


"""
tupel_test = (1, 2, 3.0, "hej")
print(tupel_test)
print(type(tupel_test))
print(tupel_test[3])
tupel_test2 = tupel_test + ("Anna", 3, 1)
# tupel_test2.extend(("pop"))    virker ikke fordi immutable
# tupel_test2[0] = 2    virker heller ikke fordi immutable
print(tupel_test2)

liste_test = [1, 2, 3.0, "hej"]
print(liste_test)
print(type(liste_test))
print(liste_test[3])
liste_test.extend(["pop"])
liste_test.extend("pop")
liste_test.append(["popper", 10])
print(liste_test)
print(liste_test[8])
liste_test[0] = "heheheh"
print(liste_test)
del(liste_test[0]) # Fjerner element i liste
print(liste_test)
B=[1,2,[3,'a'],[4,'b']]
print(B[3])

"""
Dictonaries i Python
Både dictonaries og sets er collections i python.
En dictonary minder om en liste, men indeholder 
keys og values.

En dictonary kan assignes til en variabel og herfra kan man referere til
værdien i dictonary ved at henvise til nøglen.

"""
opslag = {"key1": "hej", "key2": (1,2)}
print(opslag)
print(opslag["key1"])
print("key1" in opslag)
print("key3" in opslag)
print(opslag.keys())
print(opslag.values())


"""
Sets i Python
Både dictonaries og sets er collections i python.

sets har kun unikke elementer. 
Når man definerer et set, vil duplikater forsvinde ved dannelsen af settet.
Et set kan derfor pr definition ikke indeholde dupletter.

Man kan også konvertere en liste til et set med funktionen set()

ligesom med dictonaries kan man også bruge "in" operatoren for at finde ud af
om en værdi findes i et set.

intersection af to sets kan findes med operatoren &.

"""

set1 = {"hej", "hej", "heeej", "hallo"}
print(set1)
set2 ={"nej", "no", "hallo"}
print(set2)
set3 = set1 & set2
print(set3)


"""
Conditions and branching i python
Man kan sammenligne værdier med følgende:

==
!=
<
>
=>
=<

Man kan også sammenligne strings med hinanden.
Ud over de almindelige større end og lig med operatorer
er der også indbyggede funktioner i python som 
"or", "not", "and"

"""
a=5
print(a==6)

if(a>5):
  print("a er stoerre end 5")
elif(a==5):
  print("a er lig med 5")
else:
  print("a er ikke stoerre end 5")
print("nu er mit if statement færdigt")

print(not(False))
print(False or True)

if(a>5 or a<5):
  print("a er ikke lige med 5")
elif(a==5):
  print("a er lig med 5")

"""
Loops i python
I loops kan man bruge range() funktionen. 
While loops minder om for-loops, men bliver kun kørt
så længe betingelsen er opfyldt.

"""
firkant = ["1", "2", "3", "4", "5"]
print(firkant)

for i in firkant:
  print(i)

for i in range(0,5):
  firkant[i] = "hej"

print(firkant)

for i,firkant in enumerate(firkant):
  print(i)
  print(firkant)

print(firkant)


firkant = ["green", "green", "yellow"]
i = 0
while(firkant[i]=='green'):
  print("uhhhhh")
  i = i+1



"""
Funktioner i python
Der er både indbyggede funtkioner i python og i forsxkellige python 
pakker, men man kan også bygge sine egne pakker.

Et eksempel på en indbygget funktion er funktionen 'len()'

Sorted() er et eksempel på en funktion som outputter en liste med sorteret input.
Det sortede input kan blive skrevet til en ny variabel, men i sig selv ændrer
den ikke ved den oprindelige liste. 
Hvis man vil ændre den oprindelige liste kan man bruge metoden .sort i stedet.

En funktion i python bliver defineret således:

def funktionensnavn(inputvariabel):
  selve funktionens indhold
  return(det som skal returneres)


Man kan tilgå funktionsdokumentationen med help(add1)
For at komme ud af dokumentationen igen trykker med q

Variable som bliver defineret uden for en funktion ligger i 
'global scope'. Alle variable som ligger i 'global scope' er globale variable.
Det er kun de returnerede værdier som bliver returneret til det globale scope.
De variable som bliver defineret inde i en funktion men som ikke returneres, 
eksisterer kun der. 
Hvis en variabel ikke bliver defineret inde i funktion vil python automatisk
tjekke det globale scope og bruge funktionen der hvis den findes.
Man kan inde i en funktion henvise til en global variable med 

'global variablen' inde i selve funktionen. Her tager man bevidst den globale 
variabel.

"""

print(len([1,2,3,4]))
print(sum([1,2,3]))
print(sorted([2, 1, 5,4]))

a = [2, 1, 5,4]
print(a)
a.sort()
print(a)


def add1(a,b):
  """
  Dette er funktionsdokumentationen til denne 
  helt igennem fantastiske funktion som lægger 1 oveni 
  input.
  """
  c = a + b
  return c

print(add1(2, 4))

"""
Exception Handling i Python

Exception handling gør en funktion i stand til at håndtere at
den modtager et forkert input.
Det kan f.eks. være at input er af en forkert type. 

Exeption handling kan også være at tilføje nyttige print statements undervejs
for at gøre opmærksom på hvad der er gået galt og dermed gøre debugging nemmere.
"""

"""
Objects and classes i python
Hver datatype i python er et object som har en type.

Når man laver en liste i python laver man et liste object. 
Som man med type() kan se typen.
Metoder kan anvendes på objektet og gør noget bestemt ved objektet.

(Er det rigtigt at en metode opfører sig forskelligt afhængig af typen??)

Man kan også lave dine egne type (klasser)

Init funktionen er en speciel funktion i python, som fortæller python
at man er i gang med at lave en ny klasse.

Methods hører til en class, og er metoder som kan bruges på objekter med 
den specifikke type. 

"""

class Cirkel(object):
  
  def __init__(self, radius, color):
    self.radius =  radius;
    self.color = color;
  
  def add_radius(self, r):
    self.radius =  self.radiues + r


RedCirkel = Cirkel(10, "red")
RedCirkel.color = "blue"
RedCirkel.add_radius = 4

print(dir(RedCirkel))

"""
Læs filer med Python
med 'open' function. 
Funktionen kan kaldes med bl.a. "r" for reading, og "w" for writing.

med metoden 'name' kan man trække alle attributterne ud af filen.
og herefter bruge 'close' til at lukke filen igen, så man ikke længere læser fra den.

Med open og close laver man en connection til filen man enten gerne vil læse eller
skrive til. 
Med metoden read, kan man indlæse filen med den åbne connection. 

Når man er færdig med at bruge forbindelsen, kan man lukke den med .close()

Med .readlines metoden kan man læse specifikke elementer fra den åbne fil.
"""
# file1 = open("(home1/W22009/test.json", "r") 
# file1.name
# file1.close()

file1=open("/home1/W22009/python/testfil.txt", "r")
file2=file1.read()

file3=file1.readlines(2)
file4=file1.readlines(0)
print(file2)
print(file3)
print(file4)
file1.close()

"""
Skriv til filer med Python
med 'open' function.
Med metoden .write til en åben fil kan man tilføje indhold til filen.

"""
file1=open("/home1/W22009/python/testfil.txt", "w")
file1.write("This is line A\n")
file1.write("hehehe det her er linje 2")
file1.close()


"""
Loading data with Pandas i Python
I python kan man bruge forskellige biblioteker /libraries.
pandas indeholder således en funktion til at læse csv filer.

Med import kan man importerer et library. 'as' under import giver muligheden for 
at importerer pandas library under et valgfrit navn. Eksemplet herunder 
importerer det som "banana".

pandas pakken indeholder også en head metode, så man kan se toppen af sit dataframe.

.DataFrame metoden fungerer ligesom data.frame() i R. Den konverterer input til et
dataframe.

dataframe[['attribut']] tager den valgte attritbut ud af det valgte dataframe.
Hvis det assignes til et nyt objekt vil dette stadig være en dataframe blot med
en enkelt variabel.

"""
# import pandas as banana
# 
# csv_path = "/home1/W22009/python/testfil.txt"
# dataframe = banana.read_csv(csv_path)
# dataframe.head()

# banana.DataFrame(tuppel)
# ny_dataframe = dataframe[['artist']] 

"""
Working with and saving data with pandas
df['Released'].unique()
df['Released']>=1980
df2=df[df['Released'] >=1980]
df2.to_csv('new_songs.csv')
"""

"""
Numpy in python
Numpy arrays minder om en liste.

Numpy arrays med en dimenssion er vektorer. Numpy pakken
indeholder en masse forskellige metoder til at foretage hurtigt
vektor regning.

Numpy arrays er hurtigere end almindelig python
kode. De universelle funktioner som eks. mean
fungerer også på et numpy array. 
"""

import numpy as np
a=np.array([0,1,2,3,4])
print(type(a))
print(a.size)
print(a.ndim)
print(a.shape)

# Beregninger i numpy er hurtigere end base-python
# Herunder er et eksempel på hvordan man kan lægge 
# de to vektorer sammen med numpy notation.
u=np.array([1,0])
v=np.array([0,1])
z=u+v
# z:array([1,1])

"""
Numpy arrays med to dimenssioner

arrays med to dimenssioner virker på sammen 
måde som en matix og kan lægges sammen 
på samme måde.
"""

a=[[11,12,13], [21,22,23], [31,32,33]]
a.shape # (3,3)
a.ndim # 2
a.size # 9
a[0,0] # 11


"""
API (Apllication program interface)
Hvad er API's, API libraries, REST API

Et API lader to componenter snakke med hinanden.
Man skal bare vide et API's input og output.

Hos REST API'er hedder ens eget program 'client'. Klienten 
sender requests til 'resource' (også kaldet end point) og
sender et svar tilbage til klienten igen.

Resource kan eksempelvis være en webservice.
Data som gives frem og tilbage vil typisk være en json fil.

Data kan også være en lydfil. Et eksempel kan være klienten som 
sender en lydfil til API'et. API'et returnerer den transkriberede tekst.
Den transkriberede fil kan herefter blive sendt til et andet API
som oversætter teksten til et andet sprog.

For at få adgang til et API skal man give API'et en key (Er nogle
APIer helt åbne?)


"""

# import requests
# url='https://www.ibm.com/'
# r=requests.get(url)
# 
# r.status_code # 200 hvis ok
# r.header 
# r.encoding
# 
# 
# url_get = 'http://httpbin.org/get'
# payload={"name": "Joseph", "ID": "123"}
# r=requests.get(url_get, params=payload)
# r.url # Pinter urlen
# r.json # Viser json 
# 
# url_post = 'http://httpbin.org/post'
# payload={"name": "Joseph", "ID": "123"}
# r_post = requests.post(url_post, data=payload)

"""
HTML for WEB scraping
For at kunne udtrække data fra en hjemmeside skal man forstå
opbygningen af en html. 

1) import request og BeautifulSoup pakkerne.
2) request.get kan hente html objektet
3) Med beautifulsoup funktionen kan man lave et beautifulsoup
objekt, som man kan bruge til at trække de ønskede elementer ud,
4) Eksempelvis med soup.find_all("a") Finder alle instancer med HTML tagget
"<a>"

"""

# from bs4 import BeautifulSoup
# html= "indsæt her en html kode"
# 
# soup = BeautifulSoup(html, 'html5lib')
# tag_object = soup.h3
# # Man kan her navigerer rundt i html træet.
# 
# table = BeautifulSoup(html, 'html5lib')
# table_row=table.find.all(name='tr')
# table_row[0] # Første række


"""
Working with different file formats in Python
CSV, XML, JSON

Pandas pakken gør det nemt at indlæse forskellige filtyper
pd.read_csv 
json.load

XML filer er lidt mere komplicerede fordi der ikke findes en metode
til at indlæse xml filer med pandas
"""


