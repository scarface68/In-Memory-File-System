import os

class FileSystem:
    def current_directory(self):
        return os.getcwd()
    
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
    
    def rm(self, path):
        if os.path.exists(path):
            if(os.path.isdir(path)):
                os.rmdir(path)
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