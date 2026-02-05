import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.DelegationParentalAuthority',
      version='1.0.0',
      description=('Delegation of Parental Authority'),
      long_description='# docassemble.DelegationOfParentalAuthority\r\n\r\nDelegation of Parental Authority\r\n\r\n## Author\r\nMichigan Legal Help\r\n\r\n## Changelog\r\n* 2/5/26  1.0.0 Initial launch',
      long_description_content_type='text/markdown',
      author='Michigan Legal Help',
      author_email='michiganlegalhelp@mplp.org',
      license='MIT',
      url='https://michiganlegalhelp.org',
      packages=find_namespace_packages(),
      install_requires=['docassemble.AssemblyLine @ git+https://github.com/SuffolkLITLab/docassemble-AssemblyLine.git@bates_number_to_aldoc', 'docassemble.mlhframework @ git+https://github.com/mplp/docassemble-mlhframework.git@AddFunction'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/DelegationParentalAuthority/', package='docassemble.DelegationParentalAuthority'),
     )
