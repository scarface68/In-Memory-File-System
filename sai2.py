import os
import shutil
from distutils.dir_util import copy_tree

class FileSystem:
    def current_directory(self):
        return os.getcwd()
    
    def clear(self):
        os.system('cls||clear')
    
    def mkdir(self, directory_name):
        os.mkdir(directory_name)
    
    def cd(self, path):
        if not os.path.exists(path):
            print("No such file or directory")
            return
        if path == '~':
            os.chdir('/')
        else:
            os.chdir(path)
    
    def ls(self, all_flag, path):
        if not path:
            path = self.current_directory()
        elif not os.path.exists(path):
            print("No such file or directory")
            return
        items = os.listdir(path)
        if not all_flag:
            items = [item for item in items if not item.startswith('.')]
        print(' '.join(items))
    
    def touch(self, file_name):
        open(file_name, 'a').close()
    
    # handle if file does not exist
    def echo(self, lines, file_path, append=False):
        with open(file_path, 'a' if append else 'w') as f:
             for line in lines:
                f.write(line + '\n')
    
    def cat(self, file_path):
        if not os.path.exists(file_path):
            print("No such file or directory")
            return
        with open(file_path, 'r') as f:
            print(f.read())
    
    def rm(self, path, rf_flag=False):
        if os.path.exists(path):
            if(os.path.isdir(path)):
                if(rf_flag): os.rmdir(path)
                else: print("rm: cannot remove '"+path+"': Is a directory")
            else:
                os.remove(path)
        else:
            print("No such file or directory")
    
    def mv(self, source_path, destination_path):
        if os.path.isdir(source_path) and not os.path.isdir(destination_path):
            print("mv: cannot overwrite non-directory '" + destination_path + "' with directory '"+source_path+"'")
            return
        if os.path.isdir(destination_path):
            fileName = source_path.split('/')[-1]
            destination_path = destination_path + '/' + fileName
        os.rename(source_path, destination_path)
    
    def cp(self, source_path, destination_path, flag):
        if(not os.path.exists(source_path)):
            print("cp: cannot stat '"+source_path+"': No such file or directory")
            return
        if(not flag and os.path.isdir(source_path)):
            print("cp: -r not specified; omitting directory '"+source_path+"'")
            return
            
        if os.path.isdir(source_path) and os.path.exists(destination_path) and not os.path.isdir(destination_path):
            print("cp: cannot overwrite non-directory '" + destination_path + "' with directory '"+source_path+"'")
            return
        elif source_path == destination_path:
            if(os.path.isdir(source_path)):
                folderName = source_path.split('/')[-1]
                print("cp: cannot copy a directory, '"+source_path+"', into itself, '"+source_path+folderName+"'")
                return
            else: print("cp: '" + source_path + "' and '"+destination_path+"' are the same file")
            return
        
        if os.path.isdir(source_path):
            if(os.path.exists(destination_path)):
                folderName = source_path.split('/')[-1]
                destination_path = destination_path + '/' + folderName
                shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
            else: shutil.copytree(source_path, destination_path)
            return
        
        if os.path.isdir(destination_path):
            fileName = source_path.split('/')[-1]
            destination_path = destination_path + '/' + fileName
        shutil.copy(source_path, destination_path)
    
    def grep(self, file_path, pattern, case_sensitive, whole_words, count_flag):
        if not os.path.exists(file_path):
            print(f"grep: {file_path}: No such file or directory")
            return
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the contents of the file
            contents = file.readlines()

        # Initialize counter variable
        counter = 0

        # Iterate over each line in the contents
        for line in contents:
            # Check if the pattern is found in the line
            if case_sensitive:
                if whole_words:
                    if f" {pattern.strip()} " in f" {line.strip()} ":
                        if not count_flag:
                            print(line)
                        counter += 1
                else:
                    if pattern in line:
                        if not count_flag:
                            print(line)
                        counter += 1
            else:
                if whole_words:
                    if f" {pattern.lower().strip()} " in f" {line.lower().strip()} ":
                        if not count_flag:
                            print(line)
                        counter += 1
                else:
                    if pattern.lower() in line.lower():
                        if not count_flag:
                            print(line)
                        counter += 1

        # Print counter variable if count_flag is True
        if count_flag:
            print(counter)