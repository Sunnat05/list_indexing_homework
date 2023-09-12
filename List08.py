def main(list1):
    ans=[]
    for i in list(list1):
        if int(i)==1:
            ans+=[True]
        if int(i)==0:
            ans+=[False]
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    return ans
print(main('10111'))