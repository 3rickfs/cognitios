import os
from abc import ABC, abstractmethod

# Global variable
OPS = []

class visualization_ops(ABC):
    """ Abstract class to run visualization operations
    """

    @abstractmethod
    def run_operations(**kwargs):
        # Interface to child classes
        pass


class decorate_msg_op(visualization_ops):
    """ Run operation 1 of the visualization module
    """

    def run_operation(**kwargs):
        print("Decorate msg operation")

        msg = kwargs["msg"]
        msg = "<p>"+ msg + "</p>"
        kwargs["deco_ans"] = msg

        return kwargs


class generate_user_interface(visualization_ops):
    """ Generate files to be used for web-based user interface
    """

    def run_operation(**kwargs):
        print("Generate user interface")


        return kwargs

class operation_session:
    @staticmethod
    def run_config():
        operation_dict = {}
        operations = visualization_ops.__subclasses__()
        for op in operations:
            op_name = op.__name__
            operation_dict[op_name] = op

        return operation_dict


class VISOps:
    """ User-facing static class to run visualization operations
    """
    @staticmethod
    def run(**kwargs):
        if "OPS" not in locals():
            OPS = operation_session.run_config()
        for op in kwargs["ops"]:
            kwargs = OPS[op].run_operation(**kwargs)

        return kwargs
