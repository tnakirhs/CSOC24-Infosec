**Challenge #2**      
***Sakura Room***       

***1. INTRODUCTION***
<pre>Let's Go!</pre>

***2. TIP-OFF***
<pre>The image left behind the cybercriminals is a svg with some binary data and text in the background.
On inspecting we find the source of the file which reveals <b><i>username</i></b></pre>


***3. RECONNAISSANCE***
<pre>Since we have the username, we can use it to find the hecker on other platforms using name username 
finder or just directly google the username which gives displays his github and twitter.He has a public 
key in his repo which can be decoded with a pgp decoder online or just base64, the username in the key 
reveals <b><i>email</i></b>. His twitter shows up even when the usernames are different maybe because 
there are too many writeups for this room. Few linkedin links with a <b><i>name</i></b> also shows up.</pre>

***4. UNVEIL***
<pre>The repos have some crypto names so i just tried all the cryptos mentioned in the repos and got the answer.
Since all repo except eth and io are forked ,they may not be related to the problem at all.
So i tried on eth (io has nothing significant), it has a filename which was edited. Its previous version 
had some comments which help about the <i><b>wallet address</i></b>.<br>
To know about the payment history i <s>saw a writeup</s> did some research to track the transaction from wallet 
address (just search crypto transaction tracker and enter wallet address). 
The transaction details reveal the <b><i>mining pool</i></b> and <b><i>exchanged crypto</i></b>.</pre>

***5. TAUNT***
<pre>We already know the <b><i>twitter handle</i></b> by searching the <b><i>username</i></b>, but it can also be found by searching the
username given in screenshot attached on twitter. The hecker had tweeted that he has pasted some data on 
dark web (deep), a reference to DeepPaste, but i could not find any working link on tor instead i used the 
hint. Searching 'bssid wifi osint' i found a website 'wigle.net' </pre>
<pre>Will complete soon</pre>

***6. HOMEBOUND***
<pre>The <i><b>city</b></i> name can be found in the screenshot of DeepPaste</pre>
<pre>Will complete soon</pre>
