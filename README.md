# python_unit_testing
a class about unit testing in python

1) why is unit testing? 
2) methods of doing it in python with examples

## 1) why is unit testing? 

**many reasons...**

- a more structured way of thinking... in a function where you need to do several actions, you can create little functions for each of the actions and test them as you go individually, so that you will be aware of bugs faster... OR, create first the tests and then the little functions (TDD - test driven development), which usually makes you code more rapidly.

- when working on new features to implement on an existing codebase, we want to make sure that after our change/refactoring, everything still works.

- the new code will only be in production for users, if the tests pass! so it makes it easier for you and your team to be sure of their changes... it limits anxiety when going to bed at night.

- it's not just for fun, it's crucial sometimes, for example a bank, a hospital, military, ...

**however...**

- because we are only testing things individually, we don't know if they work as supposed to all together... that is where integration and e2e tests come in! (https://i.imgur.com/w1uYhFA.png)

- it's horribly boring to do in my opinion, it takes a lot of time and effort.

- also doesn't cover performance or scalibility.

### references
https://www.geeksforgeeks.org/unit-testing-software-testing/
(also explains differences between the different types of testing)


## 2) methods of doing it in python with examples

the `assert` statement is the basis of testing; it throws an exception when it's false:

 `assert <condition being tested>, <error message to be displayed>` 

 `assert 1 > 0, 'The Condition is True'`

 `assert 1 < 0, 'The Condition is False'`


on top of it there are many frameworks that make our lives easier...

- pytest
- unittest (built-in in python)
- doctest
- nose2
... 

example with **pytest** and **unittest**: https://github.com/Mrrvm/python_unit_testing

### pytest
install pytest:  `pip install pytest`

run all tests:  `python -m pytest tests/test_fruit_pytest.py`

run test_request inside logic class:  `python -m pytest fruit.py`

- can be next to the logic, which might be more or less organised
- only uses assert

### unittest(built-in in python)
run all tests verbosely:  `python -m unittest -v`

- must be in separate file, in a folder called tests, have an init file and call unittest.main()
- has many assert methods: assertEqual, asserNotEqual, assertIn, assertInstance, assertIs, ...

### references
about the different frameworks
https://www.aviator.co/blog/complete-guide-to-python-testing-frameworks/

unittest
https://www.dataquest.io/blog/unit-tests-python/https://docs.python.org/3/library/unittest.html (official docs)

pytest vs unittest
https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/




























































































































































