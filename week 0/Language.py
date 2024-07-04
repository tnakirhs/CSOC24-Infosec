#A simple programming language

print("$ use 'help' to know more")

import time,random,ast

def check_identifier(identifier):#Rules for naming an identifier
    for i in identifier:
        if (i.isalnum() == False and i != "_") or identifier[0].isdigit() == True:
            return False

def evaluate(code):#To allow only basic math operations using eval()
    for i in code:
        if i not in "1234567890+-/*%()":
            return False

def correct_queries(code):#prints correct outputs
    print("- "+str(code))

def error_print(code):#prints errors
    print("- "+str(code))
    global syn_count
    syn_count+=1

def raw_history(codeword):#stores history of incorrect commands
    entry = "".join(codeword)
    codelog.append(entry)

def f_history(codeword):#stores history of successfull commands
    entry = " ".join(codeword)
    codelog_f.append(entry)
    codelog.append(entry)

def syntax_error(code):#Returns error if there is a syntax error
    error_print("syntax error : "+str(code)+" is not a recognized command.")

def for_loop_num(start,stop,step=1):#basic for loop runner for the *special* syntax used
    for i in range(start,stop+1,step):
        print(i)

def value(identifier):#another way of printing the value of a variable, and using the values in expressions 
    global variables #variables is a dictionary with keys as variables
    if identifier in variables.keys():
        return (variables.get(identifier))
    
def o(line): #to print help outputs
    print("~ "+str(line))

def array_operations(codeword):#Function to manage arrays
    if codeword[1] == "len":#length of array
        correct_queries(len(ast.literal_eval(codeword[-1])))
        f_history(codeword)

    elif codeword[1] == "reverse":#reverse the array
        correct_queries(ast.literal_eval(codeword[-1])[::-1])
        f_history(codeword)
                        
    elif codeword[1] == "set":#unique elements of an array
        correct_queries(set(ast.literal_eval(codeword[-1])))
        f_history(codeword)

    elif codeword[1] == "sort" :#sorting
        if codeword[2] == "asc":
            correct_queries(sorted(ast.literal_eval(codeword[-1])))
            f_history(codeword)
        elif codeword[2] == "dsc":
            correct_queries(sorted(ast.literal_eval(codeword[-1]),reverse=True))
            f_history(codeword)
        else:
            syntax_error(codeword[2])
            raw_history(codeword)

    elif codeword[1] == "sum" :#returns sum of array if all members are <int> or <float>
        wrongdt = 0
        for i in (ast.literal_eval(codeword[-1])):
            try:
                if isinstance(i,int) or isinstance(i,float):#checks if all elements are <int> or <float>
                    pass
            except :
                error_print("data type error : SUM can only be used with arrays having int or float data types.")
                raw_history(codeword)
                wrongdt = 1
                break
        if wrongdt == 0:
            correct_queries(sum(ast.literal_eval(codeword[-1])))
            f_history(codeword)

    elif codeword[1] == "join" :#concatenate 2 arrays
        correct_queries(ast.literal_eval(codeword[-2])+ast.literal_eval(codeword[-1]))
        f_history(codeword)

    elif codeword[1] == "identical" :#returns identical elements of 2 arrays
        correct_queries("unique elements : "+str(list(set(ast.literal_eval(codeword[-2])) & set(ast.literal_eval(codeword[-1])))))
        f_history(codeword)
    
    else:
        syntax_error(codeword)
        raw_history(codeword)

def correct_syntax(code): #Checks for basic syntax error and remove unfavourable queries.  
    ideal_code = ['array','credits','disable_count',"enable_count",'eval','exit()','for','help','help()','history','reset','string','var']
    codeword = code[-1].split()
    if (code[-1][0:6]+code[-1][-1] != "value()") and (codeword[0] not in ideal_code): #checks if the query is invalid
        syntax_error(code[-1])
        raw_history(list(code[-1]))
        code.remove(code[-1])

#Explaination of function correct_syntax
#This function (correct_syntax) serves as as gateway to *almost* all queries entered.
#It is created to remove invalid or undefined queries and free up space from the *workspace*
#All defined queries in this language start with elements from ideal_code.
#syn_count is a counter. It counts the number of errors made.
#Each line is witten in a list code,the *workspace*. code = ["help"] by default for syntax reasons,when a new line is 
#entered it appends to code, it is deleted after executing (either valid or invalid(syntax error)). so at a given time
#there are either 1 or 2 elements in code. 

