print("$ use 'help' to know more")

import time,random
d_count = 0

def help():
    print("""This language can create string and int variables, do basic arithmatic operations on integers, 
    perform basic operation on strings like reverse, search for a string inside string, printing a string n times. """)

def declare():
    pass

def correct_syntax(code):
    ideal_code = ["var","eval","string","for","history","help","credits","reset"]
    ideal_code_single = ["credits","help"]
    history_commands = ["history -c","history -f"]
    global d_count
    for i in range(len(code)):
        codeword_i = code[i].split()
        if codeword_i[0] not in ideal_code or (codeword_i[0] in ideal_code_single and len(codeword_i) > 1) and code[i] not in history_commands:
            # print(code[i],33313,code[i].split()[0])
            # print(str(code[i]))
            print("- syntax error :",str(code[i]),"is not a recognized command.")
            code.remove(code[-1])
            d_count+=1
            break
def for_loop():
    pass
def main():
    while 1:
        code = ["help"]
        codelog = []
        codelog_f = []
        while code[-1] != "reset":
            code = ["help"]+[i for i in [input("$ ")] if i != ""]
            
            codelog = codelog+[code[-1]] if len(code) > 1 else codelog
            correct_syntax(code)
            codelog_f = codelog_f+[code[1]] if len(code) > 1 else codelog_f
            
            codeword = code[-1].split()
            codeface = codeword[0]
            
            if codeface == "help" and len(code) != 1:
                help()
           
            elif codeface == "history":
                # print(codelog_f)
                # print(codelog)
                if len(codeword) == 1:
                    for i in range(len(codelog)):
                        print("# ",codelog[i])     
                else:         
                    if codeword[1] == "-c": 
                            print("- history cleared")
                            codelog = codelog_f =  []
                    if codeword[1] == "-f":
                        for i in range(len(codelog_f)):
                            print("#  ",codelog_f[i])                        


            elif codeface == "eval":
                print(eval(codeword[-1]))
            elif codeface == "var":
                pass
            elif codeface == "string":
                pass
            elif codeface == "for":
                pass
            elif codeface == "credits":
                print("- Created by Shrikant Vashishtha")
            else:
                global d_count
                if d_count > 1:
                    print()
                    print("- Take a deep breath. ")
                    print("- 10 syntax errors, here is your sessional dose of wisdom")
                    quotes = ["- Correct syntax has been chasing you but you have always been faster.",\
                                        "- We would agree with your syntax but then we would both be wrong.",\
                                        "- A mistake that we did when trying to make this language completely foolproof was to underestimate your ingenuity.",\
                                        "- You're the reason we created 'help'."]
                    for i in random.choice(quotes):
                        print(i,end = "")
                        time.sleep(0.02)
                    print()
                    d_count = 0
main()
