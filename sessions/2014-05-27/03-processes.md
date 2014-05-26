Processes
===

We've already seen a bit about processes, such as using `&` to background them.
We can use the program `ps` to display running processes.

    $ ps
          PID    PPID    PGID     WINPID  TTY  UID    STIME COMMAND
         4468       1    4468       4468  con  500 14:49:37 /bin/sh
         3188    4468    3188       5484  con  500 15:11:19 /bin/sh
         4400    3188    3188       4400  con  500 15:11:19 /c/Program Files/Sublime Text 3/sublime_text
         6424    4468    6424       3004  con  500 15:23:37 /bin/    ps

By default, `ps` shows the processes that have been launched from the current shell.
If you run `ps -ef` you can see all the processes running on your computer
(except in Windows, where `ps` only has access to the processes started from Bash).

Every process has a user, a working directory, and a process ID or "PID".
The command `kill`, with a PID, will kill a process.
So I could use `kill 4400` to kill Sublime.
On Mac or Linux you will need to use `sudo kill 4400`.
`sudo` stands for "superuser do" and runs the next command with administrator permissions.
You will need to enter a password.
On Windows if you ever get a "permision denied" error, the solution is not to run `sudo` but to re-launch your shell with administrator privileges.

Also, Ctrl-C kills the current foreground process.
