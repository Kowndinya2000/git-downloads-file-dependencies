import os
arr = os.listdir('.')
for repo in arr:
    if(repo == 'app.py'):
        print('not included') 
    else:
        thisdir = repo 
        cpp_modules = []
        cpp_files = []
        for r, d, f in os.walk(thisdir):
            for file in f:
                if("." in file):
                    continue
                else:
                    cpp_modules.append(file)
        for r, d, f in os.walk(thisdir):
            for file in f:
                if(file.endswith(".cpp")):
                    print()

                    
