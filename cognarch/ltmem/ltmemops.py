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
        try:
            with sqlite3.connect("ai_model_db.db")
                print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

        except sqlite3.OperationalError as e:
            print("Failed to open database:", e)
            kwargs["result"] = "error"
            kwargs["error_msg"] = e


        return kwargs


class edit_ai_model_info_op(ltmemory_ops):
    """ Edit AI model info
    """

    def run_operation(**kwargs):
        print("Edit AI model information operation")

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
