"""Release GitHub."""
import pathlib
import re
import sys
import webbrowser
from urllib.parse import urlencode

import tomli
from result import Err, Ok, Result
from typing_extensions import assert_never


def read_pyproject_toml(
    pyproject_path: pathlib.Path,
) -> Result[str, FileNotFoundError]:
    """Read `pyproject.toml`."""
    try:
        configuration = pyproject_path.read_text(
            encoding="utf-8",
        )
    except FileNotFoundError as e:
        return Err(e)
    return Ok(configuration)


def read_about_script(about_path: pathlib.Path) -> Result[str, FileNotFoundError]:
    """Read the `__about__.py` script."""
    try:
        about_data = about_path.read_text(
            encoding="utf-8",
        )
    except FileNotFoundError as e:
        return Err(e)
    return Ok(about_data)


def main() -> None:
    """
    Open a tab ready to review and approve for new release.

    Based on https://github.com/pypa/hatch/blob/master/scripts/release_github.py
    """
    path_to_pyproject = pathlib.Path("pyproject.toml")
    about_script = (
        pathlib.Path("{{cookiecutter.project_name.lower().replace('-', '_')}}")
        / "__about__.py"
    )

    pyproject_toml = read_pyproject_toml(
        pyproject_path=path_to_pyproject,
    )

    if not isinstance(pyproject_toml, Ok):
        err = pyproject_toml.err()

        if isinstance(err, FileNotFoundError):
            sys.stdout.write(f"{path_to_pyproject} not found.\n")
            sys.exit(1)
        else:
            assert_never(err)

    pkg_data = tomli.loads(pyproject_toml.unwrap())

    about_data = read_about_script(
        about_path=about_script,
    )
    if not isinstance(about_data, Ok):
        err = about_data.err()
        if isinstance(err, FileNotFoundError):
            sys.stdout.write(f"{about_script} not found.\n")
            sys.exit(1)
        else:
            assert_never(err)

    search_result = re.search(
        r"__version__ = \"(.*?)\"",
        about_data.unwrap(),
    )

    if search_result is None:
        sys.stdout.write(f"No `__version__` variable found in the {about_script}.\n")
        sys.exit(1)

    version = search_result.group(1)
    params = urlencode(
        query={
            "title": f"v{version}",
            "tag": f"v{version}",
        }
    )

    webbrowser.open_new_tab(
        url="{source}/releases/new?{params}".format(
            source=pkg_data["project"]["urls"]["Source"], params=params
        )
    )


if __name__ == "__main__":
    main()
