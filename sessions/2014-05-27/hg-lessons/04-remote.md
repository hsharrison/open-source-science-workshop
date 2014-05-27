Remote repositories
===

We can communicate with remote repositories using `clone`, `push`, and `pull`.

You should have already cloned the workshop repository.
As have I:
I've just written these tutorials and I want to upload them to the repository.
First I should make sure that I'm synchronized.

    $ hg pull
    pulling from ssh://hg@bitbucket.org/hharrison/open-source-science-workshop
    searching for changes
    no changes found

Pulling is always safe, it won't change your working directory.
If you pull in some new changesets, you would also have to run `hg update` to update your working directory.

Let's see what my directory looks like:

    $ hg status
    ? sessions/2014-05-27/hg-lessons/01-version-control.md
    ? sessions/2014-05-27/hg-lessons/02-changesets.md
    ? sessions/2014-05-27/hg-lessons/03-example.md
    ? sessions/2014-05-27/hg-lessons/2-way-merge.png
    ? sessions/2014-05-27/hg-lessons/3-way-merge.png
    ? sessions/2014-05-27/hg-lessons/centralized.png
    ? sessions/2014-05-27/hg-lessons/changeset.png
    ? sessions/2014-05-27/hg-lessons/commits.png
    ? sessions/2014-05-27/hg-lessons/diff-example.png
    ? sessions/2014-05-27/hg-lessons/diff-example/after.txt
    ? sessions/2014-05-27/hg-lessons/diff-example/before.txt
    ? sessions/2014-05-27/hg-lessons/distributed-with-central-repo.png
    ? sessions/2014-05-27/hg-lessons/distributed.png
    ? sessions/2014-05-27/hg-lessons/final.gif
    ? sessions/2014-05-27/hg-lessons/head-tip.png
    ? sessions/2014-05-27/hg-lessons/lcs.png
    ? sessions/2014-05-27/hg-lessons/working-directory.png

I haven't modified any existing files, I've just added a whole bunch of new ones that aren't tracked yet.
These all look good, so I'll add them, commit, and push.

    $ hg add
    adding 01-version-control.md
    adding 02-changesets.md
    adding 03-example.md
    adding 2-way-merge.png
    adding 3-way-merge.png
    adding centralized.png
    adding changeset.png
    adding commits.png
    adding diff-example.png
    adding diff-example/after.txt
    adding diff-example/before.txt
    adding distributed-with-central-repo.png
    adding distributed.png
    adding final.gif
    adding head-tip.png
    adding lcs.png
    adding working-directory.png
    $ hg commit -m 'add mercurial lessons'
    $ hg push
    pushing to ssh://hg@bitbucket.org/hharrison/open-source-science-workshop
    searching for changes
    remote: adding changesets
    remote: adding manifests
    remote: adding file changes
    remote: added 7 changesets with 33 changes to 29 files

In this case I already had six other commits that I hadn't pushed yet.
Now, they are all available on the BitBucket website or to anyone else who pulls from it.


# Collaboration exercise using BitBucket

The websites BitBucket and GitHub added collaboration features on top of what you can already do with `git` and `hg`.
These include issue trackers and wikis, but most importantly, forks and pull requests (PRs).
We'll do an exercise to demonstrate these concepts.

 1. Browse to the [workshop repository](https://bitbucket.org/hharrison/open-source-science-workshop).
 1. Find the "Fork" action; fork the repository.
    This creates your own personal remote clone of the repository.
    You can do whatever you want with it.
 1. Clone your new repository to your laptop.
 1. Find the file `open-source-science-workshop/sessions/2014-05-27/participants.txt`, find the line with your name, and add whatever you want to it.
    Add your last name, email address, or something completely random.
    Don't change anything else except that line.
    (If I forgot you, I apologize, add a line to the end of the file).
 1. Check `hg status` and/or `hg diff` to see the change you made.
 1. Commit
 1. Push your new changeset.
 1. Back on the BitBucket website, find the "Create a pull request" action.
    It should available from the page of my repository, as well as your fork.
    Give your PR at least a title and submit it.
 1. Once everyone has submitted a pull request I will show you what happens when I review them.

Now you know how to contribute to an open-source project!
When you collaborate, this is a good method to use for big coding projects.
For something lik a manuscript, another option is to give your collaborators write access to your repository.
Then they can push to it just like you can.


# Aliases

I have some useful aliases that I use with Mercurial.
You can find them in `open-source-science-workshop/hg/aliases.txt`.
I will go through them and explain them (if we have time).
To use them, just run `cat aliases.txt >> ~/.hgrc`.
`~/.hgrc` is a mercurial configuration file.

