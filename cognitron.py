import yaml
from flask import Flask, request, json, jsonify

from cognarch.cognition import CognitronOps

app = Flask(__name__)
app.config['FILE_PATH'] = "/path/to/somewhere"


@app.route('/')
def about():
    msg = ""
    kwargs = {
        "request": "question",
        "question": "who you are",
        "ops": ["att_op"]
    }
    res = CognitronOps.run(**kwargs)
    msg = jsonify(res)
    msg.status_code = 200

    print(f"msg: {msg}")

    return msg


@app.route('/get_ai_model_info')
def get_ai_model_info():
    msg = ""
    ai_model_name = request.get_json()["ai_model_name"]
    kwargs = {
        "request": "get_ai_model_info",
        "ai_model_name": ai_model_name,
        "ops": ["att_op"]
    }
    res = CognitronOps.run(**kwargs)
    msg = jsonify(res)
    msg.status_code = 200
    print(f"msg: {msg}")

    return msg


@app.route('/upload_ai_model', methods=['POST'])
def ingest_csv_data():
    """ Use a cognitive architecture to process data,
    predict, execute, visualize, among other tasks.
    """

    print("Running cognitron")
    if request.method == 'POST':
        input_data = request.get_json()
        msg = ""
        kwargs = {
            "request": "upload_ai_model",
            "ai_model_info": input_data["ai_model_info"],
            "ops": ["att_op"]
        }
        res = CognitronOps.run(**kwargs)
        msg = jsonify(res)
        msg.status_code = 200


        """
        yf = request.files['yaml_file_name']
        yaml_fn = yf.filename
        yaml_file_path = os.path.join(app.config['FILES_PATH'], yaml_fn)
        #yf.save(yaml_file_path)
        #kwargs = get_kwargs(yaml_file_path)
        kwargs = yaml.load(yaml_file_path, Loader=yaml.FullLoader)
        csvf = request.files['csv_file_name']
        csv_file_path = os.path.join(app.config['FILES_PATH'], csvf.filename)
        kwargs['csv_file_path'] = csv_file_path
        """

        # Send kwargs to the cognition

        print(f"msg: {msg}")

    else:
        error_msg = "No ther method than POST is supported by this endoint"
        msg = {"error_msg": error_msg}
        msg = jsonify(msg)
        msg.status_code = 200

    return msg


if __name__ == '__main__':
    app.run()
