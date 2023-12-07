#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def srch_repl(value):
        return (value if value != search else replace)
    return list(map(srch_repl, my_list))
