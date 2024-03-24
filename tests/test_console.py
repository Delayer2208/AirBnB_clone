import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Unittests for console.py covering all features."""

    def setUp(self):
        """Set up the test environment."""
        self.console = HBNBCommand()
        self.test_file = "test_file.json"

    def tearDown(self):
        """Tear down the test environment."""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_show(self):
        """Test show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id_created = f.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(id_created))
            self.assertTrue("BaseModel" in f.getvalue())

    def test_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id_created = f.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(id_created))
            self.assertFalse(os.path.exists(self.test_file))

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create State")
            self.console.onecmd("all")
            self.assertTrue("BaseModel" in f.getvalue())
            self.assertTrue("User" in f.getvalue())
            self.assertTrue("State" in f.getvalue())

    def test_update(self):
        """Test update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id_created = f.getvalue().strip()
            self.console.onecmd("update BaseModel {} name 'Holberton'".format(id_created))
            self.console.onecmd("show BaseModel {}".format(id_created))
            self.assertTrue("'name': 'Holberton'" in f.getvalue())

    def test_help(self):
        """Test help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertTrue("Documented commands (type help <topic>):" in f.getvalue())

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertTrue(len(f.getvalue()) == 0)

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertTrue(len(f.getvalue()) == 0)


if __name__ == "__main__":
    unittest.main()
