import sys
import utils.json_fns as fns

if len(sys.argv)>1:
    operation = sys.argv[1:][0]
    match operation:
        case 'read':
            fns.read_from_json()
        case 'write':
            msg = input("what is your msg? ")
            if msg:
                fns.write_to_json(msg)
else:
    print("no operator")
