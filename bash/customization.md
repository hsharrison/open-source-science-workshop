Customizing Bash
================

*Note: all directories are relative to `open-source-science-workshop/bash`.*


## Aliases

I've included a few aliases that I use in `.bash_aliases`.
Install them on your machine with

    cat .bash_aliases >> ~/.bash_aliases

Check the file first and see what they do!
They're pretty simple.


## Automatically run `ls` after `cd`

I accomplished this by writing a replacement function `cd`.
I put it in `functions/ls-after-cd`.
To install it on your machine, run

    cat functions/ls-after-cd >> ~/.bashrc

After installing this, you may ocassionally find your directory contents printing out at unexpected times.
This is probably because you ran a script that calls `cd` somewhere in the middle.
Let me know what you were doing when that happened and I'll try to add the special case into the function.


## Keyboard control on the terminal

What different keys do is regulated by a file called `.inputrc`.
I've put one here in this directory.
Instead of blindly copying it your home directory, I recommend manually editing a file `~/.inputrc` and choosing what lines to copy over from the `.inputrc` in this directory.
There is a description above each change.
For example, you may prefer the way tab-completion works for you now, instead of cycling through all matches like it will with this `.inputrc`.

In `.inputrc`, the first part of the lines contain an escape sequence, which is a code for a particular character.
It's possible that these are different on your computer than on mine.
I found a bit [here](https://code.google.com/p/iterm2/wiki/Keybindings) on how to check your escape sequences (at the bottom page).
Note that `.inputrc` doesn't go into effect until you reload Bash, so don't conclude that it's not working until you do so.
Also note that you must use `\e` in `.inputrc` to start each escape sequence.
If you use one of the methods on the me website, and get something that starts with `^[`, replace those two characters with `\e`.
For example, when I run Ctrl-v and then shift-tab, I get this on my screen: `^[[Z`.
But the correct way to use shift-tab in `.inputrc` (for me) is `\e[Z`.
