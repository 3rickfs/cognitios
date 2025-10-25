import os
from abc import ABC, abstractmethod

from ..comm.commops import COMMOps
from ..exe.exeops import EXEOps
from ..lrn.lrnops import LRNOps
from ..ltmem.ltmemops import LTMEMOps
from ..stmem.stmemops import STMEMOps
from ..vis.visops import VISOps


# Global variable
OPS = []

class attention_ops(ABC):
    """ Abstract class to run attention operations
    """

    @abstractmethod
    def run_operations(**kwargs):
        # Interface to child classes
        pass


class answer_question_op(attention_ops):
    """ Run operation 1 of the attention module
    """

    def run_operation(**kwargs):
        print("Answer question operation")

        qst = kwargs["question"]
        kwa = {
            "question": qst,
            "ops": ["answerquestion_op"]
        }
        res = COMMOps.run(**kwa)
        msg = res["answer"]
        kwargs["answer"] = msg

        return kwargs


class decorate_msg_op(attention_ops):
    """ Decorate message gotten from comm
    """

    def run_operation(**kwargs):
        print("Decorate answer")
        msg = kwargs["answer"]
        kwa = {
            "msg": msg,
            "ops": ["decorate_msg_op"]
        }
        res = VISOps.run(**kwa)
        kwargs['deco_ans'] = res['deco_ans']

        return kwargs


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
