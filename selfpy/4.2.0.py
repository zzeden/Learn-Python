word = input()
moko = word.replace(" ","")
WORD = moko.lower()
jojo = WORD[::-1]
if(jojo == WORD):
    print("OK")
else:
    print("NOT")