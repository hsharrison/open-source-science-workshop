Files and directories
===

## First look at the shell

Let's open up a shell window:

    $

The dollar sign is a prompt, telling us that the shell is waiting for input.
Type the command `whaomi` and press enter:

    $ whoami
    hen

This command shows the name of the current user.
Next run `pwd`, which stands for "print working directory":

    $ pwd
    /home/hen

Yours is probably similar, but may vary depending on your OS.

There are two sorts of file paths.
A path that starts with `/` is an absolute path, and represents a location relative to the root directory `/`.
A path that doesn't start with `/` is a relative path, and represents a location relative to the current working direcory.
If I have a directory with the absolute path `/home/hen/projects/thesis`, I can access it from `/home/hen` by just typing `projects/thesis`.

There are also three special paths. A single dot `.` represents the current working directory, and two dots `..` represents the parent of the current working directory.
So, if `pwd` is now `/home/hen`, then `.` is the same as `/home/hen` and `..` is `/home`.
Finally, the tilde `~` always represents the home directory.

The command `ls`, which stands for "listing", displays the contents of a directory.
With no argument, it gives the contents of the current directory.

    $ ls
    anaconda  BOUS  crypt    Documents  Dropbox  optim     projects  R    Ubuntu One
    bin       Copy  Desktop  Downloads  Music    Pictures  Public    SME

With an argument, we can see the contents of some other directory.

    $ ls anaconda
    bin  conda-meta  docs  envs  etc  Examples  include  lib  LICENSE.txt  pkgs  share  var

By convention in bash, options are preceded by hyphens.
If the option is more than one character, it is preceded by two hyphens.

    $ ls --all anaconda
    .                     .conkyrc         .ghc                   .kde                 projects            .steampid
    ..                    .conkyrc~        .gimp-2.8              .keystore            .psensor            .storagemadeeasy
    .adobe                .continuum       .gitconfig             .lesshst             Public              .storagemadeeasy.conf
    anaconda              .copy            .git-credential-cache  .local               .pulse-cookie       .subversion
    .apport-ignore.xml    Copy             .gksu.lock             .lua                 .putty              .synaptic
    .aptik                crypt            .gnome                 .macromedia          .PyCharm20          .texmf-var
    .aptitude             .davfs2          .gnome2                .matlab              .PyCharm30          .thumbnails
    .bash_aliases         .dbus            .gnome2_private        .matplotlib          .python_history     .tmp
    .bash_aliases~        Desktop          .gnupg                 .mozilla             R                   Ubuntu One
    .bash_history         .distlib         .gstreamer-0.10        Music                .Rhistory           .unison
    .bash_logout          .dmrc            .gtk-bookmarks         .nightingale         .rnd                .virtualenvs
    .bashrc               Documents        .gvfs                  .nzbget              .Rprofile           .wine
    .bashrc~              Downloads        .gvfs.original         .ocamlinit           .rstudio            .wine-pipelight
    .bashrc-anaconda.bak  .dropbox         .hackertray.json       .odbc.ini            .rstudio-desktop    .Xauthority
    bin                   Dropbox          .hgrc                  .opam                .selected_editor    .Xauthority.CU06ZW
    BOUS                  .dropbox-dist    .ICEauthority          optim                .smbcredentials~    .Xauthority.QTXNXW
    .cabal                .dropbox-master  .icedtea               .pam_environment     SME                 .xbmc
    .cache                .electrum        .icons                 .pam_environment~    .smpd               .Xmodmap
    .cgminer              .everpad         .inputrc               .paradoxinteractive  .speech-dispatcher  .xournal
    .cinnamon             .filezilla       .inputrc~              Pictures             .spyder2            .xsession-errors
    .cmus                 .fstab-backup    .ipython               .pip                 .ssh                .xsession-errors.old
    .config               .gconf           .java                  .pki                 .steam
    .conky                .gdfuse          .juniper_networks      .profile             .steampath

With `--all`, `ls` includes in its output all the files and directores that start with a dot. This includes `.` and `..` as well as a whole bunch of other stuff.
In Unix, files and directories starting with a `.` are hidden by default.
So a lot of programs put hidden configuration files or directories in your home directory.

