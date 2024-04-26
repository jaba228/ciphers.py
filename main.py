import sys
import ciphers


def print_help() -> None:
    print("Not implemented yet.")


if len(sys.argv) == 1:
    print("No arguments specified.\n")
    print_help()
    sys.exit(1)

print(ciphers.caesar(sys.argv[1], int(sys.argv[2]), ciphers.ALPHA))
