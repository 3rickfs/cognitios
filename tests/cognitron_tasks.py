import unittest
import time
import requests
import json


class ingest_model_tests(unittest.TestCase):

    def test_get_ai_model_info(unittest.TestCase):
        print("************** TEST ***************")
        print("**** get_ai_model_info *****")
        print("- get information about the model to be uploaded")
        print("")

        expected_result = {
            "ai_model_filename": "ai_model_test_1.pkl",
            "ai_model_name": "ai_model_test_1",
            "ai_model_version": "v1.0.1",
            "ai_model_description": "detects plant diseases",
            "ai_model_privacy": "private",
            "ai_model_creation_date": "",
        }


        headers = {'Content-type': 'application/json'}
        cognitron_url = "http://127.0.0.1:5000"
 
        try:
            ai_model_info = {
                "ai_model_info":{
                    "model_filename": "ai_model_test_1.pkl",
                    "model_name": "ai_model_test_1",
                    "model_version": "v1.0.1",
                    "model_description": "detects plant diseases",
                    "model_privacy": "private"
            }
            json_data = json.dumps(ai_model_info)
            cognitron_hw_url = cognitron_url + "/upload_ai_model"
            cognitron_response = request.post(f"{cognitron_url}",
                                              data=json_data, headers=headers)
            print(f"Upload ai model result: {cognitron_response}")

            ai_model_name = {
                "ai_model_name": "ai_model_test_1"
            }
            json_data = json.dumps(ai_model_info)
            cognitron_hw_url = cognitron_url + "/get_ai_model_info"
            cognitron_response = request.post(f"{cognitron_url}",
                                              data=json_data, headers=headers)

            print(f"Cognitron get ai model info: {cognitron_response}")
            cognitron_response = json.loads(result.text)['ai_model_info']

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


    def test_cognitron_hello_world(self):
        print("**** TEST ****")
        print("** cognitron hello world **")
        print("- get greetings on html format")

        expected_result = "<p>Hello World! I'm Cognitron: " + \
                          "a cognitive component manager</p>"

        headers = {'Content-type': 'application/json'}
        cognitron_url = "http://127.0.0.1:5000"
        cognitron_hw_url = cognitron_url + "/"

        try:
            result = requests.get(cognitron_hw_url)
            print(result.json())
            cognitron_response = json.loads(result.text)['answer']

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

