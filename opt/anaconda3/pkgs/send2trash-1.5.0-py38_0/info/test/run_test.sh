

set -ex



echo test > test.txt
python -c "from send2trash import *; send2trash('test.txt')"
exit 0
