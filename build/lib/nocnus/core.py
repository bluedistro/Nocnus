from __future__ import print_function
from pymongo import MongoClient
import sys


def error_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Nocnus:
    def __init__(self, db=None, connection_host="mongodb://localhost:27017/"):
        self.__client = MongoClient(connection_host)
        self.__database = self.__client[db]

    def list_dbs(self):
        return self.__client.list_database_names()

    def insert(self, collection_name: str, documents: dict, multi: bool = False):
        """
        This method is used to insert documents into a particular collection in the database
        """
        self.__collection = self.__database[collection_name]
        if not multi:
            inserted = self.__collection.insert_one(documents)
            return inserted.inserted_id
        else:
            inserted = self.__collection.insert_many(documents)
            return inserted.inserted_ids

    def fetch(
        self,
        collection_name: str,
        allResults: bool = False,
        *,
        query: (dict, None) = None,
        specific_field: (dict, None) = None
    ):
        """
            This function generically fetches info from any collection name specified
            allResults:
                *False => returns the first document of the collection
                *True => returns all the docs in the collection
            query:
                Keyword only argument containing dictionary value of specific docs to search
            specific_field
                Keyword only argument containing dictionary value of specific field to search in
                all documents in a collection            
        """
        self.__collection = self.__database[collection_name]
        kwarg_return = {}
        if query or specific_field is not None:
            if query is not None:
                query_results = [q_search for q_search in self.__collection.find(query)]
                kwarg_return["query_results":query_results]
            if specific_field is not None:
                specific_field_results = [
                    sf_search for sf_search in self.__collection.find(specific_field)
                ]
                kwarg_return["specific_field_results":specific_field_results]
            return kwarg_return
        else:
            if not allResults:
                return self.__collection.find_one()
            else:
                return [all_docs for all_docs in self.__collection.find()]

    def sort(self, collection_name: str, sort_field_key: str, direction: int = 1):
        """
        This function returns sorted documents in a particular collection
        """
        self.__collection = self.__database[collection_name]
        docs = self.__collection.find().sort(sort_field_key, direction)
        return [doc for doc in docs]

    def delete(self, collection_name: str, query_data: dict, multi: bool = False):
        """
        This function deletes a document matching the given query data from the collection given
        """
        self.__collection = self.__database[collection_name]
        if not multi:
            self.__collection.delete_one(query_data)
        else:
            delete_track = self.__collection.delete_many(query_data)
            return delete_track.deleted_count

    def update(
        self, collection_name: str, query: dict, updated_data: dict, multi: bool = False
    ):
        self.__collection = self.__database[collection_name]
        new_data = {"$set": updated_data}
        if not multi:
            self.__collection.update_one(query, new_data)
        else:
            self.__collection.update_many(query, new_data)

    def drop_collection(self, collection_name: str):
        self.__collection = self.__database[collection_name]
        self.__collection.drop()
