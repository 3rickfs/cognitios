import os
from abc import ABC, abstractmethod

# Global variable
OPS = []

class attention_ops(ABC):
    """ Abstract class to run attention operations
    """

    @abstractmethod
    def run_operations(**kwargs):
        # Interface to child classes
        pass


class operation_1(attention_ops):
    """ Run operation 1 of the attention module
    """

    def run_operation(**kwargs):
        print("Running operation 1")

        return kwargs

class operation_session:
    @staticmethod
    def run_config():
        operation_dict = {}
        operations = attention_ops.__subclasses__()
        for op in operations:
            op_name = op.__name__
            operation_dict[op_name] = op

        return operation_dict


class ATTOps:
    """ User-facing static class to run attention operations
    """
    @staticmethod
    def run(**kwargs):
        if "OPS" not in locals():
            OPS = operation_session.run_config()
        for op in kwargs["ops"]:
            kwargs = OPS[op].run_operation(**kwargs)

        return kwargs
