#  tests for pycurl-7.43.0.5-py38ha12b0ac_0 (this is a generated file);
print('===== testing package: pycurl-7.43.0.5-py38ha12b0ac_0 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---
import curl
import pycurl
try:
    from cStringIO import StringIO as BytesIO
except:
    from io import BytesIO

buf = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, 'https://repo.continuum.io/')
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()

print(buf.getvalue())
assert b'Anaconda, Inc.' in buf.getvalue()
buf.close()
#  --- run_test.py (end) ---

print('===== pycurl-7.43.0.5-py38ha12b0ac_0 OK =====');
print("import: 'curl'")
import curl

print("import: 'pycurl'")
import pycurl

