# Challenges   

<br>

## A. <a href = "https://play.picoctf.org/practice/challenge/88">Web Gauntlet</a>

<pre>
A login page is given along with a page filter.php. 
When any username and password are entered, a SQL query appears in the background of the page. 
Our aim is to take admin access for which username must be <b>admin</b>. 
This is indeed a SQL injection problem.
</pre>

* #### Round 1
  **Filter used -** ```or```    
    
  ```sql
  SELECT * FROM users WHERE username='admin' AND password='admin'
  ```     
  when username and password are **admin**.    
  
  We need the query to be    
  ```sql
  SELECT * FROM users WHERE username='admin';
  ```    
  
  For this we can enter the username as  
  ```admin'--``` or ```admin'/*``` or ```admin';```.    
  
  ```--``` and ```/*``` comments the rest of query while ```;``` ends it.

* #### Round 2
  **Filter used -** ```or and like = --```

  we can enter the username as  
  ```admin'/*``` or ```admin';``` again.    

* #### Round 3
  **Filter used -** ```or and = like > < --```     

  we can enter the username as  
  ```admin'/*``` or ```admin';``` again.
   
* #### Round 4
  **Filter used -** ```or and = like > < -- admin```

  This one is a tricky one as now the word **admin** has been filtered.
  We need to find a way so that we can enter the word **admin**.
  One way is to make **admin** as concatenation of 2 strings, let **ad**
  and **min** but i tried many combinations like ```'ad'+'min'```, using ```concat()```,
  using ```union``` but they didn't seem to work.
  Finally ```ad'||'min';``` worked which uses ```||``` as concatenation.
   
* #### Round 5
  **Filter used -** ```or and = like > < -- union admin```

  Since filter does not block the last username, it will still work.
  Enter ```ad'||'min';```     

  *filter.php* gives the flag ***picoCTF{y0u_m4d3_1t_a3ed4355668e74af0ecbb7496c8dd7c5}***     

<br>   

## B. <a href = 'https://play.picoctf.org/practice/challenge/174'>Web Gauntlet 2</a>   
<pre>
A similar login page and a page filter.php are given.
</pre>
**Filter used -** ```or and true false union like = > < ; -- /* */ admin```   
Username can be taken as ```ad'||'min``` but since there is no way to end the query,
we need to find a way to make the password *true*.    
One such way is to use ```is not``` which returns true.    
The password can be taken as ```1' is not '2```.     
The query becomes :    
```sql
SELECT username, password FROM users WHERE username='ad'||'min' AND password='1' is not '2'
```    

It works and *filter.php* gives the flag ***picoCTF{0n3_m0r3_t1m3_e2db86ae880862ad471aa4c93343b2bf}***     

<br>

## C. <a href = "https://play.picoctf.org/practice/challenge/128">Web Gauntlet 3</a>
<pre>
Again similar login page and a page filter.php are given. Since no new filter is added, username and password
from previous problem works fine.
</pre>
**Filter used -** ```or and true false union like = > < ; -- /* */ admin```      

username - ```ad'||'min```      
password - ```1' is not '2```        

The query becomes :    
```sql
SELECT username, password FROM users WHERE username='ad'||'min' AND password='1' is not '2'
```    

It works and *filter.php* gives the flag ***picoCTF{k3ep_1t_sh0rt_6fdd78c92c7f26a10acd3ece176dea4d}***   

<br>

## D. <a href = "https://play.picoctf.org/practice/challenge/80">Irish-Name-Repo 1</a>   
<pre>
A <a href = "https://jupiter.challenges.picoctf.org/problem/39720/">webpage</a> is given with a login page.   
It also seems to be a SQL injection problem.
</pre>
Trying **admin** as username and password gives login failed.   
The query should be like - 
```sql
SELECT * FROM users WHERE username='admin';
```     
Trying a simple injection ```admin';``` reveals the flag ***picoCTF{s0m3_SQL_c218b685}***.    

<br> 
  
## E. <a href = "https://play.picoctf.org/practice/challenge/59">Irish-Name-Repo 2</a>   
<pre>
A similar <a href = "https://jupiter.challenges.picoctf.org/problem/52849/">webpage</a> is given with a login page.   
</pre>
Trying **admin** as username and password gives login failed.     
Trying as previous one ```admin';``` reveals the flag ***picoCTF{m0R3_SQL_plz_fa983901}***.    

<br>   

## F. <a href = "https://play.picoctf.org/practice/challenge/8">Irish-Name-Repo 3</a>   
<pre>
A similar <a href = "https://jupiter.challenges.picoctf.org/problem/29132/">webpage</a> is given with a login page.   
</pre>
This time only password box is given. Trying **admin** has password gives login failed.  
On viewing the source code of the page we can see a tag named **debug** set to 0,   
On turning it to 1, we can see the actual query.
```sql
SELECT * FROM admin where password = 'nqzva'
```
The input **admin** changed to **nqzva**, there must be some encryption here.     
But we can avoid decoding the encryption because we just have to make the password *true*.     
We can do this by ```!=```.       
Entering password ```1' != '2``` reveals the flag ***picoCTF{3v3n_m0r3_SQL_06a9db19}***.     

