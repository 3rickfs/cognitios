import os
import sqlite3
from abc import ABC, abstractmethod

# Global variable
OPS = []

class ltmemory_ops(ABC):
    """ Abstract class to run long-term operations
    """

    @abstractmethod
    def run_operations(**kwargs):
        # Interface to child classes
        pass


class create_ai_model_register_op(ltmemory_ops):
    """ Create AI model register in SQLITE database
    """

    def run_operation(**kwargs):
        print("Create AI model register operation")
        ai_model_info = kwargs["ai_model_info"]
        # ToDo: run a command to create the folder if that does not exist
        ai_model_folder_name = 'models'
        try:
            with sqlite3.connect(f"{ai_model_folder_name}/ai_model_db.db") as conn:
                print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
                cursor = conn.cursor()
                sql_statements = [ 
                    """CREATE TABLE IF NOT EXISTS ai_models (
                            id INTEGER PRIMARY KEY, 
                            model_name text NOT NULL, 
                            creation_date DATE NOT NULL, 
                            model_file_path text NULL,
                            end_date DATE
                       );"""
                ]
                # Execute sql query to create table
                for s in sql_statements:
                    cursor.execute(s)
                conn.commit()
        except sqlite3.OperationalError as e:
            print("Failed to open database:", e)

        return kwargs


class edit_ai_model_info_op(ltmemory_ops):
    """ Edit AI model info
    """

    def run_operation(**kwargs):
        print("Edit AI model information operation")
        #ToDo: update table searching per ai model name

        return kwargs


class get_ai_model_info_op(ltmemory_ops):
    """ Get AI model information
    """

    def run_operation(**kwargs):
        print("Get AI model information operation")

        return kwargs



class operation_1(ltmemory_ops):
    """ Run operation 1 of the long-term memory module
    """

    def run_operation(**kwargs):
        print("Running operation 1")

        return kwargs

class operation_session:
    @staticmethod
    def run_config():
        operation_dict = {}
        operations = ltmemory_ops.__subclasses__()
        for op in operations:
            op_name = op.__name__
            operation_dict[op_name] = op

        return operation_dict


class LTMEMOps:
    """ User-facing static class to run long-term memory operations
    """
    @staticmethod
    def run(**kwargs):
        if "OPS" not in locals():
            OPS = operation_session.run_config()
        for op in kwargs["ops"]:
            kwargs = OPS[op].run_operation(**kwargs)

        return kwargs
