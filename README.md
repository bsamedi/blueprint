# blueprint
Re-use arguments repeatedly passed to a python callable object

If you need to invoke the same function/method several times with somewhat siimlar set of arguments `blueprint` function may help keeping your code cleaner

## Usage
```
bp = blueprint(callable [,reuseable_positional_arguments] [,default_dict_arguments])
bp([more_positional_arguments,] [more_named_arguments])
```
Function `f` receives both positional and named arguments.<br>
Instead of each time providing full set of arguments:
```
f(1, 1, x=1, y=2)
f(1, 2, x=1, y=3)
f(1, 3, x=2, y=4)
f(1, 4, x=1, y=6)
```
You can write:
```
b = blueprint(f, 1, x=1)
b(1, y=2)
b(2, y=3)
b(3, x=2, y=4)
b(4, y=5)
```
Which better highlights difference in arguments by hiding repetitive values
