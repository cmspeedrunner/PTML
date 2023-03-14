import sys
import traceback

fl = sys.argv[1]
with open(fl) as contents:
    contents = contents.read()

converter = {
    "<print>": "print(",
    "</print>": ")",
    "<if>": "if ",
    "</if>": ":",
    "<else>": "else ",
    "</else>": ":",
    "<for>": "for ",
    "</for>": ":",
    "<range>": "range(",
    "</range>": ")",
    "<def>": "def ",
    "</def>": ":",
    "<comment>": "#",
    "<while>": "while ",
    "</while>": ":",
    "<and>": "and",
    "<input>":"input(",
    "</input>": ")",
    "<len>": "len(",
    "</len>":")",
    "<str>": "str(",
    "</str>": ")",
    "<int>": "int(",
    "</int>": ")",
    "<float>": "float(",
    "</float>": ")",
    "<bool>": "bool(",
    "</bool>": ")",
    "<or>": "or",
    "<import>": "import",
    "<try>": "try:",
    "<except>": "except",
    "</except>": ":",
    "<from>": "from",
    "<loop>": "while True:",
    
}



def replacer(input_dict, input_string):
    output_string = input_string
    for key, value in input_dict.items():
        if key in input_string:
            start_index = 0
            while True:
                start_index = output_string.find(key, start_index)
                if start_index == -1:
                    break
                
                # Check if the key is between brackets
                if (output_string[start_index-1:start_index] == "(" and 
                    output_string[start_index+len(key):start_index+len(key)+1] == ")"):
                    start_index += len(key)
                    continue

                output_string = output_string[:start_index] + value + output_string[start_index+len(key):]
                start_index += len(value)
    return output_string

new_contents = replacer(converter, contents)
try:
    exec(new_contents)
except (SyntaxError, NameError) as e:
    _, _, exc_tb = sys.exc_info()
    print("\033[31m\033[1mPTML ERROR CAUGHT")
    print(f"In file: {fl}")
    print("         "+"^"*len(fl))
    print("Issue is that "+e.args[0])
    print(f"\033[35m\033[3mHelp: You fucked up in file: {fl} at line: {exc_tb.tb_lineno}\033[0m")
except Exception as e:
    print(traceback.format_exc())
finally:
    sys.exit()
