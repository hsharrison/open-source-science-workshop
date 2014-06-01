#!/bin/sh
# Replace binaries installed by the old setup.sh with aliases.

if [ -f ~/bin/ipython3 ]; then
	rm ~/bin/ipython3
fi

if [ -f ~/bin/subl ]; then
	rm ~/bin/subl
fi

if [ -f ~/bin/python3 ]; then
	rm ~/bin/python3
fi

cat ./.bash_aliases >> ~/.bash_aliases
