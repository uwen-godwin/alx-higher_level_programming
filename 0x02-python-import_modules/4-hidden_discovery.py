#!/usr/bin/python3
if __name__ == "__main__":
    """print all modules defined_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:3] != "__":
            print(name)