Single-letter options only require one hyphen.
Additionally, multiple single-letter options can be placed on the same hyphen.
Often a long-form option will have an equivalent short-form option.
For `ls`, `-a` is shorthand for `--all`.

    $ ls -alhF anaconda
    total 112K
    drwxrwxr-x  14 hen hen 4.0K May 12 16:07 ./
    drwxr-xr-x  89 hen hen 4.0K May 26 02:23 ../
    drwxrwxr-x   2 hen hen  12K May 12 15:57 bin/
    drwxrwxr-x   2 hen hen  12K May 12 15:57 conda-meta/
    drwxrwxr-x   3 hen hen 4.0K May 12 15:57 docs/
    drwxrwxr-x   3 hen hen 4.0K May 12 16:07 envs/
    drwxrwxr-x   4 hen hen 4.0K May 12 15:57 etc/
    drwxrwxr-x   6 hen hen 4.0K May 12 15:57 Examples/
    drwxrwxr-x  45 hen hen 4.0K May 12 15:57 include/
    drwxrwxr-x   2 hen hen 4.0K May 12 15:57 .index/
    drwxrwxr-x  14 hen hen  20K May 12 15:57 lib/
    -rw-rw-r--   1 hen hen 3.7K Nov  7  2013 LICENSE.txt
    drwxrwxr-x 224 hen hen  20K May 12 16:09 pkgs/
    drwxrwxr-x  11 hen hen 4.0K May 12 15:57 share/
    drwxrwxr-x   3 hen hen 4.0K May 12 15:57 var/


Here, we added a few options:
 - `l` tells `ls` to show us the files in long form, one line at a time, with some extra information.
 - `h` is short for "human-readable", and refers to the file sizes.
   This option makes `ls` give sizes in terms of KB, MB, etc.
 - `F` adds the `/` character to the end of directories, making them stand out more.
   It also adds the symbol `*` to mark executables (commands, programs, etc.) but there aren't any in this directory.

Let's note a couple things I just did.
Pressing the up arrow allows me to repeat commands.
This lets us tweak the command and try out different variations of it.
Also, pressing tab will try to complete what you're typing, usually with contents of the current directory but sometimes with command names, depending on context.
Finally note that you can run `ls --help` to get a description of all the options you can use with `ls`.
This `--help` flag is a common Unix convention.
You can also use the `man` command, short for "manual", as in `man ls`.
Note that this won't work on Windows, I recommend just searching Google as all the man pages are online.

Two more useful shortcuts are Ctrl-A and Ctrl-E which go the beginnind and end of the line, respectively.

The command `cd` stands for "change directory".

    $ cd anaconda
    $ pwd
    /home/hen/anaconda
    $ cd ..
    $ pwd
    /home/hen


## Cloning the workshop repository

At this point let's all clone the workshop repository.
I'll explain exactly what that means later, but for now you're just downloading some files I've previously uploaded, that we'll use for some examples.
Run the following commands:

    $ mkdir -p repos

`mkdir`, as you might have guessed, makes a new directory.
I put all my repositories in a directory called `repos`.
You could call it something else or put the repository directly in your home directory if you wanted.
The `-p` flag tells `mkdir` not to throw an error if the directory you want already exists.
I put that there because who knows, you might already have a directory called `repos`.
Now `cd` into `repos` and clone the workshop repository.

    $ cd repos
    $ hg clone https://bitbucket.org/hharrison/open-source-science-workshop
    destination directory: open-source-science-workshop
    requesting all changes
    adding changesets
    adding manifests
    adding file changes
    added 25 changesets with 47 changes to 36 files
    updating to branch default
    18 files updated, 0 files merged, 0 files removed, 0 files unresolved

Let's look around.

    $ cd open-source-science-workshop/
    $ ls
    bash  conda-packages.txt  hg  readme.md

Let's look in the `bash` directory.

    $ cd bash
    $ ls
    functions  osx  windows-x64

## Setup

The first thing we'll do is runs some setup.
If you're on a Mac, run `bash osx/setup.sh`; if you're on Windows, `bash windows-x64/setup.sh`.
The command `bash`, when given a filename, invokes a new shell to run the commands in the file.
I created the bash scripts `setup.sh` to do some basic setup for you.

