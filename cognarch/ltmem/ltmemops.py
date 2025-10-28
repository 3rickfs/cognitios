import os
import sqlite3
import datetime
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
        ai_model_name = ai_model_info["model_name"]
        # ToDo: run a command to create the folder if that does not exist
        ai_model_folder_name = 'models'
        # Getting current datetime
        tz = datetime.timezone.utc
        ft = "%Y-%m-%dT%H:%M:%S%z"
        cdt = datetime.datetime.now(tz=tz).strftime(ft)
        ai_model_creation_date = cdt
        try:
            with sqlite3.connect(f"{ai_model_folder_name}/ai_model_db.db") as conn:
                print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
                cursor = conn.cursor()
                sql_statements = [ 
                    """CREATE TABLE IF NOT EXISTS ai_models (
                            id INTEGER PRIMARY KEY, 
                            model_name text NOT NULL, 
                            model_file_path text NULL,
                            model_version text NULL,
                            model_description text NULL,
                            model_privacy text NULL,
                            creation_date DATE NOT NULL
                       );""",
                    """INSERT INTO ai_models(model_name, creation_data)
                       VALUES(?,?)
                    """
                ]
                # Execute sql query to create table
                cursor.execute(sql_statements[0])
                conn.commit()
                # Execute sql query to insert data
                minfo = (ai_model_name, ai_model_creation_date)
                cursor.execute(sql_statements[1], minfo)
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
        ai_model_id = kwargs["aimr_id"]
        ai_model_fp = kwargs["ai_model_info"]["model_filename"]
        ai_model_version = kwargs["ai_model_info"]["model_version"]
        ai_model_description = kwargs["ai_model_info"]["model_description"]
        ai_model_privacy = kwargs["ai_model_info"]["model_privacy"]
        sql_statement = """
            UPDATE ai_models SET model_file_path=?,
                                 model_version=?,
                                 model_description=?,
                                 model_privacy=?
            WHERE id = ?
        """
        try:
            with sqlite3.connect("ai_model_db") as conn:
                cursor = conn.cursor()
                cursor.execute(sql_statement, (ai_model_fp,
                                               ai_model_version,
                                               ai_model_description,
                                               ai_model_privacy,
                                               ai_model_id,
                                              ))
                conn.commit()
            kwargs["edit_result_msg"] = "AI Model register updated"

        except Exception as e:
            raise(f"Error updating the ai_model: {e}")

        return kwargs


class get_ai_model_info_op(ltmemory_ops):
    """ Get AI model information
    """

    def run_operation(**kwargs):
        print("Get AI model information operation")
        ai_model_name = kwargs["model_name"]
        try:
            sql_statement = """
                SELECT * FROM ai_model WHERE model_name = ?
            """
            with sqlite3.connect("ai_model_db") as conn:
                cursor = conn.cursor()
                cursor.execute(sql_statement, (ai_model_name,))
                ai_model_info = conn.fetchall()
            kwargs["ai_model_info"] = ai_model_info

        except Exception as e:
            raise("Error getting ai model info: {e}")

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
