def main(list1):
    ans=[]
    for i in list(list1):
        if int(i)==1:
            ans+=[1]
        if int(i)==0:
            ans+=[False]
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    return ans
print(main('10110'))