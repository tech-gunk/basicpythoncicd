import os

def install_node_module(module):
    cmd = 'npm install --save ' + module
    print(cmd)
    os.system(cmd)

def install_python_module(module):
    cmd = 'python -m pip install ' + module
    print(cmd)
    os.system(cmd)

def runfile(file, lang):
    if lang == 'python':
        cmd = 'python ' + file
    elif lang == 'node':
        cmd = 'node ' + file
    print(cmd)
    os.system(cmd)

def takeUserInput():
    print('Type 1 to install node modules')
    print('Type 2 to install python modules')
    print('Type 3 to run a file')
    choice = input('Enter your choice: ')
    if choice == '1':
        mod = input('Enter the module name: ')
        install_node_module(mod)
        takeUserInput()
    elif choice == '2':
        mod = input('Enter the module name: ')
        install_python_module(mod)
        takeUserInput()
    elif choice == '3':
        file = input('Enter the file name: ')
        print('"python" or "node"')
        lang = input('Enter the language: ')
        runfile(file, lang)
        takeUserInput()

takeUserInput()
