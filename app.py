import flask

app = flask.Flask(__name__)


@app.route('/hello-world', methods=['GET'])
def hello_world():
    data = {"success": False}
    # get the request parameters
    params = flask.request.json
    if not params:
        params = flask.request.args
        # if parameters are found, echo the msg parameter
        if params:
            data["response"] = params.get("msg")
            data["success"] = True
    # return a response in json format
    return flask.jsonify(data)


app.run(host='0.0.0.0')

