# Sudoku Player

### Implemented Algorithms

* Naive Backtracking Algorithm
* Smart Backtracking Algorithm using Minimum Remaining Values(MRV)

### To run the program
There are no supporting modules that are to be installed for this program
```
python3 sudoku.py
```

The user will be asked if they want to make use of smart backtracking algorithm, if the input given is `y` then the Smart Backtracking with MRV will be used. For any input other than `y` Naive Backtracking algorithm will be used.

### Input

By default the input taken by the program will be `sudoku.txt` that is available in the repo. User can either rename their input file to `sudoku.txt` or edit the file to provide new inputs to the program.

#### Default input
```
0 0 3 0 2 0 6 0 0 
9 0 0 3 0 5 0 0 1 
0 0 1 8 0 6 4 0 0 
0 0 8 1 0 2 9 0 0 
7 0 0 0 0 0 0 0 8 
0 0 6 7 0 8 2 0 0 
0 0 2 6 0 9 5 0 0 
8 0 0 2 0 3 0 0 9 
0 0 5 0 1 0 3 0 0
```

#### Output by the program
```
Time taken for the solution -  0.019  seconds
Steps taken to arrive at the solution -  50
The solution is - 

4 8 3 9 2 1 6 5 7 
9 6 7 3 4 5 8 2 1 
2 5 1 8 7 6 4 9 3 
5 4 8 1 3 2 9 7 6 
7 2 9 5 6 4 1 3 8 
1 3 6 7 9 8 2 4 5 
3 7 2 6 8 9 5 1 4 
8 1 4 2 5 3 7 6 9 
6 9 5 4 1 7 3 8 2 
```