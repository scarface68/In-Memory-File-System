import os

class FileSystem:
    def current_directory(self):
        return os.getcwd()
    
    def mkdir(self, directory_name):
        os.mkdir(directory_name)
    
    def cd(self, path):
        if path == '~':
            os.chdir('/')
        else:
            os.chdir(path)
    
    def ls(self, all_flag, path):
        if not path:
            path = self.current_directory()
        items = os.listdir(path)
        if not all_flag:
            items = [item for item in items if not item.startswith('.')]
        print(' '.join(items))
    
    def touch(self, file_name):
        open(file_name, 'a').close()
    
    def echo(self, lines, file_path, append=False):
        with open(file_path, 'a' if append else 'w') as f:
             for line in lines:
                f.write(line + '\n')
    
    def cat(self, file_path):
        with open(file_path, 'r') as f:
            print(f.read())
    
    def rm(self, path):
        if os.path.exists(path):
            if(os.path.isdir(path)):
                os.rmdir(path)
            else:
                os.remove(path)
        else:
            print("The file or directory does not exist")
    
    def mv(self, source_path, destination_path):
        os.rename(source_path, destination_path)