import unittest
import time
import requests
import json


class ingest_model_tests():
    """
    def test_get_ai_model_info(unittest.TestCase):
        print("************** TEST ***************")
        print("**** get_ai_model_info *****")
        print("- get information about the model to be uploaded")
        print("")

        ai_model_info = {
            "ai_model_filename": "ai_model_test_1.pkl",
            "ai_model_version": "v1.0.1",
            "ai_model_description": "detects plant diseases",
            "ai_model_privacy": "private"
        }

        #push_ai_model_info 
        headers = {'Content-type': 'application/json'}
        json_data = json.dumps(ai_model_info)
        result = request.post(f"{cognitron_url}",
                              data=json_data, headers=headers)
 
        cognitron_response = json.loads(result.text)["cognitron_response"]
        print(f"Cognitron reply: {cognitron_response}")

    """
    def test_cognitron_hello_world(unittest.TestCase):
        print("**** TEST ****")
        print("** cognitron hello world **")
        print("- get greetings on html format")

        expected_result = "<p> Hello World! I'm Cognitron: " + \
                          "a cognitive component manager </p>"

        headers = {'Content-type': 'application/json'}
        json_data = json.dumps(ai_model_info)
        cognitron_url = "http://127.0.0.1:5000"
        cognitron_hw_url = cognitron_url + "/"
 
        try:
            result = request.get(f"{cognitron_hw_url}", headers=headers)
            cognitron_response = json.loads(result.text)

            print("__________________________________")
            print(f"Cognitron reply: {cognitron_response}")
            print("__________________________________")
            print(f"expected_result: {expected_result}")
            self.assertEqual(expected_result, cognitron_response)
        except Exception as e:
            print("%"*100)
            print(f"error: {e}")
            print("%"*100)

        print("*"*100)

if __name__ == '__main__':
    unittest.main()

