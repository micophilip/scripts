#!/bin/bash
while getopts m:f flag
do
  case "${flag}" in
    m) message=${OPTARG};;
    f) force=1;;
  esac
done

if [ -z "$message" ]
then
  message="Automated backup"
fi

FILE=~/Downloads/Thesis.zip
GIT_DIR=~/src/thesis-latex

if [ -f "$FILE" ]; then
  mkdir ~/Downloads/Thesis
  cd ~/Downloads/Thesis
  unzip $FILE
  cp -Rf ~/Downloads/Thesis/* $GIT_DIR
  cd $GIT_DIR
  changes=$(git status --porcelain)
  echo $changes

  if [ "$force" == "1" ]; then
    git add .; git commit -m "$message"; git push origin main;
  else
    while true; do
        read -p "Deliver? " yn
        case $yn in
            [Yy]* ) git add .; git commit -m "$message"; git push origin main; break;;
            [Nn]* ) break;;
            * ) echo "Please answer yes or no.";;
        esac
    done
  fi

  rm -Rf ~/Downloads/Thesis
  rm $FILE
else 
  echo "$FILE does not exist. Nothing to backup"
fi