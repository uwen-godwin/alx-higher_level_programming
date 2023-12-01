def replace_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position."""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
