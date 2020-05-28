#!/bin/python

import numpy as np

class Solution():

    def __init__(self, positions):
        self.positions = positions

    def check(self):
        self.allowed_lengths = []
        for i in range(0,len(self.positions)):
            for j in range(i,len(self.positions)):
                if i == 3 and j == 4:
                    continue
                if i == 0 and j == 0:
                    continue
                self.allowed_lengths.append(np.round(np.linalg.norm(np.array([i,j])), 2))

        for i in range(0,len(self.positions)):
            for j in range(i,len(self.positions)):
                if i == j:
                    continue
                length = np.round(np.linalg.norm(self.positions[i] - self.positions[j]), 2)
                if length in self.allowed_lengths:
                    self.allowed_lengths.remove(length)
                else:
                    return False
        return True

if __name__ == "__main__":
    dim = int(input("Size of grid to solve: "))
    positions = [0 for i in range(0,dim)]
    array = [0 for i in range(0,2*dim)]
    while True:
        for i in range(0,2*dim,2):
            positions[int(i/2)] = np.array([array[i],array[i+1]])
        if Solution(positions).check(): # If solves the system print it
            print(positions)
        index = 0
        while True: # One iteration by the time we break
            if array[index] == dim - 1:
                array[index] = 0
                index += 1
                continue
            else:
                array[index] += 1
                break

