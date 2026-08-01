from pathlib import Path

def explore_repo(repo_path):
    repo = Path(repo_path)

    relevant = []

    for file in repo.rglob("*.js"):
        if "node_modules" in str(file):
            continue
        relevant.append(str(file))

    return {
        "repo": str(repo),
        "files": relevant
    }