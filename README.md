# Bloom Filters: Password Checker

A [bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) is a space-efficient probabilistic data structure based on hashing. It is used to check whether a specific element is present in a set.

## bloom.py

Elements are added to the bloom filter using the SHA-256 hash function. The bloom filter is created using a list of 14,341,564 leaked passwords from `rockyou.txt`. Then, the file passed as an argument in the command line (eg. 'dictionary.txt') is used to lookup values to test whether they exist in the bloom filter. If the element does not exist in the bloom filter, the program outputs 'no'. Otherwise, the program prints 'maybe' and validates the element's presence at a later step. The program then verifies the results and prints a report containing statistics for true/false positives/negatives and the time it took for the program to run.

### Calculations

The size of the bit array was calculated using the formula [m = -(N * log(p)) / (log(2)^2)] where `n` is the number of elements in the array, `p` is the probability of false positives, and `m` is the calculated bit array size. In this program, `p` was initialized to a value of 0.01 and `n` was calculated to be 14,346,469. Therefore, the size of the bit array was 316,632,489.

The number of hashing algorithms used was calculated using the formula [k = (m/n) * log(2)] where `m` is the size of the bit array, `n` is the number of elements in the array, and `k` is the calculated number of hashing algorithms. Six hashing algorithms were used in this program.

## About Bloom Filters

All bits in a bloom filter's bit array are set to 0 when created. Hash functions are used to map the elements to be 'added' to a specific array position. This means the value of the elements themselves are not added to the bit array. Rather, the bits at the indexes calculated using the hash functions are flipped from '0' to '1' to indicate an element has been added to that position. When looking up an element to see if it is contained in the bloom filter, the element undergoes the same hash algorithms to determine the indexes to check. If any of the indexes calculated are found to be set to '0', then the element is definitely not present in the set. However, if all indexes for the element are set to '1', there is still a chance for a **false positive**.

Probability of false positives (`p`) according to `n` number of elements and a bit array size of `m`:

<div style="text-align: center;"><img src="https://github.com/katerib/bloomFilter/blob/master/Images/false_positive_rate.png?raw=true" width="450" alt=""></div>

## Requirements

### Packages

The configuration file `requirements.txt` can be used to install all required packages. Run the command: 
```bash
pip install -r requirements.txt
```

Alternatively, [bitarray](https://pypi.org/project/bitarray/) can be manually installed with pip: `pip install bitarray`

### Files

The program imports a list of passwords from `rockyou.txt` to generate the initial bloom filter. This dictionary file is provided with the standard installation of Kali Linux. Other users can find this wordlist online (see [Kaggle](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt) or [GitHub](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)) and download it into the program's directory containing `bloom.py` `binarySearch.py` and `bloomFilterClass.py`

## Usage

At the command prompt, enter `py bloom.py [text file name]`

The argument `[text file name]` must contain a valid filename for a .txt file. An example file `dictionary.txt` is provided in the repository.

## Example Output

The following output is the result of the user inputting the `dictionary.txt` file to compare against `rockyou.txt`:

<div style="text-align: center;"><img src="https://github.com/katerib/bloomFilter/blob/master/Images/bloomFilterTestResults.png?raw=true" width="450" alt=""></div>
