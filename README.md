# blueprint
Re-use arguments repeatedly passed to a python callable object

If you need to invoke the same function/method several times with somewhat siimlar set of arguments `blueprint` function may help keeping your code cleaner

## Usage
```
bp = blueprint(callable [,reuseable_positional_arguments] [,default_dict_arguments])
bp([more_positional_arguments,] [more_named_arguments])
```
Say some function `fn` receives both positional and named arguments.<br>
Instead of repeating the same argument values:
```
fn(1, 1, a=1, b=2)
fn(1, 2, a=1, b=3)
fn(1, 3, a=2, b=4)
fn(1, 4, a=1, b=6)
```
You can write:
```
bp = blueprint(fn, 1, a=1)
bp(1, b=2)
bp(2, b=3)
bp(3, a=2, b=4)
bp(4, b=5)
```
Which better highlights difference in arguments used by hiding repetitive values
