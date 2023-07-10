import threading
import subprocess

def update_from_github(repo_url= "https://github.com/fazalfzl/choice.git" ):
    # Clone the repository in a temporary directory
    temp_dir = "temp_clone"
    subprocess.run(["git", "clone", repo_url, temp_dir])

    # Copy the contents of the cloned repository to the current working directory
    subprocess.run(["cp", "-r", temp_dir + "/*", "."])

    # Remove the temporary directory
    subprocess.run(["rm", "-rf", temp_dir])





def check_for_updates_clicked():
    down = threading.Thread(name='scanning', target=lambda: update_from_github())
    down.start()
