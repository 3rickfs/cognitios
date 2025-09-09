import os
from abc import ABC, abstractmethod

# Global variable
OPS = []

class execution_ops(ABC):
    """ Abstract class to run execution operations
    """

    @abstractmethod
    def run_operations(**kwargs):
        # Interface to child classes
        pass


class operation_1(execution_ops):
    """ Run operation 1 of the execution module
    """

    def run_operation(**kwargs):
        print("Running operation 1")

        return kwargs

class operation_session:
    @staticmethod
    def run_config():
        operation_dict = {}
        operations = execution_ops.__subclasses__()
        for op in operations:
            op_name = op.__name__
            operation_dict[op_name] = op

        return operation_dict


class COMMOps:
    """ User-facing static class to run execution operations
    """
    @staticmethod
    def run(**kwargs):
        if "OPS" not in locals():
            OPS = operation_session.run_config()
        for op in kwargs["ops"]:
            kwargs = OPS[op].run_operation(**kwargs)

        return kwargs
