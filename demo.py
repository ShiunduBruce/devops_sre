import subprocess

def get_git_revisions_hash():
    hashes = []
    hashes.append(subprocess.check_output(['git', 'rev-parse', 'HEAD']))
    hashes.append(subprocess.check_output(['git', 'rev-parse', 'HEAD^']))
    return hashes


print(get_git_revisions_hash())