<br> 

## G. <a href = "https://play.picoctf.org/practice/challenge/25">JaWT Scratchpad</a> 
<pre>
A <a href = "https://jupiter.challenges.picoctf.org/problem/61864/">link</a> to a webpage is given.
The webpage is a scratchpad, which says 
<i>You will need to log in to access the JaWT scratchpad.You can use any name, other than admin... 
because the admin user gets a special scratchpad!</i>
So, we need to take admin access. We are also given 2 other links, <a href="https://jwt.io/">JWT</a> and <a href="https://github.com/magnumripper/JohnTheRipper">John</a>,
to a JSON Web Tokens decoder and john the ripper. This indicates we might have to use john the ripper and
the JWT decoder.

On entering a username as <b>admin</b>, the following message is displayed - 

<i>YOU CANNOT LOGIN AS THE ADMIN! HE IS SPECIAL AND YOU ARE NOT.</i>

On entering a different username,a cookie named jwt is created, it can seen using an extension or dev tools,
the cookie contains which looks like base64 data. Decoding the string gives a JSON.
Which gives the hint that it might need to be decoded from given link.
</pre>
<pre>
For username <i><b>loki</b></i> the token was
<i>eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoibG9raSJ9.xaY3VU6pL90moR9d5iywyquMo3dimZkAKCR5YPsYTLY</i>
</pre>     

**Header**     

> {"typ": "JWT","alg": "HS256"}       
    
**Payload**

> {"user": "loki"}

<pre>
The website generates another token when <i>user</i> is changed to <i><b>admin</b></i>.
The new token is 
<i><b>eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.-vh-85mhRjMzTUsaJEWhgJwu-_EzDOy8zI0a9dik2Ww</b></i>
But it is incorrect as its signature is a random string and not the secret key used by the author.
We need to find this secret key by using john.
</pre>
The algorithm is HS256. 
</pre>
<pre>
The secret key is <i><b>ilovepico</b></i>
The token is 
<i><b>eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s</b></i>
Pasting this token in cookie reveals the flag <i><b>picoCTF{jawt_was_just_what_you_thought_1ca14548}</b></i>
</pre>    

<br>   

## H. <a href = "https://play.picoctf.org/practice/challenge/296">Secrets</a> 
<pre>
It is given that several pages are hidden. An instance is given and on running it a webpage opens.
ON inspecting it can be found that the source of the directory is the folder <b><i>secret</i></b>.
</pre> 
On changing the path to ```/secret``` it says _You almost found me_.     
Upon inspect, the source has a further folder named ***hidden***,     
changing the path to ```/secret/hidden```,
another folder is found named **_superhidden_**      
changing the path to ```/secret/hidden/superhidden```
Source code of _superhidden_ page reveals the flag ***picoCTF{succ3ss_@h3n1c@10n_39849bcf}***      

<br>    

## I. <a href = "https://play.picoctf.org/practice/challenge/69">Client-side-again</a> 
<pre>
A web page with a login box is given. Entering any credential it says <i>Incorrect password</i>.
</pre>
<code>On looking the source code a JS function is given which needs to be beautified.</code>     
```javascript
var _0x5a46 = ['f49bf}', '_again_e', 'this', 'Password\x20Verified', 'Incorrect\x20password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
(function(_0x4bd822, _0x2bd6f7) {
    var _0xb4bdb3 = function(_0x1d68f6) {
        while (--_0x1d68f6) {
            _0x4bd822['push'](_0x4bd822['shift']());
        }
    };
    _0xb4bdb3(++_0x2bd6f7);
}(_0x5a46, 0x1b3));
var _0x4b5b = function(_0x2d8f05, _0x4b81bb) {
    _0x2d8f05 = _0x2d8f05 - 0x0;
    var _0x4d74cb = _0x5a46[_0x2d8f05];
    return _0x4d74cb;
};

function verify() {
    checkpass = document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];
    split = 0x4;
    if (checkpass[_0x4b5b('0x2')](0x0, split * 0x2) == _0x4b5b('0x3')) {
        if (checkpass[_0x4b5b('0x2')](0x7, 0x9) == '{n') {
            if (checkpass[_0x4b5b('0x2')](split * 0x2, split * 0x2 * 0x2) == _0x4b5b('0x4')) {
                if (checkpass[_0x4b5b('0x2')](0x3, 0x6) == 'oCT') {
                    if (checkpass[_0x4b5b('0x2')](split * 0x3 * 0x2, split * 0x4 * 0x2) == _0x4b5b('0x5')) {
                        if (checkpass['substring'](0x6, 0xb) == 'F{not') {
                            if (checkpass[_0x4b5b('0x2')](split * 0x2 * 0x2, split * 0x3 * 0x2) == _0x4b5b('0x6')) {
                                if (checkpass[_0x4b5b('0x2')](0xc, 0x10) == _0x4b5b('0x7')) {
                                    alert(_0x4b5b('0x8'));
                                }
                            }
                        }
                    }
                }
            }
        }
    } else {
        alert(_0x4b5b('0x9'));
    }
}      
```


