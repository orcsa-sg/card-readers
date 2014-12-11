import sys, re

print("".join(re.sub(r'([^0-9]|^)([0-9]{16})([^0-9]|$)',
                     r'%"\2^FIRST/LAST^0000000000000000000   000      ?;'
                     r'\2=00000000000000000?', x) for x in sys.stdin))