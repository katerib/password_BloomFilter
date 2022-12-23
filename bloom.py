import math
import time
import sys
from bloomFilterClass import BloomFilter
from binarySearch import binary_search

start = time.time()
# get leaked data
with open('rockyou.ISO-8859-1.txt', encoding='ISO_8859-1') as load:
    loaded = load.read().splitlines()
loaded.sort()

# get input data
with open(sys.argv[1], 'r') as in_file:
    data = in_file.read().splitlines()
data.sort()

'''
generate bitarray size = -[(n * log(p))/(log(2)^2)]
if len(data) > len(loaded):
    num_elements = len(data)
otherwise:
    num_elements = len(loaded)
'''
num_elements = len(loaded)
probability = 0.01
size = int(-(num_elements * math.log10(probability)) / (math.log10(2)**2))

# create bloom filter class
bf = BloomFilter(size, probability, num_elements)
# insert leaked data
print("...inserting leaked data from {} to bloom filter...".format(sys.argv[1]))
for item in loaded:
    bf.insert(item)
print("...finished loading leaked data to bloom filter...")

# initialize variables to store "no" and "maybe" response
check_neg = []
check_pos = []

# lookup input data
print("...checking if input data exists...")

for item in data:
    result = bf.lookup(item)
    if result is False:
        check_neg.append(item)
        print("no")
    else:
        check_pos.append(item)
        print("maybe")
print("...done checking input data...")
print("...validating results...")

# initialize report variables
true_neg = 0
false_neg = 0
false_pos = 0
true_pos = 0

# sort values to check
check_neg.sort()
check_pos.sort()
# perform validations / checks
for item in check_neg:
    result = binary_search(loaded, item, len(loaded))
    if result is False:
        true_neg += 1
    else:
        false_neg += 1
for item in check_pos:
    result = binary_search(loaded, item, len(loaded))
    if result is False:
        false_pos += 1
    else:
        true_pos += 1

end = time.time()

# print report calculations
print("BLOOM FILTER INFO: ")
print("  imported file: 'rockyou.ISO-8859-1.txt'")
print("  input file: '{}'".format(sys.argv[1]))
print("  num elements added (n): ", bf.numEle)
print("  size of array (m): ", bf.size)
print("  probability of false pos (p): ", bf.probability)
print("  num hash functions used (k): ", bf.numHash)
print("PROGRAM TOOK {} SECONDS TO RUN".format(int(end-start)))
print("--------")
print("RESULTS: ")
print("  true negatives: ", true_neg)
print("  false negatives: ", false_neg)
print("  true positives: ", true_pos)
print("  false positives: ", false_pos)

# calculate actual false pos rate
if (false_pos + true_neg) == 0:
    actual_fp = 0
else:
    actual_fp = false_pos / (false_pos + true_neg)

print("~ false positive rate: ", actual_fp)

