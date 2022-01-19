import os

# os.environ["GIT_PYTHON_REFRESH"] = "quiet"
# import git
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # repo = git.Repo("./")
    return 'My last commit: ' # + str(repo.head.commit)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
