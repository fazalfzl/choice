import threading
import subprocess


def update_from_github(repo_url="https://github.com/fazalfzl/choice.git"):
    subprocess.call("update.bat", shell=True)
    print("updated")
def check_for_updates_clicked():
    down = threading.Thread(name='scanning', target=lambda: update_from_github())
    down.start()
