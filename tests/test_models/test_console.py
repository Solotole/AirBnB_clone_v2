#!/usr/bin/python3
""" console test script """

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage


class TestStateConsole(unittest.TestCase):
    """ testing new improved features """
    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="carlifornia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], "carlifornia")

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="carli"fornia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], 'carli"fornia')

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="carl_if_ornia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], "carl if ornia")

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="c_arlifornia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], "c arlifornia")

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="carlif"orn_ia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], 'carlif"orn ia')

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="carl"_ifornia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], 'carl" ifornia')

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="carli_"fornia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], 'carli "fornia')

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="carlifornia""')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], 'carlifornia"')

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name=""carlifornia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], '"carlifornia')

    @patch('sys.stdout', new=StringIO())
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd('create State name="_carlifornia"')
        output = mock_stdout.getvalue().strip()
        key = "State" + output
        dictionary = storage.FileStorage.__objects
        new_dict = dictionary[key]
        self.assertEqual(new_dict.__dict__[name], " carlifornia")

class Test
if __name__ == '__main__':
    unittest.main(__name__)
