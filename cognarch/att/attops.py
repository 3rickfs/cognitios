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


class create_ai_model_register_op(attention_ops):
    """ Create an AI model register
    """

    def run_operation(**kwargs):
        print("Create ai model register operation")
        print(f"KWARGS: {kwargs}")
        kwa = {
            "ops": ["create_ai_model_register_op"],
            "ai_model_name": kwargs['ai_model_info']['model_name']
        }
        try:
            res = LTMEMOps.run(**kwa)
            kwargs['aimr_id'] = res['new_ai_model_register_id']
        except Exception as e:
            raise(f"Error creating AI model register: {e}")

        return kwargs


class save_ai_model_info_op(attention_ops):
    """ Save AI model information
    """

    def run_operation(**kwargs):
        print("Save AI model information operation")
        aimr_id = kwargs["aimr_id"]
        ai_model_info = kwargs["ai_model_info"]
        kwa = {
            "aimr_id": aimr_id,
            "ai_model_info": ai_model_info,
            "ops": ["edit_ai_model_info_op"]
        }
        try:
            res = LTMEMOps.run(**kwa)
            kwargs['result_msg'] = res['edit_result_msg']
        except Exception as e:
            raise(f"Error to update ai model info: {e}")

        return kwargs


class save_ai_model_weights_op(attention_ops):
    """ Save AI model weights
    """

    def run_operation(**kwargs):
        print("Save AI model weights operation")

        return kwargs


class get_ai_model_info_op(attention_ops):
    """ Get AI model information
    """

    def run_operation(**kwargs):
        print("Get AI model information operation")
        ai_model_name = kwargs["ai_model_name"]
        kwa = {
            "ai_model_name": ai_model_name,
            "ops": ["get_ai_model_info_op"]
        }
        res = LTMEMOps.run(**kwa)
        kwargs['ai_model_info'] = res['ai_model_info']

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
