# Releasing RTAMT

## One-time publisher setup

Create the `pypi` and `testpypi` GitHub deployment environments in
Settings > Environments. Configure a required reviewer for `pypi` if you
want to inspect the TestPyPI release before production publication.

On **each** package index, configure a trusted publisher for RTAMT:

| Field | PyPI | TestPyPI |
| --- | --- | --- |
| Owner | `nickovic` | `nickovic` |
| Repository | `rtamt` | `rtamt` |
| Workflow filename | `ci.yml` | `ci.yml` |
| Environment | `pypi` | `testpypi` |

The workflow lives at `.github/workflows/ci.yml`. The environment URL in
the YAML is only a link; it does not configure authentication. No PyPI API
token is needed. These package-index settings cannot be created by editing
this repository. See the [PyPI setup guide](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).
`CODECOV_TOKEN` is optional for release success; coverage upload errors do
not block publication.

## Release steps

1. Choose a new version that has never been uploaded to **either** index.
   Update `project.version` in `pyproject.toml` and document the changes.
   `0.4.7` was already used on TestPyPI; this branch starts at `0.4.8`.
2. Commit and push the changes. Ordinary pushes, pull requests, and manual
   workflow runs build and test without publishing. Wait for all checks,
   including the optional C++ backend tests, to pass.
3. Tag that exact commit with `v` followed by the version, for example:

   ```sh
   git tag -a v0.4.8 -m "RTAMT 0.4.8"
   git push origin v0.4.8
   ```

4. The tag run checks the tag/version match, builds a wheel and source
   archive once, checks their metadata and contents, and tests each installed
   artifact outside the checkout on Python 3.8 through 3.12. It separately
   builds and tests the C++ backend on Ubuntu's system Python.
5. After validation, the same artifacts go to TestPyPI, then PyPI. Approve
   the `pypi` environment when prompted if you configured a reviewer.
6. The workflow signs the files and creates a GitHub Release with generated
   notes and downloadable distributions/signatures. Verify the package can
   be installed in a fresh virtual environment using `python -m pip install
   rtamt==0.4.8` (substitute the version being released).

Tags that do not start with `v` do not start the workflow. A mismatched
`v` tag fails before upload. Version bumps and tags are deliberate maintainer
actions; the workflow does not create them automatically.

## Retrying a release

Use GitHub's **Re-run failed jobs** to retain the already-built artifacts.
Publishing skips files already present, and GitHub Release creation/upload
can resume after partial failure. Never move a published tag, reuse a version
for changed code, or rebuild a partially published version from a new commit.
Skipping an existing file does not replace it. A code fix requires a new version.

## Package scope and local checks

The wheel is pure Python. Python 2 is no longer supported; package metadata
requires Python 3.8 through 3.12. ANTLR 4.7 imports `typing.io`, which Python
3.13 removed; newer Python support requires updating the parser/runtime
together. Native binaries are deliberately excluded so
that a local `.so` cannot accidentally be shipped in a platform-independent
wheel. The source archive includes the C++ sources and CMake files. To use
the C++ backend, build it from source and use an editable installation as
described in README.md. Publishing platform-specific native wheels would
require a separate wheel-building and native dependency-bundling process.

For local release validation, use a fresh virtual environment with Python 3.12
and a clean checkout (no old `build/`, `dist/`, or egg-info output):

```sh
python -m pip install build twine packaging pytest pytest-cov flake8
python tools/check_release.py
flake8 rtamt tests tools --select=E9,F63,F7,F82 --show-source --statistics
python -m build
python -m twine check --strict dist/*
python tools/check_release.py --dist dist
python tools/test_distribution.py wheel
python tools/test_distribution.py sdist
```

The last two commands install the artifact into the active virtual environment
and run the Python test suite from a temporary directory, avoiding imports
from the source checkout.
