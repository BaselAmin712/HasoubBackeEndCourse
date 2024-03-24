import sys
import utils.json_fns as fns
from utils.input import *

if len(sys.argv)>1:
    operation = sys.argv[1:][0]
    match operation:
        case 'read':
            fns.read_from_json()
        case 'write':
            try:
                fns.write_to_json(get_input())
            except Exception as error:
                print("you did not write any thing!")
                print(error)

else:
    print("no operator")
