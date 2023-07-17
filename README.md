# Call C from Python **'c-from-python'**

Yet another example of calling **DLL** (Dynamic Link Library) from Python. More valuable is example of **command line**  invocations of Microsoft **Visual Studio** compiler and linker to compile and build DLL/.exe

## Requirements

Created with:
<br>
 - Microsoft (R) C/C++ Optimizing Compiler Version 19.36.32532 for x64
 - Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32

## Installation

Clone repository, and check build_local.bat. Use .py files as you would expect.

### Files
- primeGenDLL.c - C version of prime number generator (not particularly fast)
- primeGenApp.c - C file to create standalone .exe
- *pyCallCPrimeGen.py* - Python script that call C library (DLL)
- pyPrimeGenApp.py - native Python implementation of prime number generator used for comparisons

In case you want to just see example of calling DLL,  see: **\code\pyCallCPrimeGen.py**. Please change path variable accordingly. Example DLL is provided in _\build_ directory. <br>

If you would like to build DLL yourself using MS tool chain check **build_local.bat** file. Example requires **\code\primeGenDLL.c**.
<br>
First part is setting up environment variables, important part is:
```
::Build DLL
cl /LD  %scriptpath%\code\%filename%.c /Fe:%scriptpath%build\%filename%.dll /Fo:%scriptpath%build\%filename%.obj 

```

In case you would like to create standalone _.exe_ file use **\code\primeGenApp.c** and compile it with (add to build_local.bat):
```
::Build binary
cl /TC /Zi /c %scriptpath%\code\%filename%.c /Fo%scriptpath%build\ /Fd%scriptpath%build\%filename%.pdb /Fe%scriptpath%build
link -incremental:no /DEBUG %scriptpath%\build\*.obj /SUBSYSTEM:console /OUT:%scriptpath%\build\%filename%.exe

```

## Disclaimer

You can find faster prime number generators.


## Licence
MIT 

Copyright (c) Ilija Tatalovic, 2023.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
