# [START gae_python38_app]
# [START gae_python3_app]
import googleapiclient.discovery
from flask import Flask, render_template

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/getstatus')
def get_server_status():
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().get(project='mud-host', zone='us-central1-a', instance='game-server-linux').execute()
    return result['status']


@app.route('/startserver')
def start_server():
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().start(project='mud-host', zone='us-central1-a', instance='game-server-linux').execute()
    return get_server_status()


@app.route('/stopserver')
def stop_server():
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().stop(project='mud-host', zone='us-central1-a', instance='game-server-linux').execute()
    return get_server_status()


@app.route('/')
def start():
    """Return a friendly HTTP greeting."""
    compute = googleapiclient.discovery.build('compute', 'v1')
    status = get_server_status()
    print(f'Status is {status}')
    return render_template('index.html', title='Home', status=status)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]