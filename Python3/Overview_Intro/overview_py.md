### 1. Is python compiled or Interpreted

### Ans:

```diff
Python is both compiled and iterpreted language , 

-compiler:
+ Computers  work on Machine languages so we have to convert the code into the machine language  by the use of the compiler 
convert the high to low or low to high language 

- python first gets the compiled into the byte code
- Byte code is interpreted into the Machine language by the python virtual Machine
! Interpreter ; it reaches by line by line or execute it line by line


+ In python we use the concept of converting the byte the code to achieve the portability for platform independance

! Portability:  Write the code once and use it on the different platform or machines 

-to solve the problem of having the machine different cpu architecture , we uses the virtual machine , run the byte code and convert in the native code
-: Here the virtual machine is meant by the PVM(Py virtual Machine) , like JVM in java.

! In the python itself handle the compilation

+ cpython

- the actual implemenation is done using c like  cpython for python, or it is implemented in the c language like the pypy , jpython, ironpython.

```
