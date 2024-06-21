<a href = "https://cryptohack.org/challenges/">**Cryptohack Challenges**</a>   
<br>  

# Introduction  

*A. Finding Flags*
<pre>
<i>crypto{y0ur_f1rst_fl4g}</i>
</pre>

*B. Great Snakes*
<pre>
A <a href = "https://cryptohack.org/static/challenges/great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py">python file</a> is given which when executed gives the flag <i>crypto{z3n_0f_pyth0n}.</i>
</pre>

*C. Network Attacks*
<pre>
It is given to send a JSON object with the key <i><b>buy</b></i> and value <i><b>flag</b></i> on <b>socket.cryptohack.org</b> on port <b>11112</b>.
Using <b>nc socket.cryptohack.org 11112</b> and entering <i><b>{"buy":"flag"}</i></b> returns a JSON revealing the flag 
<i>crypto{sh0pp1ng_f0r_fl4g5}</i>.
</pre>

<pre>
It can also be done by modifying the given <a href = "https://cryptohack.org/static/challenges/pwntools_example_72a60ff13df200692898bb14a316ee0b.py">python file</a>, change <b>line 27</b> from <i><b>"buy": "clothes"</i></b> to <i><b>"buy": "flag"</i></b>.
</pre>

<pre>
#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

request = {
    "buy": "flag"
}
json_send(request)

response = json_recv()

print(response)
</pre>

<br>

# General    

<code>- Encoding</code>   

*A. ASCII*
<pre>
A list <mark>[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]</mark> is given.
The numbers need to be converted to their corresponding ASCII characters to obtain a flag.
</pre>

<pre>
# This can be done by the given python script.

l = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag = ""
for i in l:
    flag = flag+chr(i)
print(flag)

#revealing the flag <i>crypto{ASCII_pr1nt4bl3}</i></pre>

*B. Hex*
<pre>
A hex string <mark><i>63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d</i></mark>
is given which needs to be converted into string.</pre>

<pre>
# This can be done by the given python script. 

hst = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

print(bytes.fromhex(st).decode())

#revealing the flag <i>crypto{You_will_be_working_with_hex_strings_a_lot}</i></pre>

*C. Base64*
<pre>A hex string <mark><i>72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf</i></mark> is given which needs to be decoded 
into bytes and then encoded into Base64.</pre>
<pre>
# This can be done by the given python script.

import base64
hst = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byt = bytes.fromhex(hst)
print(base64.b64encode(byt).decode())

#revealing the flag <i>crypto/Base+64+Encoding+is+Web+Safe/</i></pre>

*D. Bytes and Big Integers*
<pre>
Given is a long integer <mark><i>11515195063862318899931685488813747395775516287289682636499965282714637259206269</i></mark><br>It needs to be converted into string.
It can be done by <i><b>long_to_bytes()</i></b> function from <i><b>pycryptodome</i></b>.
</pre>

<pre>
# This can be done by the given python script.

from Crypto.Util.number import *
li = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(li).decode())

#revealing the flag <i>crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}</i>
</pre>

<br>

<code>- XOR</code>

*A. XOR Starter*
<pre>
A string <i><b>label</b></i> is given whose each character is to be XOR with the integer <b>13</b>.
First convert both 'label' and 13 into binary and then XOR and convert back to string.
</pre> 
<pre>
# This can be done by the given python script.

binlabel = []
for i in "label":
    binlabel.append(bin(ord(i))[2::])
bin13 = "0001101"
result = []
for i in binlabel:
    xr = ""
    for j in range(len(i)):
        if i[j] == bin13[j]:
            xr  = xr + "0"
        else:
            xr  = xr + "1"
    result.append(xr)
for i in result:
    print(chr(int(i, 2)),end = "")

#The flag is <i>crypto{aloha}</i>
</pre>

*B. XOR Properties*
<pre>
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
</pre>
<pre>
We are given a hex string KEY1 which is XOR with KEY2 to give another hex string. We can find KEY2 by XOR between 
KEY1 and given hex string. Then hex string obtained by XOR between KEY2 and KEY3 is given, KEY3 can be obtained 
similarly. Another hex string is given by XOR between <i>FLAG</i>, KEY1, KEY2, KEY3. <i>FLAG</i> can be obtained by XOR between 
the given hex string, KEY1, KEY2 and KEY3 and then converting the output hex string into bytes. All hex strings 
need to be converted into bytes to use <b>xor()</b> function or integer to use (^). 
</pre>
<pre>
#The given python code can do this

from Crypto.Util.number import *

KEY1 = int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313",16)
XK12 = int("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e",16)

KEY2 = (KEY1 ^ XK12)

XK23 = int("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1",16)

KEY3 = (KEY2 ^ XK23)

XKF132 = int("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf",16)

FLAG = (KEY1 ^ KEY2 ^ KEY3 ^ XKF132)

print(long_to_bytes(FLAG).decode())

#It gives the flag <i>crypto{x0r_i5_ass0c1at1v3}</i>
</pre>


