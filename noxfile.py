"""Nox sessions."""
from pathlib import Path
import shutil

import nox
from nox.sessions import Session

owner, repository = "garethstockwell", "cookiecutter-hypermodern-python"
labels = "cookiecutter", "documentation"
bump_paths = "README.md"


@nox.session(name="prepare-release")
def prepare_release(session: Session) -> None:
    """Prepare a GitHub release."""
    args = [
        f"--owner={owner}",
        f"--repository={repository}",
        *[f"--bump={path}" for path in bump_paths],
        *[f"--label={label}" for label in labels],
        *session.posargs,
    ]
    session.install("click", "github3.py")
    session.run("python", "tools/prepare-github-release.py", *args, external=True)


@nox.session(name="publish-release")
def publish_release(session: Session) -> None:
    """Publish a GitHub release."""
    args = [f"--owner={owner}", f"--repository={repository}", *session.posargs]
    session.install("click", "github3.py")
    session.run("python", "tools/publish-github-release.py", *args, external=True)


@nox.session(name="dependencies-table")
def dependencies_table(session: Session) -> None:
    """Print the dependencies table."""
    session.install("tomli")
    session.run("python", "tools/dependencies-table.py", external=True)
