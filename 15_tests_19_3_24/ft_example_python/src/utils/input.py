def get_input():
    msg = input("what is your msg? ")
    if msg:
        return msg
    else:
        raise Exception("empty massage")