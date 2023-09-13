def main(list1):
    for i in list1:
        if i!=list1[0]:
            return False
    return True
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
print(main([0,0,0,0]))