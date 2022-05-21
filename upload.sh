#!/usr/bin/env bash

echo
echo '******************************************************************************'
echo '* Ensuring that pip build requirements are installed and upgraded.'
pip install --upgrade --requirement requirements.txt

echo
echo '******************************************************************************'
echo '* Get old version from setup.py'
OLDVERSION=$(grep version setup.py | sed -e "s/.*='//" -e "s/',//")

echo
echo '******************************************************************************'
echo '* Ready to update setup.py?'
echo '* Press [ENTER] to continue (cntrl-c to quit)'
read ANS
vi setup.py

VERSION=$(grep version setup.py | sed -e "s/.*='//" -e "s/',//")
if [[ $OLDVERSION == $VERSION ]]; then
  echo
  echo '******************************************************************************'
  echo "* Old version $OLDVERSION same as $VERSION"
  echo '* Press [ENTER] to continue (cntrl-c to quit)'
  read ANS
else
  echo
  echo '******************************************************************************'
  echo "* Ready to push $VERSION to GitHub?"
  echo '* Press [ENTER] to continue (cntrl-c to quit)'
  read ANS
  git tag -a $VERSION -m v$VERSION
  gitchangelog
  vi CHANGELOG.rst
  git commit -m "Version $VERSION" CHANGELOG.rst setup.py
  git push origin master
  git tag --force  -a $VERSION -m v$VERSION
  git push origin --tags
fi

echo
echo '******************************************************************************'
echo "* Ready to build $VERSION?"
echo '* Press [ENTER] to continue (cntrl-c to quit)'
read ANS
if [[ -d dist ]]; then
    rm -rf dist
fi
python setup.py sdist bdist_wheel
twine check dist/*

echo
echo '******************************************************************************'
echo "* Ready to tox test $VERSION?"
echo '* Press [ENTER] to continue (cntrl-c to quit)'
read ANS
tox

echo
echo '******************************************************************************'
echo "* Ready to push $VERSION to TestPyPI?"
echo '* Press [ENTER] to continue (cntrl-c to quit)'
read ANS
if [[ ! -f ~/.pypirc ]]; then
  echo 'no ~/.pypirc exist!'
  exit 1
fi
twine upload dist/* -r ansible-filters-ldif-test
