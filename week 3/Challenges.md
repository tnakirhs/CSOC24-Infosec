# Challenges   

<br>

## A. <a href = "https://play.picoctf.org/practice/challenge/88?page=1&search=web%20gaun">Web Gauntlet</a>

<pre>
A login page is given along with a page filter.php. 
When any username and password are entered, a SQL query appears in the background of the page. 
Our aim is to take admin access for which username must be <b>admin</b>. 
This is indeed a SQL injection problem.
</pre>

* #### Round 1
  **Filter used -** ```or```    
    
  ```SELECT * FROM users WHERE username='admin' AND password='admin'```     
  when username and password are **admin**.    
  
  We need the query to be    
  ```SELECT * FROM users WHERE username='admin';```    
  
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

## B. <a href = 'https://play.picoctf.org/practice/challenge/174?page=1&search=web%20gaun'>Web Gauntlet 2</a>   
<pre>
A similar login page and a page filter.php are given.
</pre>
**Filter used -** ```or and true false union like = > < ; -- /* */ admin```   
Username can be taken as ```ad'||'min``` but since there is no way to end the query,
we need to find a way to make the password *true*.    
One such way is to use ```is not``` which returns true.    
The password can be taken as ```1' is not '2```.    
It works and *filter.php* gives the flag ***picoCTF{0n3_m0r3_t1m3_e2db86ae880862ad471aa4c93343b2bf}***     

<br>

## C. <a href = "https://play.picoctf.org/practice/challenge/128?page=1&search=web%20gaun">Web Gauntlet 3</a>
<pre>
Again similar login page and a page filter.php are given. Since no new filter is added, username and password
from previous problem works fine.
</pre>
**Filter used -** ```or and true false union like = > < ; -- /* */ admin```      

username - ```ad'||'min```      
password - ```1' is not '2```        

<br>

## Irish-Name-Repo 1
## Irish-Name-Repo 2
## Irish-Name-Repo 3
## JaWT Scratchpad
## Secrets
## Client-side-again
## Who are you?
## IntroToBurp
## Java Script Kiddie 
## Java Script Kiddie 2
