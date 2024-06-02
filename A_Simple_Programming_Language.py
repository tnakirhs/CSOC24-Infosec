def help():
    print("""This language can create string and int variables, do basic arithmatic operations on integers, 
    perform basic operation on strings like reverse, search for a string inside string, printing a string n times. """)

help()

def declare():
    pass

def correct_syntax(code):
    ideal_code = ["var","eval","string","for","history","help","credits","reset"]
    ideal_code_single = ["history","credits","reset","raw","help"]
    history_commands = ["history -c","history -f"]
    for i in range(len(code)):
        codeword_i = code[i].split()
        if codeword_i[0] not in ideal_code or (codeword_i[0] in ideal_code_single and len(codeword_i) > 1) and code[i] not in history_commands:
            # print(code[i],33313,code[i].split()[0])
            # print(str(code[i]))
            print("- Syntax Error :",str(code[i]),"is not a recognized command.")
            code.remove(code[-1])
            break

def main():
    codelog = []
    codelog_f = []
    while 1:
        code = ["help"]
        while code[-1] != "reset":
            code = ["help"]+[i for i in [input("$ ")] if i != ""]
            
            codelog = codelog+[code[1]] if len(code) > 1 else codelog
            correct_syntax(code) 
            codelog_f = codelog_f+[code[1]] if len(code) > 1 else codelog_f
            
            codeword = code[-1].split()
            codeface = codeword[0]
            
            if codeface == "help" and len(code) != 1:
                help()
            elif codeface == "history":
    
                print(codelog_f)
                print(codelog)
                if len(codelog) > 1: 
                    for i in range(1,len(codelog)):
                        print("# ",codelog[i])
                    if input("- Type 'clear' to clear history, press any key to exit : ") == "clear": 
                        print("- history cleared")
                        codelog = ["help"]
                        print(codelog)
                # if code[-1] == "history -r":

            elif codeface == "reset":
                main()
            elif codeface == "credits":
                print("- Created by Shrikant Vashishtha")
            elif codeface == "raw":     
                print()
            else: pass
    
main()
