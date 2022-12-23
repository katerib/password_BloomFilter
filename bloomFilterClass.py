import hashlib
import sys
import math
from bitarray import bitarray


class BloomFilter:
    def __init__(self, m, p, n):
        self.size = m
        self.probability = p
        self.numEle = n
        self.numHash = int((m/n)*(math.log10(2)))
        self.arr = bitarray([0] * int(m))
        self.check = bitarray([0])
        self.first = 0
        self.last = int(self.size - 1)

    def hash_md5(self, item):
        encoded = hashlib.md5(item.encode())
        return int(encoded.hexdigest(), base=16)

    def hash_sha256(self, item):
        encoded = hashlib.sha256(item.encode())
        return int(encoded.hexdigest(), base=16)

    def hash_sha512(self, item):
        encoded = hashlib.sha512(item.encode())
        return int(encoded.hexdigest(), base=16)

    def calc_p(self, m, n):
        """
        calculate (p): possibility of false positive
        :param m: int ; size bit array
        :param n: int ; number of elements
        :return: int ; probability of false pos
        """
        return 0.5 ** (math.log10(2)) * (m / n)

    def insert(self, item):
        # hash function 1
        for count in range(self.numHash):
            index1 = int(self.hash_sha256(item+str(count)) % self.size)
        # print('index1: ', index1)
            self.arr[index1] = 1

    def lookup(self, item):
        for count in range(self.numHash):
            check1 = int(self.hash_sha256(item+str(count)) % self.size)
            if self.arr[check1] == 0:
                return False
        return True
