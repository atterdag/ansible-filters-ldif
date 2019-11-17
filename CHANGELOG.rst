Changelog
=========


0.0.7 (2019-11-17)
------------------
- Added test deploy to Test PyPI. [atterdag]
- Added deploy section when master branch is merged. [atterdag]
- Cleaned up .travis.yml. [atterdag]
- Changed test requirement to build requirements. [atterdag]
- Added minimum version of tox supported. [atterdag]
- Added additional check regarding pip packaging. [atterdag]
- Expanded py27, and py36 to run ansible playbook. [atterdag]
- Added pip module dependencies to pep8 section. [atterdag]
- Replaced specific functional testing with default pytest in generic
  [testenv] [atterdag]
- Renamed virtualenv to testenv because using python-development was a
  mistake. [atterdag]
- Removed [python-development:venv] section because I can't see that I
  need it. [atterdag]
- Aligned indentation in tox.ini. [atterdag]
- Disabled support for python 3 because the ldif module is broken in
  python 3. [atterdag]
- Ldif.py cannot adhere to PEP8 E402, so we have to ignore it.
  [atterdag]
- Moved ansible playbook to test directory. [atterdag]
- Changed StringIO module import to use Ansibles six implementation.
  [atterdag]
- Differentiated between error messages in to_ldif method. [atterdag]
- Moved PEP8 exception to pytest.ini, so its can be reused whenever
  pytest is called. [atterdag]
- Added test upload to Test PyPI before uploading to _real_ PiPY.
  [atterdag]
- Renamed examples to testing. [atterdag]
- Made ansible playbook specific to testing filters. [atterdag]


0.0.6 (2019-11-16)
------------------
- Improved upload script to handle also testing. [atterdag]


0.0.5 (2019-11-16)
------------------
- Got rid of all the _query_ stuff in the various descriptions. This
  filter only reads, and writes LDIF. [atterdag]
- Renamed ansible playbook 'play.yml' to 'playbook.yml' to make it more
  clear how to run it. [atterdag]
- Improved name of task in example playbook. [atterdag]


0.0.4 (2019-11-16)
------------------
- I kinda broke my setup.py so it didn't include the actual python code.
  [atterdag]


0.0.3 (2019-11-16)
------------------
- First travis pipeline. [atterdag]
- Replaced jenkins with travis build status icon. [atterdag]
- Forgot to add ```dist/*``` as argument for twine check. [atterdag]


0.0.2 (2019-11-15)
------------------
- 2nd attempt tp upload. [atterdag]
- Fixed formatting errors in README.rst. [Valdemar Lemche]
- Initial version of module, and files to support pushing code to pipy.
  [atterdag]


0.0.1 (2019-11-15)
------------------
- Initial Commit [Valdemar Lemche]
