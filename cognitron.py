import yaml
from flask import Flask, request

app = Flask(__name__)
app.config['FILE_PATH'] = "/path/to/somewhere"


@app.route('/', method=['POST'])
def about():
    msg = """<p> Cognitron: Human-knowledge-centered manager machine </p>"""

    return msg


@app.route('/ingest_csv_data', method=['POST'])
def ingest_csv_data():
    """ Use a cognitive architecture to process data,
    predict, execute, visualize, among other tasks.
    """

    print("Running cognitron")
    if request.method == 'POST':
        yf = request.files['yaml_file_name']
        yaml_fn = yf.filename
        yaml_file_path = os.path.join(app.config['FILES_PATH'], yaml_fn)
        #yf.save(yaml_file_path)
        #kwargs = get_kwargs(yaml_file_path)
        kwargs = yaml.load(yaml_file_path, Loader=yaml.FullLoader)
        csvf = request.files['csv_file_name']
        csv_file_path = os.path.join(app.config['FILES_PATH'], csvf.filename)
        kwargs['csv_file_path'] = csv_file_path

        # Send kwargs to the cognition

        # TODO: looks like Cognitron and cognition should be different modules
        # cognitron is the REST API service, while cognition is the architecture
        # itself that gather all the components: attention, lerarning, etc.
        # 
        # Possible first test:
        # (1) Using Postman, send the files, might be a csv dataset, among other params
        # (2) Get the csv file and run a AutoML framework (maybe Autogluon) to get the model 
        # that fits the best the underlying data. It might also get a model to be fine-tuned. 
        # (3) deploy the model and get it available on an API service. Maybe use same cognitron
        # service, just adding an endpoint might be enough. However, this means that the endpoint
        # should be added in execution time. That makes it harder. 
        # Optional forms of deploying:
        #  - API service: write a template-based Flask app and then run it, save the process ID and kill it when required.
        #  - CHOSEN ONE #Container based#: similar than the above one but may require more memory as more layers are needed.
        #     * This looks more stable and independent, although mem consumption is high
        #     * It anyway uses an API container on an specific venv
        #     * Containers might be deployed on local machine using specific cores and memory or on the cloud.
        #  - RAM, contained in a class: when may require IDs for new models so we can retrieve them. Monolitic.
        # (4) CRUD over the deployed model-containers
        # (5) Some proto-visualization of predictions
        # REMEMBER: we're leading with human knowledge centred approach.





        res = 


    return "lala"

if __name__ == '__main__':
    app.run()
