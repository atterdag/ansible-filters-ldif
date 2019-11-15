#!/usr/bin/env bash
if [[ ! -f ~/.pypirc ]]; then
  echo 'no ~/.pypirc exist!'
  exit 1
fi

tox

pip install --upgrade gitchangelog twine

OLDVERSION=$(grep version setup.py | sed -e "s/.*='//" -e "s/',//")

vi setup.py

VERSION=$(grep version setup.py | sed -e "s/.*='//" -e "s/',//")
if [[ $OLDVERSION == $VERSION ]]; then
    echo "Old version $OLDVERSION same as $VERSION"
    echo 'Press [ENTER] to continue (cntrl-c to quit)'
    read ANS
else
  git tag -a $VERSION -m v$VERSION
  gitchangelog
  vi CHANGELOG.rst
fi

echo "Ready to push $VERSION?"
echo 'Press [ENTER] to continue (cntrl-c to quit)'
read ANS
git commit -m "Version $VERSION" CHANGELOG.rst setup.py
git push origin master
git tag --force  -a $VERSION -m v$VERSION
git push origin --tags

echo "Ready to build and push $VERSION to PiPY?"
echo 'Press [ENTER] to continue (cntrl-c to quit)'
read ANS
rm -rf dist
python setup.py sdist bdist_wheel
twine check
twine upload dist/*
