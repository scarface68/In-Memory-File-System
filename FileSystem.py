import os

class InMemoryFileSystem:
    def __init__(self):
        self.root = {'type': 'dir', 'contents': {}, 'path': '/'}
        self.current_directory = self.root
    
    def mkdir(self, directory_name):
        new_directory = {'type': 'dir', 'contents': {}, 'path': ''}
        self.current_directory['contents'][directory_name] = new_directory

    def cd(self, path):
        if path == '/':
            self.current_directory = self.root
        elif path.startswith('/'):
            self.navigate_absolute_path(path)
        else:
            self.navigate_relative_path(path)

    def ls(self, path=''):
        if not path:
            contents = self.current_directory['contents']
        else:
            contents = self.get_directory_by_path(path)['contents']

        for name, item in contents.items():
            if item['type'] == 'dir':
                print(f'{name}/')
            else:
                print(name)

    def grep(self, pattern, file_path):
        try:
            file_content = self.get_file_content(file_path)
            lines = file_content.split('\n')
            matching_lines = [line for line in lines if pattern in line]
            return '\n'.join(matching_lines)
        except Exception as e:
            return f"Error: {e}"

    def cat(self, file_path):
        try:
            file_content = self.get_file_content(file_path)
            print(file_content)
        except Exception as e:
            print(f"Error: {e}")

    def touch(self, file_name):
        new_file = {'type': 'file', 'content': ''}
        self.current_directory['contents'][file_name] = new_file

    def echo(self, text, file_path):
        try:
            file = self.get_file_by_path(file_path)
            file['content'] = text
        except Exception as e:
            print(f"Error: {e}")

    def mv(self, source_path, destination_path):
        try:
            source_item = self.get_item_by_path(source_path)
            destination_item = self.get_directory_by_path(destination_path)
            destination_item['contents'][source_item['name']] = source_item
            del self.get_directory_by_path(os.path.dirname(source_path))['contents'][source_item['name']]
        except Exception as e:
            print(f"Error: {e}")

    def cp(self, source_path, destination_path):
        try:
            source_item = self.get_item_by_path(source_path)
            destination_item = self.get_directory_by_path(destination_path)
            destination_item['contents'][source_item['name']] = source_item.copy()
        except Exception as e:
            print(f"Error: {e}")

    def rm(self, path):
        try:
            parent_directory = self.get_directory_by_path(os.path.dirname(path))
            del parent_directory['contents'][os.path.basename(path)]
        except Exception as e:
            print(f"Error: {e}")

    def navigate_absolute_path(self, path):
        path_components = path.split('/')
        current_directory = self.root
        for component in path_components[1:]:
            if component == '..':
                current_directory = self.get_parent_directory(current_directory)
            else:
                current_directory = current_directory['contents'][component]
        self.current_directory = current_directory

    def navigate_relative_path(self, path):
        path_components = path.split('/')
        current_directory = self.current_directory
        for component in path_components:
            if component == '..':
                current_directory = self.get_parent_directory(current_directory)
            else:
                current_directory = current_directory['contents'][component]
        self.current_directory = current_directory

    def get_directory_by_path(self, path):
        if path == '/':
            return self.root
        path_components = path.split('/')
        current_directory = self.root
        for component in path_components[1:]:
            current_directory = current_directory['contents'][component]
        return current_directory

    def get_parent_directory(self, directory):
        path_components = directory['path'].split('/')
        parent_path = '/'.join(path_components[:-1]) or '/'
        return self.get_directory_by_path(parent_path)

    def get_item_by_path(self, path):
        directory = self.get_directory_by_path(os.path.dirname(path))
        item_name = os.path.basename(path)
        return directory['contents'][item_name]

    def get_file_content(self, file_path):
        file = self.get_file_by_path(file_path)
        return file['content']

    def get_file_by_path(self, path):
        file_name = os.path.basename(path)
        directory = self.get_directory_by_path(os.path.dirname(path))
        return directory['contents'][file_name]