<pre>
The given function looks like a password verification system.
It verifies the password during runtime, but by reversing the function we can see with what value
is it comparing the entered password.
The verify() function verifies if the input password (checkpass) conforms to a specific format and
contains certain substrings whose indexes are overlapping in some cases in specified positions. 
Each if statement corresponds to checking one part of the password format. If all checks pass, 
it alerts "Password Verified"; otherwise, it alerts "Incorrect password".
</pre>
    
> _0x4b5b("0x0") - "getElementById"     
> _0x4b5b("0x1") - "value"     
> _0x4b5b("0x2") - "substring"     
> _0x4b5b("0x3") - "picoCTF{"     
> _0x4b5b("0x4") - "not_this"     
> _0x4b5b("0x5") - "55670}"     
> _0x4b5b("0x6") - "_again_0"     
> _0x4b5b("0x7") - "this"     
> _0x4b5b("0x8") - "Password Verified"     
> _0x4b5b("0x9") - "Incorrect password"           
         
_These are the values from the array, and the substring is checked against them in each step._      
_Substituting the values in the program_    
```javascript
if (checkpass["substring"](0, split * 2) == "picoCTF{") {
```
Checks if the substring from index 0 to split * 2 (which is 8 characters if split is 4) matches "picoCTF{".     

```javascript
if (checkpass["substring"](7, 9) == "{n") {
```
Checks if the substring from index 7 to 9 is "{n".

```javascript
if (checkpass["substring"](split * 2, split * 2 * 2) == "not_this") {
```
Checks if the substring from index 8 to 16 (if split is 4) matches "not_this".

```javascript
if (checkpass["substring"](3, 6) == "oCT") {
```
Checks if the substring from index 3 to 6 matches "oCT".

```javascript
if (checkpass["substring"](split * 3 * 2, split * 4 * 2) == "55670}") {
```
Checks if the substring from index 16 to 24 (if split is 4) matches "55670}".

```javascript
if (checkpass["substring"](6, 11) == "F{not") {
```
Checks if the substring from index 6 to 11 matches "F{not".

```javascript
if (checkpass["substring"](12, 16) == "this") {
```
Checks if the substring from index 12 to 16 matches "this".

```javascript
if (checkpass["substring"](split * 2 * 2, split * 3 * 2) == "_again_0") {
  alert("Password Verified");
}
```
Checks if the substring from index 8 to 16 (if split is 4) matches "_again_0". If all conditions are satisfied,
it displays an alert saying "Password Verified".    

If any of the conditions fail, an alert stating "Incorrect password" is displayed.

By just removing the overlaping we get the flag ***picoCTF{not_this_again_55670}***      

<br>
     
## J. <a href = "https://play.picoctf.org/practice/challenge/142">Who are you?</a> 
<pre>
A web page is given which says 
<i>Only people who use the official PicoBrowser are allowed on this site!</i>
Using Burp Suite to send the requests 
</pre>

We need to change the ```User-Agent``` to ```PicoBrowser``` and send the request again.

The response is now changed to    
_I don't trust users visiting from another site._     
     
We need to add a header ```Referer``` and set its value to same as that of ```host```.    
  
The response is now changed to    
_Sorry, this site only worked in 2018._      
    
We need to add the ```Date``` header and set it some date in 2018.      
like ```Date: Sat, 30 Jun 2018 10:10:00 GMT```      

The response is now changed to    
_I don't trust users who can be tracked._      
   
We need to add ```DNT``` header and set its value to ```1```  

The response is now changed to         
_This website is only for people from Sweden._     
       
We now need to change the IP address to Sweden using ```X-Forwarded-For``` header    
add ```X-Forwarded-For: 46.236.76.0```     

The response is now changed to       
_Youre in Sweden but you dont speak Swedish?_    

We need to add ```Accept-Language``` header to ```sv```

### Example request
> GET / HTTP/1.1         
> Host: mercury.picoctf.net:46199        
> Accept-Language: sv        
> Upgrade-Insecure-Requests: 1        
> Date: Sat, 30 Jun 2018 10:10:00 GMT         
> DNT: 1        
> Content-Length: 0        
> X-Forwarded-For: 46.236.76.0        
> User-Agent: Picobrowser        
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7        
> Accept-Encoding: gzip, deflate, br        
> Referer: http://mercury.picoctf.net:46199        
> Connection: keep-alive        

The flag is now revealed to be ***picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_8d5d8d77}***     

<br>   
      
## K. <a href = "https://play.picoctf.org/practice/challenge/419">IntroToBurp</a> 
<pre>
 
</pre>

## L. <a href = "https://play.picoctf.org/practice/challenge/29">Java Script Kiddie </a> 
<pre>
Will complete soon
</pre>

## M. <a href = "https://play.picoctf.org/practice/challenge/33">Java Script Kiddie 2</a> 
<pre>
Will complete soon
</pre>
</pre>
