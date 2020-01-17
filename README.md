# Nocnus
Nocnus is a simple Python library built on top of Pymongo to ensemble the basic MongoDB CRUD operations into one class in order to simplify its usage and save some development time.

Why the name Nocnus?
Ocnus is the name of the greek god of delays and frustrations and we
do not want any any of those in implementing basic CRUD MongoDB operations
thus the name. (No Ocnus => Nocnus)

#### Instantiation
The Nocnus class is instantiated with a database name and connection link passed as string parameters to it. The default connection link is: 
> mongodb://localhost:27017/ 

#### Basic CRUD Methods
  - insert: This method is used to insert documents into a particular collection in the database.
    Parameters:
    * collection_name (string): The name of the collection to insert documents into.
    * documents (dictionary): The document to be inserted into the collection
    * multi: A boolean parameter to indicate whether the insertion being done contains multiple 
      documents or just a single document.

    Return:
    The insert method returns the inserted id(s) of the documents.

 - fetch: This method is used to fetch documents from a collection in the database.
    Parameters:
    *  collection_name (string): The name of the collection to insert documents into.
    *  allResults: A boolean parameter to specify whether to return all results that matches the query
       or only the first result that matches the query
    *  query (dictionary): A keyword-only argument that contains the query dictionary to search the
       collection with
    *  specific_field (dictionary): A keyword-only parameter that makes querying for only specific       fields of the documents in a collection possible.
    
    Return:
    The fetch method returns a dictionary containing lists as values for queries made

 - sort: This method returns sorted documents in a particular collection
    Parameters:
    *  collection_name (string): The name of the collection to insert documents into.
    *  sort_field_key (string): A parameter that contains the key of the field to sort the collection    with
    *  direction (int): This parameter indicates the direction of sorting (whether in a descending or    ascending order)
    
    Return:
    The sort method returns a list of the sorted collection

 - delete: This method deletes a document matching the given query data from the collection given.
    Parameters:
    *  collection_name (string): The name of the collection to insert documents into.
    *  query_data (dictionary): The query information to search for matching documents.
    *  multi (boolean): This parameter is used to specify whether to delete all matching documents or    just the first document to match the query data
    
    Return:
    This method returns nothing for single document deletions and deleted counts for multiple document deletions

 - update:
    Parameters:
    *  collection_name (string): The name of the collection to insert documents into.
    *  query_data (dictionary): The query information to search for matching documents.
    *  updated_data (dictionary): The updated dictionary data to replace the matched document with.
    *  multi (boolean): This parameter is used to specify whether to update all matching documents or    just the first document to match the query data
    
    Return:
    The method does not return any data

 - drop_collection: This method deletes a collection from the database
    Parameter:
    *  collection_name (string): The name of the collection to insert documents into.
    
    Return:
    This method does not return any data 
  
### Installation
```sh
$ pip3 install nocnus
```
### Dependency
Nocnus requires Pymongo to run (Of course!)

```sh
$ pip3 install Pymongo
```

### Usage Examples
```sh
from nocnus import Nocnus
# create a database named "sela"
db = Nocnus(db='sela')
# a dictionary containing information to save in the database collection "books"
single_book = {
    "name": "Mongo Mastery",
    "author": "Mike Ekim"
}

multi_book = [
    {
        "name": "Testing Python",
        "author": "Steven Time"
    },
    {
        "name": "Posting Python",
        "author": "Paul Timothy"
    }
]
doc_id = db.insert(collection_name='books', documents=single_book)
# insert multiple documents into collection books
doc_ids = db.insert(collection_name="books", documents=multi_book, multi=True)
# update the name field of the document with author name Steven Time to Testing Python 2nd Edition
query = {"author": "Steven Time"}
updated_data={"name": "Testing Python 2nd Edition"}
db.update(collection_name="books", query=query, updated_data=updated_data)
# print the ids of the inserted documents
print(doc_id, doc_ids)
# search for documents with publish_year greater than 2011
print(db.fetch(collection_name="books", query={"publish_year":{"$gt": 2011}}))
# # delete a document with author Paul Timothy from the collection
db.delete(collection_name="books", query_data={"author": "Paul Timothy"})
# # print all documents in the collection books
print(db.fetch(collection_name="books", allResults=True))
# drop the collection
db.drop_collection(collection_name="books")
```

### Development

All contributions are welcome.
