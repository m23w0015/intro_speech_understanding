
def list_to_dict(input_list):
    '''
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`. 
    '''
    import importlib, homework4
    importlib.reload(homework4)

    print(homework4.list_to_dict([1, 3.14, "hello", True])) 
    print(homework4.list_to_dict(["a", "a", "a"]))           
    print(homework4.list_to_dict([]))                       




