tabularize.py
=============

This module helps you to read tabular data from string or file like objects.

Usage
-----

You can parse a string with `loads` method.

    import tabularize

    print tabularize.loads("""
    ------------------
    | name | surname |
    ------------------
    | edi  | budu    |
    | budu | edu     |
    ------------------
    """)

    # prints [{ "name": "edi", "surname": "budu"},
              { "name": "budu", "surname": "edi"}]


Also you can specify the return type of result.


    print tabularize.loads("""
    ------------------
    | name | surname |
    ------------------
    | edi  | budu    |
    | budu | edu     |
    ------------------
    """, return_type=list)

    # prints [["edi", "budu"], ["budu", "edi"]]

So that might be funny too

    tabular = tabularize.loads("""
    ------------------
    | name | surname |
    ------------------
    | edi  | budu    |
    | budu | edu     |
    ------------------
    """, return_type=tuple)

    for name, surname in tabular:
        print name, surname # disco

And also you can parse the doctstring of object with `from_docstring`

    class MyClass(object):
        """
        This is a docstring

        Here is my test case:

            _____________________________
            | name | surname | full_name |
            | edi  | budu    | edi budu  |
            | budu | edi     | budu edi  |
            ______________________________

        """

    tabular = tabularize.from_docstring(MyClass, return_type=tuple)

    for name, surname, full_name in tabular:
        assert "%s %s" % (name, surname) == full_name

