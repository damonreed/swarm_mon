import functions_framework
import subprocess
import re

@functions_framework.http
def test(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'host' in request_json:
        host = request_json['host']
    elif request_args and 'host' in request_args:
        host = request_args['host']
    else:
        host = request.remote_addr

    return f'Hello {host}!'
