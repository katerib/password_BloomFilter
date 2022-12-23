# Bloom Filter

## Requirements

Use pip to install bitarray: https://pypi.org/project/bitarray/
```bash
pip install bitarray
```

>> bloom.py uses binarySearch.py , bloomFilterClass.py

```python
import math
import time
import sys
from bloomFilterClass import BloomFilter
from binarySearch import binary_search
```


## Usage

At the command prompt, type `py bloom.py [text file name]`


## Description

Program imports a list of leaked passwords from 'rockyou.ISO-8859-1.txt'. A bloom filter is created from these
preloaded values. Then, the file passed as an argument in the command line (eg. 'dictionary.txt') is used to
lookup values and see if they are already present in the bloom filter.

Prints program stats, including values of: true negatives, false negatives, false positives, true positives