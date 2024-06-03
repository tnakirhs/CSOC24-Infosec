print("$ use 'help' to know more")

import time,random
d_count = 0 #egg

def help():
    print("- this language can create and print string and integer variables, use these variables in basic operations, do basic")
    print("  arithmatic operations on integers, perform basic operation on strings like reverse and concatenation and for loop.")
    print("- syntax")
    print("\n - for loop ----- 'for the memes from <start> to <stop> by <step> step to the moon'")
    print("   type in exact format and replace the values for <start>, <stop>, <step> with integers")
    print("\n - basic operations ----- 'eval <enter_a_simple_mathematical_expression>'")
    print("\n - check command history ----- 'history' ----- and clear history -----'history -c' ")
    print("\n - string operations ----- 'string reverse <string>' ----- 'string add <string1> <string2>'")
    print("\n - to define a variable 'var int <identifier>' and 'var string <identifier>' can be used")
    print("\n - to print the value of a variable 'var value <identifier>' can be used")
    print("\n - 'value(<identifier>)' ----- can be used to print value of a variable and can also be used to replace")
    print("    to replace the formats given above between < > according to data type")
    print("\n - this language follow general programming context and is loosely based on python and C")
    print("\n - the language is case-sensative and error handling is done at almost all points")
    print("\n - some features such as for loop and string are very basic and not very well worked on")
    print("\n - comments are provided for further help")
    print("\n - though it is quite hard to exit the language with an error, good luck with possible command operations")
    print()


def syntax_error(code): #to output the message,probably the most used function
    print("- syntax error :",code,"is not a recognized command.")

def check_identifier(identifier):#checks for the general rules for naming an identifier
    for i in identifier:
        if i not in "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890_" or identifier[0] in "1234567890":
            return False

def value(identifier):#it is another way of printing the value of a variable, and using the values in expressions 
    global variables #variables is a dictionary with keys as variables
    if identifier in variables.keys():
        return (variables.get(identifier))

def evaluate(code):#since eval() function is used in the code, so that only simple math operations on integers are done, this function is defined
    for i in code:
        if i not in "1234567890+-/*%":
            return False    

def correct_syntax(code): #this may be the most important function
    ideal_code = ["var","eval","string","for","history","help","credits","reset"]
    ideal_code_single = ["credits","help"]
    history_commands = ["history","history -c","history -f"]
    global d_count
    codeword = code[-1].split()
    if code[-1][0:6]+code[-1][-1] != "value()" and ((codeword[0] not in ideal_code) or (codeword[0] in ideal_code_single and len(codeword) > 1)) \
    or  (codeword[0] == "history" and code[-1] not in history_commands):#checks if the query is invalid
        syntax_error(code[-1])#syntax error
        code.remove(code[-1])#removes from *workspace*
        d_count+=1#counter adds up

#explaination of function correct_syntax
#so this function correct_syntax serves as as gateway to *almost* all queries entered.
#it is created to remove invalid or undefined queries and free up space from the *workspace*
#all defined queries in this language start with elements from ideal_code.
#ideal_code_single has queries which are just one word and don't have any flag or other command
#history_commands has some history functions, history displays history, history -c clears it,
#history -f was created to record only those queries which give some result or are defined in code or are *functional* or it *filters* history 
#but does not work properly as a lot of changes will be required but eliminates all rubbish queries 
#excepts for the invalid queries of the functions in ideal_code except history.
#d_count is a counter. It do something.
#so each line is witten in a list code,the *workspace*. code = ["help"] by default for syntax reasons,when a new line is 
#entered it appends to code, it is deleted after executing(either valid or invalid(syntax error)). so at a given time
# there are either 1 or 2 elements in code. 

def for_loop_num(start,stop,step=1):#it is a basic for loop runner for the *special* syntax used
    for i in range(start,stop,step):
        print(i)

