Customizing Mercurial
=====================

*Note: all relative paths mentioned here are relative to `open-source-science-workshop/hg`.*


## Intro
There are two configuration files you should worry about:

 1. A user file in `~/.hgrc`.
    (On Windows there are two, there is also `~/mercurial.ini`.
    It's OK to use both files.)
    This file applies to every repository.
 2. A repository specific file in `/path/to/repo/.hg/hgrc`.

This document discusses customization with regard to #1 only.

Some useful `hg` commands related to configuration.

 - Get help on configuration, including all the different configuration files and all the different options you can configure: `hg help config`.
   The output is very long, so you may want to do `hg help config | less`.
 - Edit your user config: `hg config -e`.
   This is just a shortcut to open your config file in your default text editor.
   Remember that if you never changed your default editor this is a bad idea,
   you'll get stuck in `vim` on OSX or open Notepad on Windows.
   Both are bad news.
   You can always find the config file in the GUI and open it that way!
   (See below for how to change your default editor.)

The config files are broken into sections, denoted by square brakets.
Sections can appear multiple times so don't worry if your config file gets messy.

You can also edit your settings in the GUI through TortoiseHG, that may be easier for some things.


## Default text editor

It is possible to change your system-wide default text editor, which you may want to Google.
However, it is easy to change your editor with respect to hg, which tells hg which editor to use, for example, when you run `hg commit` or `hg config -e`.
Just add the following to your `~/.hgrc` under `[ui]`:

    editor = subl

That assumes, of course, that you want Sublime as your default editor and you've setup a shortcut or alias `subl` to get to it.


## Aliases
Under a section `[Aliases]` you can put, well, aliases.
For example, if you have `latest = log --limit 5`, then running `hg latest` will give you a log of the last five commits.
I have saved all my aliases in `aliases.txt`.
To use them in your `hg`, run `cat aliases.txt >> ~/.hgrc`.
However, take a look at the file.
Note that some of the aliases have a path in them.
These are pretty log styles that someone made, but for them to work you have to download them.
This should do the trick:

    cd ~/repos
    mkdir -p external  # Not sure if you have this directory yet
                       # I like to keep other people's repos separate
    cd external
    hg clone https://bitbucket.org/sjl/mercurial-cli-templates

Feel free to clone into a different directory, but then you have to change the paths in `~/.hgrc`.

One more thing, the alias `sglog` ("short graph log") also requires the extension "graphlog",
and some others may require the extension "color".
To activate this, add the following under `[Extensions]` (no need to download anything):

    graphlog =
    color =

(This is how you activate the extensions that come included with mercurial.
Nothing to the right of the equal sign.)

These aliases are worthless if you never use them, so read through the list and see if you can figure out what they do (or just try them out I guess)!
Many of them are just shorter versions of common commands.


## Prompt
I have my bash prompt set up to give me an indicator when I'm in a repo.
It shows an exclamation point if I have uncommitted changes, a qusetion mark if there are untracked files, etc.
It also shows what branch I'm in--we haven't talked much about branches but it's almost always `default`.
I set this up following instructions [here](http://stevelosh.com/blog/2009/03/candy-colored-terminal/) and [here](http://stevelosh.com/blog/2009/03/mercurial-bash-prompts/
)
(note: there are some additional instructions on that page for getting colored prompts on OSX.
I've tested these instructions on Linux and Windows at least).

I've put some basic instructions as a comment in `prompt.txt` but I'll repeat it here.

This requires an extension called hg-prompt.
You also have to download it.

    cd ~/repos/external
    hg clone https://bitbucket.org/sjl/hg-prompt

Extensions are defined under the section `[Extensions]` in `~/.hgrc`.
So edit `~/.hgrc` and add this:

    [Extensions]
    prompt = $HOME/repos/external/hg-prompt/prompt.py

Note that you'll have to change the path if you cloned the repo somewhere else.

Finally, stick the bash code in `prompt.txt` in your `~/.bashrc` to run automatically when you start Bash:

    cat prompt.txt >> ~/.bashrc

Remember you will need to open up a new terminal for these changes to take effect.
