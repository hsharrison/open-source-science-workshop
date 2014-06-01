#!/bin/sh -e

echo 'Installing executables into ~/bin ...'
mkdir -p ~/bin
cp bin/* ~/bin

cat source-aliases >> ~/.bashrc
cat .bash_aliases >> ~/.bash_aliases
