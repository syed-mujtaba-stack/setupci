from src.main import greet

def test_greet():
    assert greet("setupci") == "Hello, setupci!"
    assert greet() == "Hello, World!"
