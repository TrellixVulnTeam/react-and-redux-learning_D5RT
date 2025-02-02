#  tests for h5py-2.10.0-py38h3134771_0 (this is a generated file);
print('===== testing package: h5py-2.10.0-py38h3134771_0 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---
import h5py
import h5py._conv
import h5py._errors
import h5py._objects
import h5py._proxy
import h5py.defs
import h5py.h5
import h5py.h5a
import h5py.h5d
import h5py.h5f
import h5py.h5fd
import h5py.h5g
import h5py.h5i
import h5py.h5l
import h5py.h5o
import h5py.h5p
import h5py.h5r
import h5py.h5s
import h5py.h5t
import h5py.h5z
import h5py.utils

import numpy as np

from sys import exit

# test file read/write, regression test for https://github.com/ContinuumIO/anaconda-issues/issues/7686
fh = h5py.File('test.h5', 'w')
fh.create_group('/top')
fh['/top'].attrs['attr1'] = 'Test Attribute 1'
fh['/top'].attrs['attr2'] = 'Test Attribute 2'
fh['/top'].create_dataset('image', data=np.arange(1000)/3.0)
fh.flush()
fh.close()

fh = h5py.File('test.h5', 'r')
fh['/top'].attrs['attr1']

exit(h5py.run_tests())
#  --- run_test.py (end) ---

print('===== h5py-2.10.0-py38h3134771_0 OK =====');
print("import: 'h5py'")
import h5py

