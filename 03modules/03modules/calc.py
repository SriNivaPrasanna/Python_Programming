import simple
import complex

from simple import *
ans = simple.add(1,2)
print(ans)

s = complex.sqr(5)
print(s)

from simple import add

print(add(3,4))

from simple import add
from complex import add

add(4)

print(dir())

def main():
        print(add(1,2))

print("calc:" ,__name__)

if __name__ == "__main__":
     main()

