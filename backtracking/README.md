# Exhaustive recursion and backtracking

References:
```
https://web.archive.org/web/20181211024251/https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf
```

## Classic exhaustive permutation pattern
The above pattern finds all the possible re-arrangement of the letter in a string. 
There can be possible n! combinations for a given string using this method.

* Pseudocode
```
    if you have no more characters left to rearrange, print the current permutation
    for (every possible choice among the characters left to rearrange) {
        Make a choice and add that character to the permutation so far
        Use recursion to rearrange the remaining letters
    }
```

Please refer to c++ or Python codes in under rec_permute folder
```
cd backtracking
```
1. For compling c++
```
/usr/bin/clang++ -std=c++17 -stdlib=libc++ -g rec_permute/rec_permute.cpp -o rec_permute/rec_permute
```
2. For python using python3
```
python3 rec_permute/rec_permute.py
```

## Classic exhaustive subset pattern
Another example of the exhaustive recurison is listing all the subsets of given set. This algorithm makes two additional recursive calls and continues to depth of n, making it 2^n.

* Pseudocode
```
if there are no more elements remaining,
    print current subsets
else {
    consider the next element of those remaining
    try adding it to the current subset, and use recurison to build subsets from here
    try not adding it to current subset, and use recursion to build subsets from here
}
```
Please refer to c++ or Python codes in under rec_subsets folder
```
cd backtracking
```
1. For compling c++
```
/usr/bin/clang++ -std=c++17 -stdlib=libc++ -g rec_subsets/rec_subsets.cpp -o rec_subsets/rec_subsets
```
2. For python using python3
```
python3 rec_subsets/rec_subsets.py
```