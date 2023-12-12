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
    
    def ls(self, path=''):
        if not path:
            path = self.current_directory()
        print(os.listdir(path))
    
    def touch(self, file_name):
        open(file_name, 'a').close()
    
    def echo(self, lines, file_path, append=False):
        with open(file_path, 'a' if append else 'w') as f:
             for line in lines:
                f.write(line + '\n')
    
    def cat(self, file_path):
        with open(file_path, 'r') as f:
            print(f.read())
    
    def rm(self, file_path):
        os.remove(file_path)