import os
import sys

### template
if os.getenv("LOCAL"):
    sys.stdin = open("in.txt", "r")
    sys.stdout = open("out.txt", "w")
input = sys.stdin.readline
def show(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
### template