def main(): #main body 
    while 1: 
        global codelog,codelog_f,variables,syn_count
        code = ["help"] #the *workspace*
        codelog = []#stores the raw history including invalid queries entered
        codelog_f = []#it stores only those queries which were executed successfully,f for filtered
        syn_count = 0
        variables = {}#a dictionary to store variables and their values
        
        while code[-1] != "reset":#some condition was needed for the while loop to break,while history -c only clears history, reset resets everything.
            code = ["help"]+[i for i in [input("$ ")] if i != ""] #takes queries, ignores unnecessary enters
            
            correct_syntax(code)#queries checked for basic syntax errors.
            
            codeword = code[-1].split()#queries can be multi word so better to split them based on "space"
            codeface = codeword[0]#unnecessary but is frequently used

            #codeface is the first word of the query entered and is always from list ideal_code
            
            if codeface == "help" and len(code) != 1:#to call an ambulance but not for me
                if len(codeword) == 1:
                    f_history(codeword)
                    o('     -gen  General or help()')
                    o('     -arr  Arrays and list')
                    o('     -syn  Syntax error counter')
                    o('     -evl  Mathematical operations on integers')
                    o('     -ext  Exit')
                    o('     -for  For loop')
                    o('     -hst  History')
                    o('     -rst  Reset')
                    o('     -str  String Operations')
                    o('     -var  Variables and Value()')
                    
                elif len(codeword) == 2:

                    if codeword[-1] == "-gen":
                        f_history(codeword)
                        help()
                    
                    elif codeword[-1] == "-arr":
                        f_history(codeword)
                        o("Arrays don't have native support, they are stored as string and then converted into lists using ast module.")
                        o("Due to syntax reasons Arrays cannot have space (' ')")
                        o("Written like python lists.")
                        o("The query having Array as first word can have either 3 or 4 words.")
                        o("Example - [1,2,3,4] or ['h','e','l','p']")
                        o("The following operations can be performed : ")
                        o("1. len - returns the length of array.")
                        o("syntax : array len <array>")
                        o("2. reverse - returns the reversed array.")
                        o("syntax : array reverse <array>")
                        o("3. set - returns an array of unique elements of the input array.")
                        o("syntax : array set <array>")
                        o("4. sort - sorts the array in ascending or descending order.")
                        o("syntax : array sort asc <array>")
                        o("syntax : array sort dsc <array>")
                        o("5. sum - returns sum of elements of array if all elements are integer.")
                        o("syntax : array sum <array>")
                        o("6. identical - compares 2 arrays and returns an array of identical elements.")
                        o("syntax : array identical <array1> <array2>")
                        o("7. join - concatenate 2 arrays.")
                        o("syntax : array join <array1> <array2>")
                        o("<array> can be replaced by variable by using <value(variable)>")
                        
                    
                    elif codeword[-1] == "-evl":
                        f_history(codeword)
                        o("eval do simple mathematical calculations.")
                        o("query can have only 2 words, eval and the expression, space (' ') is not allowed in expression.")
                        o("syntax : eval <expression_without_space>")
                        o("only +,-,/,*,% are supported.")
                    
                    elif codeword[-1] == "-ext":
                        f_history(codeword)
                        o("exit uses exit() of python to exit the program.")
                        o("syntax : exit()")
                    
                    elif codeword[-1] == "-for":
                        f_history(codeword)
                        o("to initialize for loop")
                        o("syntax : for <start> to <stop> by <step>")
                        o("<start>, <stop>, <step> must be integers.")
                        o("to iterate elements of an array or a string")
                        o("syntax : for array <array>")
                        o("syntax : for string <string>")
                        
                    elif codeword[-1] == "-hst":
                        f_history(codeword)
                        o("'history' returns all entered queries")
                        o("'history -c' clears history")
                        o("'history -f' shows queries which were successfully executed.")

                    elif codeword[-1] == "-rst":
                        f_history(codeword)
                        o("'reset' resets all all user defined variables.")
                    
                    elif codeword[-1] == "-str":
                        f_history(codeword)
                        o("supported string operations are - ")
                        o("1. len - returns length of string.")
                        o("syntax : string len <string>")
                        o("2. reverse - reverses the string.")
                        o("syntax : string reverse <string>")
                        o("3. count - count frequency of one string in another.")
                        o("syntax : string count <string1> <string2>")
                        o("searches for <string2> in <string1>")
                        o("4. join - concatenate 2 strings.")
                        o("syntax : string join <string1> <string2>")
                    
                    elif codeword[-1] == "-syn":
                        f_history(codeword)
                        o("It is counter which gives a dose of wisdom when 10 errors are made.")
                        o("can be turned off with 'disable_counter'.")
                        o("can be turned off with 'enable_counter'.")

                    elif codeword[-1] == "-var":
                        f_history(codeword)
                        o("var is used to assign values to variables")
                        o("variables can be of 3 types : ")
                        o("1. int - used to store integers.")
                        o("syntax : var int myint")
                        o("2. string - used to store strings.")
                        o("syntax : var int mystr")
                        o("3. int - used to store arrays.")
                        o("syntax : var int myarr")
                        o("val is used to return the value of the variable with type.")
                        o("value(<variable>) returns the value, can be used in expressions.")
                        o("Example - ")
                        o("         var int myint1")
                        o("         - enter value : 9")
                        o("         eval value(myint1)+7")
                        o("         - 16")
                        o("         value(myint1)")
                        o("         - 9")
                        o("         var value myint1")
                        o("         - 9 | <class 'int'>")
                    
                    else:
                        syntax_error(code[-1])
                        raw_history(codeword)# when an error is encountered its history is stored to codelog.                      
                else:
                    syntax_error(code[-1])
                    raw_history(codeword)
                        
            elif codeface == "history":#recalls history (codeface is the first word of the query)
                
                if len(codeword) == 1: #since history commands have max word length 2(with -c and -f)
                    f_history(codeword)
                    for i in range(len(codelog)):#prints the history
                        print(" * ",codelog[i])
                
                elif len(codeword) == 2:#if a query start with history and has two words, it can either be -c or -f, otherwise error        
                    if codeword[1] == "-c":
                        f_history(codeword) #it stores queries executed successfully in codelog_f
                        print(" < history cleared > ")
                        codelog = []
                        codelog_f = []
                    elif codeword[1] == "-f":
                        f_history(codeword) 
                        for i in range(len(codelog_f)):
                            print(" * ",codelog_f[i]) #prints filtered list
                    else:
                        syntax_error(code[-1])
                        raw_history(code[-1])
                else:
                    syntax_error(code[-1])
                    raw_history(codeword)
                        

            elif codeface == "eval":#basic math operations
                if len(codeword) == 2:#can only be a 2 word query, eval and the expression
                    
                    key_list = list(variables.keys())#this part was written in the end, it is a list of variables from dictionary variables
                    key_list.sort(key=len, reverse=True)#it sorts the variables according to length, so that longer identifiers are checked first
                    if len(key_list) != 0:
                        for i in key_list:
                            if bool(type(variables.get(i)) == int) == True: #checks if the variable has integer data type
                                if "value("+i+")" in codeword[-1]:#if the variable is present in the expression
                                    codeword[-1] = codeword[-1].replace("value("+i+")",str(variables.get(i)))  
                                    #replaces the variable in expression with its value                  
                
                    evaluate(codeword[-1]) #checks if only simple math operations are performed
                    
                    if evaluate(codeword[-1]) == False:#if not
                        syntax_error(code[-1])
                        raw_history(codeword)
                    else:
                       correct_queries("result of expression "+str(codeword[-1])+" is "+str(eval(codeword[-1])))
                       f_history(codeword)
                        #expression evaluated with subsituted values if any
               
                else:
                    syntax_error(code[-1])
                    raw_history(codeword)
            
            elif codeface == "var":#(codeface is the first word of the query) for defining a variable
                if len(codeword) == 3:#this query can take only 3 words - (var + data-type + identifier)
                    
                    identifier_key = str(codeword[-1]) #used in storing the key in dictionary 
                    if check_identifier(codeword[-1]) != False: #checks for the general rules for naming an identifier
                        
                        if codeword[-2] == "array":#if the var data type is array
                            codeword[-1] = input("- enter array : ")

                            try:
                                if isinstance((ast.literal_eval(codeword[-1])),list):
                                    variables[identifier_key] = (codeword[-1])#adds the variable to dictionary
                                else:
                                    error_print("data type error : only arrays with (int) or (str) data type permitted.")
                                    raw_history(code[-1])
                            except:
                                error_print("data type error : only arrays with (int) or (str) data type permitted.")
                                raw_history(codeword)  
                            
                        elif codeword[-2] == "int":#if the var data type is int
                            codeword[-1] = input("- enter integer : ")
                            
                            try:#so that program is not exited when isinstance() give valueerror for checking str against int
                                if isinstance(int(codeword[-1]), int):#if it is by change convertable to int
                                    variables[identifier_key] = int(codeword[-1])#stored as key
                            except :
                                error_print("value error : "+identifier_key+" can only take integer values.")
                                raw_history(codeword)
                        
                        elif codeword[-2] == "string":#if the var data type is string
                             codeword[-1] = input("- enter string : ")
                             variables[identifier_key] = (codeword[-1])#adds the variable to dictionary
                        
                        elif codeword[-2] == "value":#to print value of the variable,value() also do the same job,but this is original one.
                            if codeword[-1] in variables.keys():#if the identifier exists it prints value and data type
                                correct_queries(str(variables.get(codeword[-1]))+"  |  "+str(type(variables.get(codeword[-1]))))
                                f_history(codeword)
                            else:
                                error_print("name error : invalid variable name "+str(codeword[-1])+".")
                                raw_history(codeword)
                        else:
                            error_print("data type error : "+str(codeword[-2])+" not recognized.")
                            raw_history(codeword)
                    else:
                        error_print("identifier error : identifier should be alphanumeric + '_' and should not start with a number.")
                        raw_history(codeword)
                else:
                    syntax_error(code[-1])
                    raw_history(codeword)
                
            elif codeface == "string":#string operations

                    key_list = list(variables.keys())#list of variables
                    key_list.sort(key=len, reverse=True)
                    if len(key_list) != 0:
                        for i in key_list:
                            if bool(type(variables.get(i)) == str) == True: #if the data type of variable is str
                                if "value("+str(i)+")" == str(codeword[-1]): #if the variable from the list is same as the entered variable
                                    codeword[-1] = variables.get(i) #the value of first variable is subsituted with value of the same variable from the list
                                if "value("+str(i)+")" == str(codeword[-2]):
                                    codeword[-2] = variables.get(i)

                    if (len(codeword) == 3) and (codeword[1] in ["len","reverse"]):
                        if codeword[1] == "len":
                            correct_queries(len(codeword[-1]))
                            f_history(codeword)
                        if codeword[1] == "reverse" :#reverse the given string
                            correct_queries(codeword[-1][::-1])
                            f_history(codeword)

                    elif (len(codeword) == 4) and (codeword[1] in ["count","join"]):
                        if codeword[1] == "count":
                            correct_queries(codeword[-2].count(codeword[-1]))
                            f_history(codeword)
                        if codeword[1] == "join":
                            correct_queries(codeword[-2]+codeword[-1])
                            f_history(codeword)
                    
                    else:
                        syntax_error(code[-1])
                        raw_history(codeword)

            elif codeface == "array" :#array operations

                    key_list = list(variables.keys())#list of variables
                    key_list.sort(key=len, reverse=True)
                    if len(key_list) != 0:
                        for i in key_list:
                            if bool(type(variables.get(i)) == str) == True: 
                                if "value("+str(i)+")" == str(codeword[-1]): 
                                    codeword[-1] = variables.get(i)
                                if "value("+str(i)+")" == str(codeword[-2]):
                                    codeword[-2] = variables.get(i)

                    if (len(codeword) == 3 and codeword[1] in ["len","reverse","set","sum"]) or (len(codeword) == 4 and codeword[1] == "sort") :
                        try:
                            if isinstance((ast.literal_eval(codeword[-1])),list):
                                array_operations(codeword)
                            else:
                                error_print("data type error : only arrays with (int) or (str) data type permitted.")
                                raw_history(codeword)
                        except :
                            error_print("data type error : only arrays with (int) or (str) data type are permitted.")
                            raw_history(code[-1])
          
                    elif (len(codeword) == 4 and codeword[1] in ["identical","join"]):
                        try:
                            if (isinstance((ast.literal_eval(codeword[-1])),list) and isinstance((ast.literal_eval(codeword[-2])),list)):
                                array_operations(codeword)
                            else:
                                error_print("data type error : only arrays with (int) or (str) data type permitted.")
                                raw_history(codeword)
                        except :
                            error_print("data type error : only arrays with (int) or (str) data type permitted.")
                            raw_history(codeword) 
                    else:
                        syntax_error(code[-1])
                        raw_history(codeword)
                 
            elif codeface == "for": #for "start" to "stop" by "step"
                if len(codeword) == 6 and codeword[2]+codeword[4]== "toby":
                    if [bool(i) for i in [codeword[1],codeword[3],codeword[5]]] == [True,True,True]:#checks if all are integer
                        f_history(codeword)
                        for_loop_num(int(codeword[1]),int(codeword[3]),int(codeword[5]))

                    else:
                        error_print("data type error : start, stop and step must be integers.")
                        raw_history(codeword)

                elif codeword[1] in ["array","string"] :
                    
                    key_list = list(variables.keys())
                    key_list.sort(key=len, reverse=True)
                    if len(key_list) != 0:
                        for i in key_list:
                            if bool(type(variables.get(i)) == str) == True: 
                                if "value("+str(i)+")" == str(codeword[2]):
                                    codeword[2] = variables.get(i)
                    
                    elif codeword[1] == "array":
                        try:
                            if isinstance(ast.literal_eval(codeword[2]), list):
                                f_history(codeword)
                                for i in ast.literal_eval(codeword[2]):
                                    print(i)
                            else:
                                error_print("data type error : only arrays with (int) or (str) data type permitted.")
                                raw_history(codeword)
                        except :
                            error_print("data type error: only arrays with (int) or (str) data type permitted.")
                            f_history(codeword)
                
                    elif codeword[1] == "string":
                        f_history(codeword)
                        for_string = ""
                        for i in codeword[2::]:
                            for_string = for_string+i+" "
                        for i in for_string[0:-1]:
                            print(i)
                    
                    else:
                        syntax_error(code[-1])
                        raw_history(codeword)                      

                else:
                    syntax_error(code[-1])
                    raw_history(codeword)

                
            elif codeface[0:6]+codeface[-1] == "value()":#it can be used to print the value of variable but it was created so that the variables can be used in expressions.
                if check_identifier(codeface[6:-1]) != False:#if the value between value(<->), is not (not an identifier)
                    if value(codeface[6:-1]) != None:
                        correct_queries(value(codeface[6:-1]))#value function returns the value
                        f_history(codeword)
                    else:
                        error_print("name error : invalid variable name "+str(codeface[6:-1])+".")
                        raw_history(codeword)
                else:
                    error_print("identifier error : identifier should be alphanumeric + '_' and should not start with a number.")#niche error
                    raw_history(codeword)
            
            elif codeface == "credits":
                correct_queries("created by Shrikant Vashishtha")
                f_history(codeword)
            
            elif codeface == "exit()":
                if len(codeword) == 1:
                    confirm = input("Do you want to exit (y/N): ")
                    if confirm.lower() in ["yes","y"]:
                        print("Exited.")
                        exit()
                else:
                    syntax_error(code[-1])
                    raw_history(codeword)

            elif codeface == "disable_count":
                syn_count = float("-inf")

            elif codeface == "enable_count":
                syn_count = 0
                                        
            else:
                if syn_count == 10:
                    print()
                    print("- Take a deep breath. ")
                    time.sleep(1)
                    print("- For 10 errors, here is your sessional dose of wisdom")
                    quotes = ['.retsaf neeb syawla evah uoy tub uoy gnisahc neeb sah xatnys tcerroC -', \
                              ".gnorw eb htob d'ew neht tub xatnys ruoy htiw eerga dluow I -", \
                              '.ytiunegni ruoy etamitserednu ot saw foorploof yletelpmoc egaugnal siht ekam ot gniyrt nehw did i taht ekatsim A -', \
                               ".'pleh' detaerc i nosaer eht er'uoY -"]
                    for i in random.choice(quotes)[::-1]:
                        print(i,end = "")
                        time.sleep(0.02)
                    print()
                    syn_count = 0 

def help():
    o("This language can do basic string/array oprations. Create and use variables.")
    o("Do basic arithmatic operations, operations like reversing, concatenation, sum can be done.")
    o("Brief help about each function is given.")
    o("Case sensative and strict syntax.")
    o("Queries are recorded and executed line by line.")
    o("It follows general programming context and is loosely based on python and C")
    o("The language is case-sensative and error handling is done at almost all points")
    o("Features are very basic.")
    o("Comments are provided for further help")

main() 
