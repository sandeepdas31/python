#using finally
import sys
s=['a',0,2]
for i in s:
    try:
        print("the value is", i)
        z=1/int(i)
        break
    except:
        print(sys.exc_info())

    finally:
        print("hola!")

print("the answer is", z )
