#  tests for krb5-1.18.2-h75d18d8_0 (this is a generated file);
print('===== testing package: krb5-1.18.2-h75d18d8_0 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---

# just load libfreexl using ctypes
import os
import sys
import ctypes
import platform

bits, linkage = platform.architecture()
bits = bits[:2]

if sys.platform == 'win32':
    libfreexl = ctypes.CDLL('krb5_%s.dll' % bits)
elif sys.platform == 'darwin':
    # LD_LIBRARY_PATH not set on OSX or Linux
    path = os.path.expandvars('$PREFIX/lib/libkrb5.dylib')
    libfreexl = ctypes.CDLL(path)
else:
    path = os.path.expandvars('$PREFIX/lib/libkrb5.so')
    libfreexl = ctypes.CDLL(path)
#  --- run_test.py (end) ---

print('===== krb5-1.18.2-h75d18d8_0 OK =====');
