import sys
import ciphers
import sys


sys.path.insert(1, "modules/")


from modules import pretty_print


def print_help() -> None:
    print("Not implemented yet.")


if len(sys.argv) == 1:
    print("No arguments specified.\n")
    print_help()
    sys.exit(1)

enc_msg = ciphers.caesar(sys.argv[1], int(sys.argv[2]), ciphers.ALPHA)

pretty_print.pretty_print(sys.argv[1], enc_msg, sys.argv[2])

