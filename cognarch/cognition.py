from flask import Flask, request

app = Flask(__name__)
app.config['FILE_PATH'] = "/path/to/somewhere"

@app.route('/', method=['POST'])
def cognitron():
    """ Use a cognitive architecture to process data,
    predict, execute, visualize, among other tasks.
    """

    print("Running cognitron")
    if request.method == 'POST':
        yf = request.files['sth_here']
        yaml_fn = yf.filename
        yaml_file_path = os.path.join(app.config['FILES_PATH'], yaml_fn)
        yf.save(yaml_file_path)
        kwargs = get_kwargs(yaml_file_path)

        # Send kwargs to the cognition
        # TODO: looks like Cognitron and cognition should be different modules
        # cognition is the REST API service, while cognition is the architecture
        # itself that gather all the components: attention, lerarning, etc.
        res = 


    return "lala"

if __name__ == '__main__':
    app.run()
