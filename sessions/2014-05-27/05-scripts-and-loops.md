Scripts and loops
===

Now that we've developed that analysis pipeline, we have to admit that it's a bit hard to remember.
If we want to use it again later, it would be nice to package it for easy re-use.
To do that we make a script.
I already made one in `longest-file`.

    $ cat ../longest-file
    #!/bin/bash
    # Output the filename of the longest file in a directory.
    
    wc -l "$1"/* | sort | tail -2 | head -1 | cut -d / -f 2

Here we see the shebang that we've seen before.
Then we have a comment.
Now we have the actual command.
The only change from what we wrote before is that we now have `$1`.
That means "the first argument given to this script".
We put the varaible in quotes so that it will stay in one piece if it has any spaces in it.
Note that we have to keep the `/` because that's we use as the delimiter in `cut`.
So this script looks at all the files inside any given directory.

Let's test it.
First one thing, in order to make a file directly executable (so we can run `../longest-file` instead of `bash ../longest-file`) we need to make add execute permissions.
I already did this, but if the next bit doesn't work for you, run this:

    $ chmod +x ../longest-file

This means add the execute permission (`+x`) to `../longest-file`.

OK, to test it:

    $ ../longest-file s01
    t04.txt

It works!
The reason we need the `../` is because `longest-file` is in the parent directory.
If we want to be able to use it wherever we are, we can put it in a folder on the path.
We've already put some executables in `~/bin`, let's put this there:

    $ cp ../longest-file ~/bin

Now we can use it directly:

    $ longest-file s01
    t04.txt

Finally, let's use this in a larger example.
We want to plot one trial for each participant, and we may as well use the longest trial.
To do that we use a loop.
Here's how loops work in Bash:

    $ for dir in s*  
    > do             
    > echo $dir      
    > done           
    s01              
    s02              
    s03              
    s04              
    s05

Note that the prompt changed from `$` to `>` to indicate that we're still running the same command.
All we did here is `echo` each directory we want to analyze.
This is a good way to test what we're doing and build our process step by step.
First `echo` the command you'd like to run.
If it looks right, run it by taking out the `echo`.

    $ for dir in s*
    > do
    > echo longest-file "$dir"
    > done
    longest-file s01
    longest-file s02
    longest-file s03
    longest-file s04
    longest-file s05

Now we're echoing the commands we want to run on each directory.
How do we actually run them?
We could get rid of the `echo`:

    $ for dir in s*
    > do
    > longest-file "$dir"
    > done
    t04.txt
    t03.txt
    t02.txt
    t03.txt
    t03.txt

Another option is to use backticks, `\``.
Anything inside backticks gets executed separately before evaluating the whole line.
So the above is the same as

    $ for dir in s*
    > do
    > echo `longest-file "$dir"`
    > done
    t04.txt
    t03.txt
    t02.txt
    t03.txt
    t03.txt

This runs `longest-file` on each directory and sends the output to `echo`, which is the same as what we did before since by default the output goes to the screen.
This is necessary if we want to use something other than echo, though.
Imagine we have a command called `plot` that generates the plots we want.
Then we could make a loop to plot the longest trial in each directory.

We don't actually have a command called `plot` at this point, so let's use `echo` to print the commands that we would like to run.

    $ for dir in s*
    > do
    > echo plot "$dir"/`longest-file "$dir"`
    > done
    plot s01/t04.txt
    plot s02/t03.txt
    plot s03/t02.txt
    plot s04/t03.txt
    plot s05/t03.txt

This is the same as above, except we've added `"$dir"/` in order to tell the `plot` command specifically which file we want, in which directory.
If we just took out the `echo` this would actually run the comands instead of printing them.
And if this was actually how we generated our plots, we'd want to save those four lines into a script, so that we could easily recreate them if our data changed.
