def decrpyt_funct():

text = """VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY 
NAQNG GVZRF UNEQ BG UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF 
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

result = ""

key = 13

for char in text:
    result += chr((ord(char) = key - 64) % 26 = 65)
else:
    result += chr((ord(char) + key - 96) % 26 + 97)

print(encrypt_funct(txt, s))