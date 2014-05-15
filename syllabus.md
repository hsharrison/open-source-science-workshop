Open Source Science Workshop
===
## Summer 2014

Instructor: [Henry Harrison][me]

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
Because most of us are self-taught, we never learn general software-development principles, such as how to organize code for easy reuse.
As a result, scientists often waste time due to duplicated effort.
We continually run into problems that have already been solved by software developers.

In particular, we have a lot to learn from the open-source software community, and not just about programming.
The open-source software development process is similar to how we believe science *should* work.
It is completely transparent, with all the failed attempts, design decisions, and even the communication between developers publicly visible.
In science, on the other hand, 99% of the time we only see the final product.
In the face of a questionable finding, a replication can be attempted, but the actual data collection and analysis process cannot be closely scrutinized.

With programming skills, scientists can not only be more productive but also take on a more reliable workflow. If we learn from the open-source community, this can have the welcome side effects of making our workflows more visible, maintainable, and reproducible.

Here are some of the things I hope that participants will be able to avoid in the future:

 - Embarrassment about sharing or publishing code.
 - Inability to understand code they wrote the previous semester.
 - Documents with filenames like `manuscript_revisions_v3_comments (2)`.
 - Inability to reproduce a result due to change in software or loss of the exact steps taken.
 - A programming workflow dependent on copy-paste, code templates, or commenting and uncommenting.
 - Reluctance to make a small analysis change because of how many steps will need to be re-done to recreate the manuscript.

 For more along these lines, and a preview of some specific points, see [Wilson et al. (2014), Best practices for scientific computing.][best]

## Schedule of topics
Each session will be three hours, including a break. The material will be hands-on whenever possible.
 
 1. The Unix shell, version control.
 1. Python basics, built-in data structures.
 1. Iterators and generators, object-oriented programming.
 1. Functional programming, array programming.
 1. The Scientific Python ecosystem.
 1. Data analysis.
 1. Defensive programming, development strategies.
 1. Figures and visualizations, automating experiments.
 1. Dynamic documents, makefiles.
 1. Overflow session.

 I am open to feedback on this list and may modify it as we go depending on everyone's priorities and interests.

## Setup

Ideally everyone will come prepared with everything already installed on our laptops before the first day. Please follow the instructions [at software-carpentry.org][setup], with the following revisions:

 - We will not be using SQL, skip that part.
 - Windows users: the software-carpentry page links to an older version of Git for Windows.
   Get the latest version [here][msysgit].
 - Create an account at [Bitbucket][bitbucket]
   (sign up with your `.edu` email address and you will automatically get the academic plan).
   Follow [Bitbucket's guide to setting up Git and Mercurial][hggitsetup].
   This goes a bit beyond the software-carpentry guide:
   it also directs you to install Mercurial, and links both Git and Mercurial to your Bitbucket account.
 - Optionally, install [PyCharm Community Edition][pycharm]. 
   It's the IDE I use for Python, I can't recommend it enough, and you may find it advantageous to use the same tools as I do.
   However, any editor will do, including Spyder which will be installed with Anaconda if you follow the software-carpentry guide.
 - You will still want a lightweight text editor.
   I recommend [Sublime Text 3][sublime] on all platforms, though it doesn't really matter.
 - Toward the end of the workshop, we will use [Pandoc][pandoc] for document generation.
   Also follow the instructions on that link for installing LaTeX on your platform.

Please [contact me][me] if you run into problems getting set up.


[best]: http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001745
[setup]: http://software-carpentry.org/v5/setup.html
[bitbucket]: http://software-carpentry.org/v5/setup.html
[hggitsetup]: https://confluence.atlassian.com/display/BITBUCKET/Set+up+Git+and+Mercurial
[pycharm]:http://www.jetbrains.com/pycharm/download/
[sublime]:http://www.sublimetext.com/3
[me]: mailto:henry.harrison@uconn.edu
[pandoc]: http://johnmacfarlane.net/pandoc/installing.html
[msysgit]: http://msysgit.github.io/