def main(): #it is the main body 
    while 1: #so that the loop never say never
        code = ["help"] #the *workspace*
        codelog = []#it stores the raw history including invalid and useless queries entered
        codelog_f = []#it stores *mostly* only those queries which were executed successfully,f for filter in case you wonder
        global variables #a dictionary to store variables and their values
        variables = {}#obvious
        
        while code[-1] != "reset":#some condition was needed for the while loop to break,while history -c only clears history, reset resets everything(atleast try to)
            code = ["help"]+[i for i in [input("$ ")] if i != ""] #takes queries, ignores unnecessary enters
            
            codelog = codelog+[code[-1]] if len(code) > 1 else codelog #stores the raw query for history
            correct_syntax(code)#queries go to the gateway for sanity check
            codelog_f = codelog_f+[code[-1]] if len(code) > 1 else codelog_f#store the filtered queries for history -f
            
            codeword = code[-1].split()#queries can be multi word so better to split them based on space
            codeface = codeword[0]#unnecessary but is frequently used

            #codeface is the first word of the query entered and is always from list ideal_code
            
            if codeface == "help" and len(code) != 1:#to call an ambulance but not for me
                help()
           
            elif codeface == "history":#recalls history (codeface is the first word of the query)
                if len(codeword) == 1: #since history commands have max word length 2(with -c and -f)
                    for i in range(len(codelog)):#prints the history
                        print("--",codelog[i])
                
                elif len(codeword) == 2:#if a query start with history and has two words, it can either be -c or -f, otherwise error        
                    if codeword[1] == "-c": 
                            print("- history cleared")#evidence removed, somethings not right here
                            codelog = codelog_f =  [] #chaos and order descends to nullity
                    if codeword[1] == "-f": 
                        for i in range(len(codelog_f)):#prints filtered list
                            print("--",codelog_f[i])   

            elif codeface == "eval":#for basic meth operations
                if len(codeword) == 2:#it can only be a 2 word query, eval and the expression
                    
                    key_list = list(variables.keys())#this part was written in the end, it is a list of variables from dictionary variables
                    key_list.sort(key=len, reverse=True)#it sorts the variables according to length, to solve a very annoying problem
                    if len(key_list) != 0: #if its not broke
                        for i in key_list:
                            if bool(type(variables.get(i)) == int) == True: #checks if the variable has integer data type
                                if "value("+i+")" in codeword[-1]:#if the variable is present in the expression
                                    codeword[-1] = codeword[-1].replace("value("+i+")",str(variables.get(i)))  
                                    #replaces the variable in expression with its value                  
                    evaluate(codeword[-1]) #checks if only simple math operations are performed
                    if evaluate(codeword[-1]) == False:#if meth operations are performed 
                        syntax_error(code[-1])
                    else:
                        print("- result of expression",codeword[-1],"is",eval(codeword[-1]))
                        #expression evaluated with subsituted values if any
                else:
                    syntax_error(code[-1])#error if length of query is not 2
            
            elif codeface == "var":#(codeface is the first word of the query) for defining a variable
                if len(codeword) == 3:#this query can take only 3 words - var+data type+identifier
                    
                    identifier_key = str(codeword[-1]) #used in storing the key in dictionary 
                    if check_identifier(codeword[-1]) != False: #it checks for the general rules for naming an identifier(wasted)
                        if codeword[-2] == "int":#if var is of int data type
                            codeword[-1] = input("$ enter value : ")#not $
                            
                            try:#so that program is not exited when isinstance() give valueerror for checking str against int
                                if isinstance(int(codeword[-1]), int):#if it is by change convertable to int
                                    variables[identifier_key] = int(codeword[-1])#stored as key
                            except ValueError:
                                print("- value error : "+identifier_key+" can only take integer values.")#new type of error
                        
                        elif codeword[-2] == "string":#if the var type is string
                             codeword[-1] = input("$ enter value : ")#enter string
                             variables[identifier_key] = (codeword[-1])#adds the variable to dictionary
                        
                        elif codeword[-2] == "value":#to print value of the variable,value() also do the same job,but this is original one.
                            if codeword[-1] in variables.keys():#if the identifier exists it prints value and data type
                                print("-",variables.get(codeword[-1])," | ",type(variables.get(codeword[-1])))
                            else:
                                print("- name error : invalid variable name "+codeword[-1]+".")#else prints error(newww error),if identifier not found or undefined
                        else:
                            print("- data type error :",codeword[-2],"not recognized.")#nu error, data type invalid or other than str and int
                    else:
                        print("- identifier error : identifier should be alphanumeric + _ and should not start with a number.")#niche error
                else:
                    syntax_error(code[-1])#dumb error
                
            elif codeface == "string":#sting operations

                if len(codeword) in [3,4]:#so that variables can be used in the functions
                    key_list = list(variables.keys())#list of variables
                    key_list.sort(key=len, reverse=True)#to a avoid super annoying problem
                    if len(key_list) != 0:
                        for i in key_list:
                            if bool(type(variables.get(i)) == str) == True: #if the data type of variable is str
                                if "value("+str(i)+")" == str(codeword[-1]): #if the variable from the list is same as the entered variable
                                    codeword[-1] = variables.get(i) #the value of first variable is subsituted with value of the same variable from the list
                                if "value("+str(i)+")" == str(codeword[-2]):
                                    codeword[-2] = variables.get(i)

                    if codeword[1] == "reverse" :#reverse the given string
                        if len(codeword) == 3:#the query can have 3 words only string+reverse+<string_to_be_reversed>
                            print("-",codeword[-1][::-1])
                        else:
                            syntax_error(code[-1])

                    if codeword[1] == "add" :#adds 2 given strings
                        if len(codeword) == 4: #string + add + <string1> + <string2>
                            print("-",codeword[-1]+codeword[-2])
                        else:
                            syntax_error(code[-1])
                else:
                    syntax_error(code[-1])#dumb error

            elif codeface == "for": # for the memes from "start" to "stop" by "step" step to the moon
                if len(codeword) == 13:#13
                    if codeword[1]+codeword[2]+codeword[3]+codeword[5]+codeword[7]+codeword[9]+codeword[10]+codeword[11]+codeword[12]== "thememesfromtobysteptothemoon" :
                        if [bool(i) for i in [codeword[4],codeword[6],codeword[8]]] == [True,True,True]: #checks if all the integer
                            for_loop_num(int(codeword[4]),int(codeword[6]),int(codeword[8]))
                        else:
                            print("- data type error : start, stop and step must be integers.")#they should be, though there are others conditions and errors that can be fixed they are not done.
                    else:
                        syntax_error(code[-1])
                else:
                    syntax_error(code[-1])#dumb error

            elif codeface[0:6]+codeface[-1] == "value()":#it can be used to print the value of variable but it was created so that the variables can be used in expressions.
                if check_identifier(codeface[6:-1]) != False:#if the value between value(<----->), is not (not an identifier)
                    if value(codeface[6:-1]) != None:
                        print(value(codeface[6:-1]))#value function returns the value
                    else:
                        print("- name error : invalid variable name "+codeface[6:-1]+".")# (:-1)
                else:
                    print("- identifier error : identifier should be alphanumeric + _ and should not start with a number.")#niche error
            
            elif codeface == "credits":
                print("- created by Shrikant Vashishtha")#hats off
            
            else:
                global d_count #global issues
                if d_count > 10:
                    print()
                    print("- Take a deep breath. ")
                    time.sleep(1)
                    print("- For 10 syntax errors, here is your sessional dose of wisdom")
                    quotes = ["- Correct syntax has been chasing you but you have always been faster.",\
                                        "- We would agree with your syntax but then we would both be wrong.",\
                                        "- A mistake that we did when trying to make this language completely foolproof was to underestimate your ingenuity.",\
                                        "- You're the reason i created 'help'."]
                    for i in random.choice(quotes):
                        print(i,end = "")
                        time.sleep(0.02)
                    print()
                    d_count = 0 #d is for dumb
main()

