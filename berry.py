import os, shutil
import concurrent.futures
import django
import sys
import typer


#list object to hold the names of all the modules to be included in BerryEnv
modules = []

#check if command line argument is greater than 2 i.e berry.py {name of module}

while True:
    module = input("Enter name of module you'd like to add to you virtual environment \n"
    "press enter to stop:")
    if module != "":
        modules.append(module)
    else:
        break       #add every other passed argument to module's list

print(modules)
#list object to hold the paths to each module passed in as an argument
paths_to_modules = []

import importlib
for module in modules:
    try:
        path_to_module = importlib.import_module(module).__file__ #get path to module 
        #print(path_to_module)
        #print(os.path.join(os.path.dirname(path_to_module), os.path.basename(path_to_module)))
        paths_to_modules.append(path_to_module) #append path the modules to paths_to_module's list
    except Exception as err:
        print(err)    

 

dest = os.path.join(os.getcwd(), os.path.basename(path_to_module))



def copy_module(pathh):
    path=os.path.join(os.path.dirname(pathh), os.path.basename(pathh))

    if os.path.isdir(path):
        try:
            shutil.copytree(path, dest, copy_function= shutil.copy2)
            return "Finished Recursive Copy!"
        except NotADirectoryError as err:
            return f"program ran into this problem ============>>>>{err}"

    elif os.path.isfile(path):
        try:
            shutil.copyfile(path, dest)
            return "Finished Recursive Copy!"
        except NotADirectoryError as err:
            return f"program ran into this problem ============>>>>{err}"

    return "Operation not recognised!"

def threader():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        paths = paths_to_modules
        results = executor.map(copy_module, paths)

        for result in results:
            print(result)

threader()