Let's look at the script `windows-x64/setup.sh`.
The command `cat`, short for "concatenate", combines the contents of multiple files and prints them out.
Here we just use it with one file, so it just prints the contents of that file.

    $ cat windows-x64/setup.sh
    #!/bin/bash

    echo 'Installing executables into ~/bin ...'
    mkdir -p ~/bin
    cp bin/* ~/bin    

    cat source-aliases >> ~/.bashrc

First look at the first line.
In bash, `#` starts a comment.
The first line of an executable file is called the "shebang".
It tells the OS what program is supposed to interpret the file.
In this case it is interpreted by `bash`, which lives at `/bin/bash`.

Other than the shebang, this file is a list of commands to be executed.
First we have `echo`.
`echo` just prints something to the screen, in this case a message.
Next we make a `bin` directory in the home directory.
Finally we use the `cp` command.
`cp` is short for copy-paste, and `*` is a wildcard.
So this line copies everything in `open-source-science-workshop/bash/windows-x64/bin` directory into the `~/bin` directory.
Essentially, this adds some programs to the Windows bash that are missing from the basic install.
Ignore the last line, we'll learn what that does later.

Let's do one more thing:

    $ echo $PATH
    /home/hen/anaconda/bin:/home/hen/.opam/system/bin:/usr/lib/jvm/jdk1.7.0_21/bin:/home/hen/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$HOME/.opam/system/bin

The dollar sign `$` in a command denotes a bash variable.
Some variables have special significance.
`$PATH`, for example, is a list of paths where bash will look for executables to run when you type a command.
If you look closely you'll see that `/home/hen/bin` (equivalent to `~/bin`) is listed.
This means that the binaries we just placed there should now be accessible.
If they weren't, we could edit the `$PATH` variable.

Let's check it worked.
One of the new programs is `wget` (if you're not on Windows just follow along, you already have `wget`).
`wget` is short for web get, and it downloads a file given a URL.
I don't have anything for you to download right now, but see what happens when you just run it by itself:

    $ wget
    wget: missing URL
    Usage: wget [OPTION]... [URL]...    

    Try `wget --help' for more options.

If you got that message, it means the setup script worked.

## Some more stuff

Let's try a few more commands.
Go back to the home directory.

    $ cd ~

Now let's make a dummy directory to play around in.

    $ mkdir temp
    $ cd temp

Let's try a text editor.
The most basic is `nano`.

    $ nano test.txt

Type some things and press Ctrl-X to quit.
You may also have a better text editor.
If you installed Sublime Text, you can use the `subl` command to open it up.

    $ subl test.txt

Note that now we can't do anything else in the terminal.
So quit Sublime, then try this instead:

    $ subl test.txt &

The `&` tells bash to run the program in the background, allowing you to keep working in the terminal.
This is useful for launching external programs like Sublime.
We could later run `fg` to get the program back to the foreground.
You can background it with Ctrl-Z, but this doesn't work on Windows so you'd have to quit the program entirely and run it again.
Also note that once you have a tab open in Sublime, you can leave off the `&` when opening additional files as the process is already backgrounded.

    $ touch blank.txt
    $ subl blank.txt

The command `touch` updates the "last modified" date on a file.
If the file doesn't exist, it makes a blank file.

We can delete files with `rm`:

    $ rm blank.txt

And rename them with `mv`:

    $ mv test.txt blah.txt

`mv` may be less intuitive than "rename" but you can think of renaming files as moving them.
Now that we've messed with some files, let's get rid of the directory.

    $ cd ..
    $ rm temp
    rm: `temp' is a directory

Well, `rm` doesn't do directories.
Instea we use `rmdir`.

    $ rmdir temp
    rmdir: `temp': Directory not empty

`rmdir` a safety feature that it won't delete non-empty directories.
We would first have to delete `temp/test.txt`.
But if we're feeling dangerous we can also use `rm` with the `-r` flag:

    $ rm -r temp

That does it.
In Bash, there is no recycle bin; `rm` is forever.
`rm -r` is dangerous because one typo and you can delete a bunch of work.
It's better to use `rmdir` and delete the files first.
