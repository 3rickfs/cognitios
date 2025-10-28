import os
from abc import ABC, abstractmethod

from cognarch.att.attops import ATTOps
from cognarch.comm.commops import COMMOps
from cognarch.exe.exeops import EXEOps
from cognarch.lrn.lrnops import LRNOps
from cognarch.ltmem.ltmemops import LTMEMOps
from cognarch.stmem.stmemops import STMEMOps
from cognarch.vis.visops import VISOps

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
        if req == "question":
            print("Who you are request")
            req = kwargs["request"]
            qst = kwargs["question"]
            kwa = {
                "question": qst,
                "ops": ["answer_question_op", "decorate_msg_op"]
            }
            res = ATTOps.run(**kwa)
            kwargs['answer'] = res['deco_ans']
        elif req == "upload_ai_model":
            print("Request: upload ai model")
            ai_model_info = kwargs["ai_model_info"]
            try:
                kwa = {
                    "ai_model_info": ai_model_info,
                    "ops": [
                        "create_ai_model_register_op",
                        "save_ai_model_info_op",
                        "save_ai_model_weights_op"
                    ]
                }
                res = ATTOps.run(**kwa)
                kwargs['upload_ai_model_result_msg'] = res['result_msg']
            except Exception as e:
                raise(f"Cognition was not able to upload ai model: {e})")
        elif req == "get_ai_model_info":
            print("Request: get ai model info")
            ai_model_name = kwargs["ai_model_info"]
            try:
                kwa = {
                    "ai_model_name": ai_model_name,
                    "ops": [
                        "get_ai_model_info_op"
                    ]
                }
                res = LTMEMOps.run(**kwa)
                kwargs['ai_model_info'] = res['ai_model_info']
            except Exception as e:
                raise(f"Cognition was not able to get ai model info: {e})")

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


class CognitronOps:
    """ User-facing static class to run cognitron operations
    """
    @staticmethod
    def run(**kwargs):
        if "OPS" not in locals():
            OPS = operation_session.run_config()
        for op in kwargs["ops"]:
            kwargs = OPS[op].run_operation(**kwargs)

        return kwargs
