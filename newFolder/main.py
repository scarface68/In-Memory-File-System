import FileSystem

def main():
    file_system = FileSystem.InMemoryFileSystem()

    while True:
        command = input(f'{file_system.current_directory["path"]}$ ')
        if command.startswith('mkdir '):
            _, directory_name = command.split(' ', 1)
            file_system.mkdir(directory_name)
        elif command.startswith('cd '):
            _, path = command.split(' ', 1)
            file_system.cd(path)
        elif command.startswith('ls'):
            if len(command.split()) > 1:
                _, path = command.split(' ', 1)
                file_system.ls(path)
            else:
                file_system.ls()
        elif command.startswith('grep '):
            _, rest = command.split(' ', 1)
            pattern, file_path = rest.split(' ', 1)
            result = file_system.grep(pattern, file_path)
            print(result)
        elif command.startswith('cat '):
            _, file_path = command.split(' ', 1)
            file_system.cat(file_path)
        elif command.startswith('touch '):
            _, file_name = command.split(' ', 1)
            file_system.touch(file_name)
        elif command.startswith('echo '):
            _, rest = command.split(' ', 1)
            text, file_path = rest.split('>', 1)
            file_system.echo(text.strip(), file_path.strip())
        elif command.startswith('mv '):
            _, paths = command.split(' ', 1)
            source_path, destination_path = paths.split()
            file_system.mv(source_path, destination_path)
        elif command.startswith('cp '):
            _, paths = command.split(' ', 1)
            source_path, destination_path = paths.split()
            file_system.cp(source_path, destination_path)
        elif command.startswith('rm '):
            _, file_path = command.split(' ', 1)
            file_system.rm(file_path)
        elif command == 'exit':
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()