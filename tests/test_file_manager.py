import os
import pytest
from pyfakefs.fake_filesystem_unittest import Patcher

from app.file_management import FileManager


# Test Cases
@pytest.fixture
def fs():
    """Fixture to initialize pyfakefs."""
    with Patcher() as patcher:
        yield patcher

def test_write_file_positive(fs):
    """Test writing to a file successfully."""
    file_manager = FileManager("test_file.txt")
    file_manager.write_file("Hello, World!")

    # Check if the file exists in the fake filesystem
    assert fs.fs.exists("test_file.txt")

    # Read the content to verify
    with open("test_file.txt", 'r') as file:
        content = file.read()
        assert content == "Hello, World!"

def test_read_file_positive(fs):
    """Test reading from a file successfully after writing."""
    fs.fs.create_file("test_file.txt", contents="Hello, World!")  # Correctly use the fake filesystem

    file_manager = FileManager("test_file.txt")
    content = file_manager.read_file()

    assert content == "Hello, World!"

def test_delete_file_positive(fs):
    """Test deleting a file successfully."""
    fs.fs.create_file("test_file.txt", contents="Hello, World!")  # Correctly use the fake filesystem

    file_manager = FileManager("test_file.txt")
    file_manager.delete_file()

    assert not fs.fs.exists("test_file.txt")

def test_read_file_negative(fs):
    """Test reading from a non-existent file."""
    file_manager = FileManager("non_existent_file.txt")

    with pytest.raises(FileNotFoundError):
        file_manager.read_file()

def test_delete_file_negative(fs):
    """Test deleting a non-existent file."""
    file_manager = FileManager("non_existent_file.txt")
    # This should not raise an error, just check no error is raised
    file_manager.delete_file()  # No assertion needed; just check no error is raised
