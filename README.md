# You Don't Know Dynamic Arrays

But after this, you will.

In this assignment, you will engage in a test-driven development process to implement a dynamic array that grows to acommodate as many elements as needed. It supports insertion into the middle of the array. It also keeps the elements packed toward the lowest index, which means that when an element in the middle is removed, everything that was to the right of that element should shift one index to the left.

Oh, and we'll practice linear and binary search too, with maybe some bonuses for maintaining a sorted list.

## Run the Test Suite

`python3 -m unittest test_dynamic_array`

Open both *test_dynamic_array.py* and *dynamic_array.py* in your editor of choice. Modify the implementation in *dynamic_array.py* to pass the first test. Once it passes, create a commit. Then, uncomment the next test, and re-run the test suite. Implement what's necessary to pass the test, and then repeat this process.

**But wait!**

Toward the middle of the test suite, you should be thinking about the algorithmic efficiency of each operation. What should be O(1)? What should be linear? In addition, try to implement your operations using recursion, whenever appropriate.

## Best Done in Pairs!

Get together with a colleague in front of just one machine, and take turns being the driver. Change drivers after each test is passed. Don't forget to commit after each test.

(c) 2019 Yong Joseph Bakos. All rights reserved.
