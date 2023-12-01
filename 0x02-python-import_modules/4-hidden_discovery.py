#!/usr/bin/python3
#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    f_names = dir(hidden_4)
    for f_name in f_names:
        if f_name[:2] != "__":
            print(f_name)
