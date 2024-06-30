# Challenge 1

<pre>
A <a href = "https://github.com/JustAnAverageGuy/literate-octo-fiesta/blob/main/challenge_1/source.enc">string</a> is given which looks like Base64 due to the padding. 
</pre>
```python
#The given programs convert it into string

import base64
string = "d2l0aCBvcGVuKCdmbGFnLnR4dCcsICdyJykgYXMgZjoKICAgIGZsYWgPSBmLnJlYWQoKQoKcyA9ICcnLmpvaW4oZm9\
ybWF0KG9yZChpKSwgJzAyeCcpIGZvciBpIGluIGZsYWcpCmUgPSAiIgoKZm9yIGkgaW4gcmFuZ2UoMCxsZW4ocyksNCk6CiAgICBl\
ICs9IGZvcm1hdChpbnQoc1tpOmkrMl0sMTYpXmludChzW2k6aSs0XSwxNiksICcwMngnKQoKd2l0aCBvcGVuKCdvdXRwdXQudHh0Jy\
wgJ3cnKSBhcyBmOgogICAgZi53cml0ZShlKQ=="

print(base64.b64decode(string).decode())

#The output is a python program given below.
```

```python
with open('flag.txt', 'r') as f:
    flag = f.read()

s = ''.join(format(ord(i), '02x') for i in flag)
e = ""

for i in range(0,len(s),4):
    e += format(int(s[i:i+2],16) ^ int(s[i:i+4],16), '02x')

with open('output.txt', 'w') as f:
    f.write(e)
```

<pre>
Since <a href = "https://github.com/JustAnAverageGuy/literate-octo-fiesta/blob/main/challenge_1/output.txt">output.txt</a> is given, we can can reverse the given program. But first we need to understand it.

<b>Explaination</b>
  
  First, the program opens a file name <b>flag.txt</b> and reads it.
  Every character of file is then read and converted into its ASCII value and then converted to hexadecimal,
  all the converted characters are then concatenated to form a hex string.
  Next part looks like an encryption process,
  int(s[i:i+2],16) converts the extracted substring of length 2 from hexadecimal to an integer,
  int(s[i:i+4],16) converts the extracted substring of length 4 from hexadecimal to an integer,
  ^ is the bitwise XOR operator, which performs the XOR operation between the two integers,
  format(,'02x') converts the result back to a hexadecimal representation, padded with leading zeros if necessary.
  The result of the encryption process is then concatenated to the e variable.
  Finally, the encrypted hex string is written in a file name <b>output.txt</b>.

<b>Reversing</b>
  
  We need to follow the steps backwards to get the flag if output is given.
  In the program given below the variable <b>e</b> is the hex string from <b>output.txt</b>,
  <b>s</b> is an empty string, we use for loop to reverse the encryption process and concatenate 
  the decoded substrings of length 2 to <b>s</b>. Now the hex string <b>s</b> is converted to bytes
  using <b>bytes.fromhex()</b> function and then converted to string using <b>decode()</b>.
</pre>

```python
e = "43104f0c32017b48340179266203350636025f6b6e0a5f2730423f42"
s = ""
for i in range(0, len(e), 4):
    s += format(int(e[i:i+2], 16) ^ int(e[i:i+4], 16), '02x')

print(bytes.fromhex(s).decode())

#It gives the flag <i>CSOC23{345y_ba5364_4nd_x0r?}</i>
```
