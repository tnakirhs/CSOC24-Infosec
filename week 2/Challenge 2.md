# Challenge 2

<pre>
A <a href = "https://github.com/JustAnAverageGuy/literate-octo-fiesta/blob/main/challenge_2/encoded.txt">text file</a> with wierd text is given.

On inspection it looks like that the text is composed of - <i>binary</i>     -  <b>01000011 01010011 01001111 01000011 00110010</b>
                                                           <i>hex string</i> -  <b>33 7b 6a 75 35 37 5f</b>
                                                           <i>Base64</i>     -  <b>ZDFmZjNyM243XzNuYw==</b>
                                                           <i>ASCII</i>      -  <b>60 144 61 156 66 65 137 154 60 154 175</b>

When converted it can be found that <mark><b>60 144 61 156 66 65 137 154 60 154 175</b></mark> are not ASCII values.
Using Cyberchef, it can be found that the numbers are infact octal numbers.
</pre>

<pre>
#The given python script decodes the text

f = l = a = g = ""

for i in [0b1000011, 0b01010011, 0b01001111, 0b01000011, 0b00110010]:
  f += chr(i)

l = bytes.fromhex("337b6a7535375f").decode()

from base64 import *
a = b64decode("ZDFmZjNyM243XzNuYw==").decode()

g = ''.join(chr(int(str(i), 8)) for i in [60, 144, 61, 156, 66, 65, 137, 154, 60, 154, 175])

print(f+l+a+g)

#The output is the flag <i>CSOC23{ju57_d1ff3r3n7_3nc0d1n65_l0l}</i>
</pre>
