Open Source Science Workshop
===
## Summer 2014

This workshop will teach computing skills that will increase your productivity as a scientist.
Some inspiration is taken from the open-source software community toward the goals of open science and reproducible research.
The core topics are:

 - the Python programming language and its scientific ecosystem,
 - version control using Git and Mercurial,
 - the Unix shell, and
 - general best practices.

## Motivation

Most scientists these days must have a certain amount of computer literacy in order to collect and analyze data.
We often learn how to do one specific thing at a time, when it comes up (e.g., how to do FFT in Matlab.)
Because most of us are self-taught, we never learn general software-development principles, such as organizing code for easy reuse.
As a result, scientists quite often waste time due to duplicated effort.
We continually run into problems that have already been solved by software developers.

In particular, we have a lot to learn from the open-source software community, and not just about computing.
The open-source software development process is similar to how we believe science *should* work.
It is completely transparent, with all the failed attempts, design decisions, and even the communication between developers publicly visible.

We will start with the basic assumption that all code contains mistakes.
Therefore, given the current state of scientific computing, most published data analyses have mistakes.
Hopefully these are minor mistakes, but most of the time we will never know, because the code that ran the statistical tests and generated the figures was never published.
One workshop is not going to change much, but my hope is that participants will ...

 - Never again be embarrassed to publish code with their results.
 - Never again look at code six months later and have no idea what they were trying to do.
 - Never again write code that someone else has already written (in fact, they may never write any *interesting* code, only "glue" code).
 - Never again work on a document with a filename like 'manuscript revisions v3 (1).docx'.
 - Never again use a workflow dependent on copy-paste, code templates, or commenting and uncommenting sections of code.
 - Never again be reluctant to change something because of how many analysis steps they will have to re-do afterwards.
 - Never again bike into the lab at 9pm in order to grab a USB stick with the latest code.

 For more along these lines, and a previous of some of our topics, see [Wilson et al. (2014), Best practices for scientific computing.][best]

## Schedule of topics


## Setup

Ideally we will all come prepared with everything already installed on our laptops before the first day. Please follow the instructions [at software-carpentry.org][setup], with the following revisions:

 - We will not be using SQL, skip that part.
 - Create an account at [Bitbucket][bitbucket] (sign up with your `.edu` email address and you will automatically get the generous academic plan).
 - Follow [Bitbucket's guide to setting up Git and Mercurial][hggitsetup].
 This goes slightly beyond the software-carpentry guide: it also directs you to install Mercurial, and it helps you link both Git and Mercurial to your Bitbucket account.
 - Install [PyCharm Community Edition][pycharm]. 
It's the IDE I use for Python and it will work best if we're all on the same platform.
You will still want a lightweight text editor, especially older computers which might struggle with PyCharm.
I recommend [Sublime Text 3][sublime], though it doesn't really matter.


[best]: http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001745
[setup]: http://software-carpentry.org/v5/setup.html
[bitbucket]: http://software-carpentry.org/v5/setup.html
[hggitsetup]: https://confluence.atlassian.com/display/BITBUCKET/Set+up+Git+and+Mercurial
[pycharm]:http://www.jetbrains.com/pycharm/download/
[sublime]:http://www.sublimetext.com/3
