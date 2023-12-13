import unittest
from filesystemclass import FileSystem

class FileSystemTests(unittest.TestCase):
    def setUp(self):
        # Create an instance of the FileSystem class
        self.fs = FileSystem()

    def test_mkdir(self):
        # Test creating a directory
        self.fs.mkdir("test_dir")
        self.assertIn("test_dir", self.fs.ls(False, self.fs.current_directory()))
        self.fs.rm("test_dir", True)

    def test_touch(self):
        # Test creating a file
        self.fs.touch("test_file.txt")
        self.assertIn("test_file.txt", self.fs.ls())
        self.fs.rm("test_file.txt")

    def test_ls(self):
        # Test listing the contents of the filesystem
        self.fs.mkdir("test_dir")
        self.fs.touch("./test_dir/test_file.txt")
        self.assertEqual(self.fs.ls(False, "./test_dir"), ["test_file.txt"])
        self.fs.rm("test_dir", True)
        
    def test_rm(self):
        # Test removing a file
        self.fs.touch("test_file.txt")
        self.fs.rm("test_file.txt")
        self.assertNotIn("test_file.txt", self.fs.ls())
    
    def test_cd(self):
        # Test changing directory
        self.fs.mkdir("test_dir")
        root = self.fs.current_directory()
        self.fs.cd("test_dir")
        self.assertEqual(self.fs.current_directory(), root + "/test_dir")
        self.fs.cd("..")
        self.assertEqual(self.fs.current_directory(), root)
        self.fs.rm("test_dir", True)
    
    def test_echo(self):
        # Test writing to a file
        self.fs.touch("test_file.txt")
        self.fs.echo(["test"], "test_file.txt")
        with open("test_file.txt", "r") as f:
            self.assertEqual(f.read(), "test\n")
        self.fs.rm("test_file.txt")
        
    def test_cat(self):
        # Test reading a file
        self.fs.touch("test_file.txt")
        self.fs.echo(["test"], "test_file.txt")
        self.assertTrue(self.fs.cat("test_file.txt") == "test\n")
        self.fs.rm("test_file.txt") 
               
    def test_cp(self):
        # Test copying a file
        self.fs.touch("test_file.txt")
        self.fs.cp("test_file.txt", "test_file_copy.txt", False)
        self.assertIn("test_file_copy.txt", self.fs.ls())
        self.fs.rm("test_file.txt")
        self.fs.rm("test_file_copy.txt")
    
    def test_mv(self):
        # Test moving a file
        self.fs.touch("test_file.txt")
        self.fs.mv("test_file.txt", "test_file_copy.txt")
        self.assertNotIn("test_file.txt", self.fs.ls())
        self.assertIn("test_file_copy.txt", self.fs.ls())
        self.fs.rm("test_file_copy.txt")
    
    def test_grep(self):
        # Test searching for a string in a file
        self.fs.touch("test_file.txt")
        self.fs.echo(["test"], "test_file.txt")
        self.assertTrue(self.fs.grep("test_file.txt", "test",  count_flag=True) == 1)
        self.fs.rm("test_file.txt")
    

if __name__ == '__main__':
    unittest.main()