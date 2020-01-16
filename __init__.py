'''
Nocnus is a Python wrapper for quickly implementing CRUD MongoDB operations.
Why the name Nocnus?
Ocnus is the name of the greek god of delays and frustrations and we
do not want any any of those in implementing basic CRUD MongoDB operations
thus the name. (No Ocnus => Nocnus)
'''

from .Nocnus import (
    list_dbs,
    insert,
    fetch,
    sort,
    delete,
    update,
    drop_collection
)