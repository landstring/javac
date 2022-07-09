import os 

def dfs(repository, name):
    file_list = os.listdir(repository) #список файлов текущего каталога

    folders = [] #папки текущего каталога 
    paths = [] #файлы текущего каталога 

    for f in file_list:
        if '.java' in f:
            if f == name:
                paths = [repository + '/' + f] + paths
            else:
                paths.append(repository + '/' + f)
        elif not '.' in f:
            folders.append(f)

    for folder in folders:
        result_dfs = dfs(repository + '/' + folder, name)
        for path in result_dfs:
            paths.append(path)
    return paths


    

folder = input("Enter the name of project's folder: ") #ввод папки проекта
name = input("Enter the name of main project's file: ") #ввод главного файла, который запустит нам весь проект
args = input("Enter args with space between: ") #для аргументов заупуска String[] args

paths = dfs('./' + folder, name)

gen_bat = ""
for path in paths:
    gen_bat += "javac " + path + '\n' 

gen_bat += "java " + paths[0][2:-5] + ' ' + args + '\n'
gen_bat += "pause"

result = open("run.bat", "w")
result.write(gen_bat)
result.close()

