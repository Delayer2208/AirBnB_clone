import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Unit tests for console.py"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def test_help(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("help")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_help_specific_command(self):
        """Test help command for a specific command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("help show")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Show command documentation", output)

    def test_quit(self):
        """Test the quit command"""
        with self.assertRaises(SystemExit) as e:
            self.console.onecmd("quit")

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(obj_id))
            output = mock_stdout.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_destroy(self):
        """Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.console.onecmd("show BaseModel {}".format(obj_id))
            output = mock_stdout.getvalue().strip()
            self.assertIn("** no instance found **", output)

    # Add more test cases for other commands such as update, all, count, etc.

if __name__ == '__main__':
    unittest.main()
