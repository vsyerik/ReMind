import unittest
from pathlib import Path
import tempfile
import shutil
from src.utils.file_finder import get_all_markdown_files

class TestFileFinder(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory structure
        self.test_dir = tempfile.mkdtemp()
        (Path(self.test_dir) / "sub").mkdir()
        (Path(self.test_dir) / "file1.md").write_text("# File 1")
        (Path(self.test_dir) / "file2.txt").write_text("Not markdown")
        (Path(self.test_dir) / "sub" / "file3.md").write_text("# File 3")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_get_all_markdown_files(self):
        files = get_all_markdown_files(Path(self.test_dir))
        file_names = sorted([f.name for f in files])
        self.assertEqual(file_names, ["file1.md", "file3.md"])

if __name__ == "__main__":
    unittest.main()
