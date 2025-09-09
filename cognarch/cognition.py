import os
from abc import ABC, abstractmethod

from att.attops import ATTOps
from comm.commops import COMMOps
from exe.exeops import EXEOps
from lrn.lrnops import LRNOps
from ltmem.ltmemops import LTMEMOps
from stmem.stmemops import STMEMOps
from vis.visops import VISOps

# Global variable
OPS = []

class cognitron_ops(ABC):
    """ Abstract class to run cognitron operations
    """

    @abstractmethod
    def run_operation(**kwargs):
        # Interface to child classes
        pass


class att_op(cognitron_ops):
    """ Call attention module to perfom attention operations
    """

    def run_operation(**kwargs):
        print("Calling attention operations")

        return kwargs


class comm_op(cognitron_ops):
    """ Call Communication module to perfom communication operations
    """

    def run_operation(**kwargs):
        print("Calling communication operations")

        return kwargs


class exe_op(cognitron_ops):
    """ Call Execution module to perfom execution operations
    """

    def run_operation(**kwargs):
        print("Calling execution operations")

        return kwargs


class lrn_op(cognitron_ops):
    """ Call Learning module to perfom learning operations
    """

    def run_operation(**kwargs):
        print("Calling learning operations")

        return kwargs


class ltmem_op(cognitron_ops):
    """ Call long-term memory module to perfom long shot memory operations
    """

    def run_operation(**kwargs):
        print("Calling long-term memory operations")

        return kwargs


class stmem_op(cognitron_ops):
    """ Call short-term memory module to perfom short shot memory operations
    """

    def run_operation(**kwargs):
        print("Calling short-term memory operations")

        return kwargs


class stmem_op(cognitron_ops):
    """ Call short-term memory module to perfom short shot memory operations
    """

    def run_operation(**kwargs):
        print("Calling short-term memory operations")

        return kwargs


class operation_session:
    @staticmethod
    def run_config():
        operation_dict = {}
        operations = cognitron_ops.__subclasses__()
        for op in operations:
            op_name = op.__name__
            operation_dict[op_name] = op

        return operation_dict


class COGNITRONOps:
    """ User-facing static class to run cognitron operations
    """
    @staticmethod
    def run(**kwargs):
        if "OPS" not in locals():
            OPS = operation_session.run_config()
        for op in kwargs["ops"]:
            kwargs = OPS[op].run_operation(**kwargs)

        return kwargs
