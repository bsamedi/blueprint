#!/usr/bin/env python
from itertools import chain

def blueprint(callable, *prepend_list, **defaults_dict):
    def fn(*arg_list, **arg_dict):
        all_arg_list = chain(prepend_list, arg_list)
        all_arg_dict = defaults_dict.copy()
        all_arg_dict.update(arg_dict)
        return callable( *all_arg_list, **all_arg_dict)
    return fn
