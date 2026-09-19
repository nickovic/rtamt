"""Install a release artifact and test it without importing the checkout."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('distribution', choices=('wheel', 'sdist'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    pattern = '*.whl' if args.distribution == 'wheel' else '*.tar.gz'
    artifacts = list((root / 'dist').glob(pattern))
    if len(artifacts) != 1:
        raise SystemExit('Expected exactly one ' + args.distribution)
    env = dict(os.environ)
    env.pop('PYTHONPATH', None)
    with tempfile.TemporaryDirectory(prefix='rtamt-installed-') as directory:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--force-reinstall', str(artifacts[0])],
                       cwd=directory, env=env, check=True)
        subprocess.run([sys.executable, '-m', 'pip', 'check'], cwd=directory, env=env, check=True)
        shutil.copytree(root / 'tests' / 'python', Path(directory) / 'tests')
        subprocess.run([sys.executable, '-c',
                        'import rtamt; print("Testing installed RTAMT:", rtamt.__file__)'],
                       cwd=directory, env=env, check=True)
        subprocess.run([sys.executable, '-m', 'pytest', 'tests', '--import-mode=importlib',
                        '--cov=rtamt', '--cov-report=xml:' + str(root / 'coverage.xml')],
                       cwd=directory, env=env, check=True)


if __name__ == '__main__':
    main()
