"""Validate release tags and distribution contents before publishing (Python 3.11+)."""

import argparse
from email.parser import BytesParser
import os
from pathlib import Path
import tarfile
import tomllib
import zipfile

from packaging.version import Version
from packaging.specifiers import SpecifierSet


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path)
    args = parser.parse_args()
    project = tomllib.loads(Path('pyproject.toml').read_text(encoding='utf-8'))['project']
    version = project['version']
    if str(Version(version)) != version:
        raise SystemExit('Use a canonical PEP 440 version in pyproject.toml')
    ref = os.environ.get('GITHUB_REF', '')
    if ref.startswith('refs/tags/') and ref != 'refs/tags/v' + version:
        raise SystemExit('Release tag must be v' + version)
    if not args.dist:
        return
    wheels = list(args.dist.glob('*.whl'))
    sdists = list(args.dist.glob('*.tar.gz'))
    if len(wheels) != 1 or len(sdists) != 1:
        raise SystemExit('Expected exactly one wheel and one source archive')
    with zipfile.ZipFile(wheels[0]) as archive:
        names = archive.namelist()
        if wheels[0].name != 'rtamt-{}-py3-none-any.whl'.format(version):
            raise SystemExit('Expected a pure Python wheel matching the project version')
        metadata = BytesParser().parsebytes(archive.read('rtamt-{}.dist-info/METADATA'.format(version)))
        if SpecifierSet(metadata['Requires-Python']) != SpecifierSet(project['requires-python']):
            raise SystemExit('Wheel Python requirement does not match pyproject.toml')
        for name in names:
            if not name.startswith(('rtamt/', 'rtamt-{}.dist-info/'.format(version))):
                raise SystemExit('Unexpected wheel entry: ' + name)
            if name.startswith(('rtamt/lib/', 'rtamt/cpplib/')) or name.endswith(('.so', '.pyd', '.dll')):
                raise SystemExit('Native files must not be in the pure Python wheel: ' + name)
        if 'rtamt/__init__.py' not in names:
            raise SystemExit('Wheel is missing the RTAMT package')
    with tarfile.open(sdists[0]) as archive:
        names = {member.name for member in archive.getmembers()}
        root = 'rtamt-' + version + '/'
        for required in ('pyproject.toml', 'LICENSE', 'rtamt/__init__.py', 'rtamt/CMakeLists.txt',
                         'rtamt/cpplib/stl/rtamt_stl_library_wrapper/CMakeLists.txt'):
            if root + required not in names:
                raise SystemExit('Source archive is missing ' + required)
        if any(name.startswith(root + directory + '/') for name in names
               for directory in ('tests', 'examples', 'rtamt/lib', 'rtamt/build')):
            raise SystemExit('Source archive contains excluded files')
    print('Release metadata and distribution contents are valid')


if __name__ == '__main__':
    main()
