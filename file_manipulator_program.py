import sys

def main():
    if len(sys.argv) < 3:
        print("system: python fileManipulatorProgram.py <instruction> <input_file_path> [additional_args]")
        sys.exit(1)
    instruction = sys.argv[1]
    input_file_path = sys.argv[2]

    if instruction == 'reverse':
        if len(sys.argv) < 4:
            print("system: python fileManipulatorProgram.py reverse <input_file_path> <output_file_path>")
            sys.exit(1)
        output_file_path = sys.argv[3]
        do_reverse(input_file_path, output_file_path)
        print('system: Complete reverse')
    elif instruction == 'copy':
        if len(sys.argv) < 4:
            print("system: python fileManipulatorProgram.py copy <input_file_path> <output_file_path>")
            sys.exit(1)
        output_file_path = sys.argv[3]
        do_copy(input_file_path, output_file_path)
        print('system: Complete copy')
    elif instruction == 'duplicate-contents':
        if len(sys.argv) < 4:
            print("system: python fileManipulatorProgram.py duplicate-contents <input_file_path> <n>")
            sys.exit(1)
        n = sys.argv[3]
        do_duplicate(input_file_path, n)
        print('system: Complete duplicate')
    elif instruction == 'replace-string':
        if len(sys.argv) < 5:
            print("system: python fileManipulatorProgram.py replace-string <input_file_path> <old_string> <new_string>")
            sys.exit(1)
        old_string = sys.argv[3]
        new_string = sys.argv[4]
        do_replace(input_file_path, old_string, new_string)
        print('system: Complete replace')
    else:
        print("system: python fileManipulatorProgram.py <instruction> <input_file_path> [additional_args]")
        sys.exit(1)

def do_reverse(input_file_path, output_file_path):
    contents = ''
    with open(input_file_path, encoding='utf-8') as f:
        contents = f.read()
    with open(output_file_path, 'w') as f:
        reverse_contents = do_reverse_contents(contents)
        f.write(reverse_contents)

def do_reverse_contents(contents):
    arr = []
    for content in reversed(contents):
        arr.append(content)
    return ''.join(arr)

def do_copy(input_file_path, output_file_path):
    contents = ''
    with open(input_file_path, encoding='utf-8') as f:
        contents = f.read()
    
    with open(output_file_path, 'x') as f:
        f.write(contents)

def do_duplicate(input_file_path, n):
    contents = ''
    try:
        n = int(n)
    except ValueError:
        sys.exit('system: Enter a number in <n>')
    with open(input_file_path, encoding='utf-8') as f:
        contents = f.read()
    
    with open(input_file_path, 'a') as f:
        for i in range(n):
            f.write('\n' + contents)

def do_replace(input_file_path, old_string, new_string):
    contents = ''
    with open(input_file_path, encoding='utf-8') as f:
        contents = f.read()
    
    with open(input_file_path, 'w') as f:
        replaced_contents = replace_needle(contents, old_string, new_string)
        f.write(replaced_contents)

def replace_needle(contents, old_string, new_string):
    if not old_string in contents:
        return contents
    return replace_needle(contents.replace(old_string, new_string), old_string, new_string)

main()