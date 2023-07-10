import threading
import subprocess


def update_from_github(repo_url="https://github.com/fazalfzl/choice.git"):
    # Clone the repository in a temporary directory
    temp_dir = "temp_clone"
    subprocess.run(["git", "clone", repo_url, temp_dir], shell=True)

    # Copy the contents of the cloned repository to the current working directory, overwriting existing files
    subprocess.run(["xcopy", temp_dir, ".", "/E", "/H", "/C", "/I", "/Y"])

    # Remove the temporary directory
    subprocess.run(["rd", "/S", "/Q", temp_dir], shell=True)


def check_for_updates_clicked():
    down = threading.Thread(name='scanning', target=lambda: update_from_github())
    down.start()
