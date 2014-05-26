Pipes and redirection
===

Now the interesting stuff.
Check out the contents of the directory `data`:

    $ ls -F data
    make_data.py  s01/  s02/  s03/  s04/  s05/

Here we have a Python script that I used to generate the data and five directories.

    $ cd data
    $ ls s01
    t01.txt  t02.txt  t03.txt  t04.txt  t05.txt  t06.txt  t07.txt  t08.txt  t09.txt  t10.txt

Each directory contains ten text files.
The text files contain position data in x-y coordinates from a random walk.
But let's pretend that we have participant data.

First let's look around.

    $ head s01/t01.txt
    5.633869185214487318e-01 7.164302309365390142e-01
    4.197918481459276263e-01 1.150829572338865070e+00
    1.449718336174872224e-01 9.473228591889699679e-01
    1.613438482662696849e-01 1.158944568777338979e+00
    4.817602334777835171e-01 5.314726762768537949e-01
    1.997601230222502133e-01 3.785229760278441269e-01
    6.760775525668066832e-01 1.629386645749379525e+00
    9.803604553368119312e-01 1.963103031230663209e+00
    2.714061843486313963e-01 3.873742659641731256e-01
    7.294027464534363903e-01 1.481411408884545367e+00

`head` shows the first ten lines of the file.
Here we get a sense of the format of the data.
There's also a similar command `tail`, you can probably guess what it does.

The program `wc` shows the number of characters, words, and lines in a file:

    $ wc s01/*.txt
        106     212    5300 s01/t01.txt
        109     218    5450 s01/t02.txt
         94     188    4700 s01/t03.txt
        117     234    5850 s01/t04.txt
         92     184    4600 s01/t05.txt
        107     214    5350 s01/t06.txt
        109     218    5450 s01/t07.txt
        112     224    5600 s01/t08.txt
         93     186    4650 s01/t09.txt
         95     190    4750 s01/t10.txt
       1034    2068   51700 total

Remember the wildcard expansion `*` matches any number of characters.
The shell handles the expansion, so what the `wc` program actually sees is

    $ wc s01/t01.txt s01/t02.txt s01/t03.txt s01/t04.txt ...

(you get the idea).
We can use the flags `-c`, `-w`, and `-l` to get only the number of characters, words, or lines in the file.
Let's say we want to know how long each trial was:

    $ wc -l s*/t*.txt
        106 s01/t01.txt
        109 s01/t02.txt
         94 s01/t03.txt
        117 s01/t04.txt
         92 s01/t05.txt
        107 s01/t06.txt
        109 s01/t07.txt
        112 s01/t08.txt
         93 s01/t09.txt
         95 s01/t10.txt
        100 s02/t01.txt
        113 s02/t02.txt
        116 s02/t03.txt
         88 s02/t04.txt
         97 s02/t05.txt
         90 s02/t06.txt
         98 s02/t07.txt
        103 s02/t08.txt
        111 s02/t09.txt
        114 s02/t10.txt
         96 s03/t01.txt
        119 s03/t02.txt
        110 s03/t03.txt
         82 s03/t04.txt
        115 s03/t05.txt
         97 s03/t06.txt
         86 s03/t07.txt
         86 s03/t08.txt
        104 s03/t09.txt
        103 s03/t10.txt
        109 s04/t01.txt
         85 s04/t02.txt
        119 s04/t03.txt
        118 s04/t04.txt
        103 s04/t05.txt
         81 s04/t06.txt
         90 s04/t07.txt
         95 s04/t08.txt
        112 s04/t09.txt
         89 s04/t10.txt
        109 s05/t01.txt
        112 s05/t02.txt
        117 s05/t03.txt
        104 s05/t04.txt
        101 s05/t05.txt
         91 s05/t06.txt
        111 s05/t07.txt
         93 s05/t08.txt
         94 s05/t09.txt
        111 s05/t10.txt
       5106 total

Notice that I combined two wildcards to process all the files.
But let's stick to one subject for now, and redirect the trial lengths to a file:

    $ wc -l s01/t*.txt > s01/lengths.txt

The character `>` means redirection.
Each process in Unix also has an input and an output, called "standard in" or "stdin" and "standard out" or "stdout".
By default stdin comes from some file or files (the `t*.txt` in this example) and stdout goes to the screen.
But if we use redirection, we can get the output to go to a file instead.
We can check that with `cat`:

    $ cat s01/lengths.txt
        106 s01/t01.txt
        109 s01/t02.txt
         94 s01/t03.txt
        117 s01/t04.txt
         92 s01/t05.txt
        107 s01/t06.txt
        109 s01/t07.txt
        112 s01/t08.txt
         93 s01/t09.txt
         95 s01/t10.txt
       1034 total

We can use the `sort` command to sort the file contents:

    $ sort s01/lengths.txt
         92 s01/t05.txt
         93 s01/t09.txt
         94 s01/t03.txt
         95 s01/t10.txt
        106 s01/t01.txt
        107 s01/t06.txt
        109 s01/t02.txt
        109 s01/t07.txt
        112 s01/t08.txt
        117 s01/t04.txt
       1034 total

Note that by default the output goes to the screen, if we want to output to a file we need to use a redirect:

    $ sort s01/lengths.txt > s01/sorted-lengths.txt

Note: don't try to redirect back to `lengths.txt` because a file can't be read and written to at the same time.

Let's use `head` to see what the shortest trial was:

    $ head -1 s01/sorted-lengths.txt
         92 s01/t05.txt

The flag `-1` means that we only want the first line, not the first ten.
Usually with `head` and `tail` we use a flag like this.

You're probably thinking that requiring all the intermediate files is annoying.
You'd be right; the only time we actually want intermediate files is if the data processing takes a long time.
In other cases we can run commands at the same time to avoid the need for intermediate files.
First let's delete them.

    $ rm s01/lengths.txt s01/sorted-lengths.txt

Now let's introduce the pipe, denoted with the pipe character `|`.

    $ wc -l s01/t*.txt | sort | head -1
         92 s01/t05.txt

A pipe is like two redirections in one.
It redirects the output of one command to the input of another.
This kind of composition is very powerful.
What happens is that the shell opens three processes `wc`, `sort`, and `head` at the same time.
The data flows directly from one process to the next.
Only the output of `head` goes to the screen, because we didn't redirect it anywhere else.

Two important lessons here are piecing together small programs or functions to do more complex operations, and the idea that lines of text are a primary unit of analysis.

A quick aside:

    $ ps -ef | grep python

`grep` finds lines of text containing a certain string.
So this command gets all the running processes and finds any with "python" in the name.
This is how `ps` is often used.
(On this computer I don't have anything running with Python right now.)

Back to our data analysis.
Let's try getting the longest trial:

    $ $ wc -l s01/t*.txt | sort | tail -1
       1034 total

Oops, that total line gets in the way.

    $ wc -l s01/t*.txt | sort | tail -2
        117 s01/t04.txt
       1034 total

That's better, but what if we don't want the total line at all?
There is no Unix program for getting a specific line.
Instead we have to use `head` and `tail` together:

    $ wc -l s01/t*.txt | sort | tail -2 | head -1
        117 s01/t04.txt

Note that we also could have used `sort -r` to sort in reverse order.

Finally, let's say we just want to know which trial was longest.
For that we can use the `cut` command.
`cut` takes a delimiter and divides the input into fields.
Then it takes a field number and outputs that field.
Looking at the output above, if we use the character "/" as our delimiter and grab the second field, we can get just the trial filename.

    $ wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d / -f 2
    t04.txt

A useful command here is `history`.
If we run `history` we get a list of the commands we've run in this shell.

    $ history
      294  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 2
      295  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 1
      296  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 0
      297  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 3
      298  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 5
      299  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f -1
      300  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d s -f 1
      301  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d / -f 2

Here we see all the commands that I ran trying to figure out how to get `cut` to work right (I didn't include all the output here, there were many more).
We can re-run a command using `!` and the history number.

    $ !301
    wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d / -f 2
    t04.txt

`history` is also useful with `grep`.
Here are all the commands I used with `wc` as I was testing this tutorial:

    $ history | grep wc
      246  wc *.txt
      247  wc -l *.txt
      249  wc -l *.txt > lengths.txt
      264  wc s01/*.txt
      265  wc -l s*/t*.txt
      266  wc -l s01/t*.txt > s01/lengths.txt
      273  wc -l s01/t*.txt > s01/lengths.txt
      278  wc -l s01/t*.txt > s01/lengths.txt
      284  wc -l s01/t*.txt | sort | head -1
      285  wc -l s01/t*.txt | sort | tail -1
      286  wc -l s01/t*.txt | sort | tail -2
      288  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut
      289  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 1
      290  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d ' ' -f 1
      291  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d ' ' -f 2
      292  wc --help
      294  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 2
      295  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 1
      296  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 0
      297  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 3
      298  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f 5
      299  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -f -1
      300  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d s -f 1
      301  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d / -f 2
      308  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d / -f 2
      309  wc -l s01/t*.txt | sort | tail -2 | head -1
      310  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d ' ' -f -1
      313  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d ' ' -f -1
      314  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d' ' -f1
      315  wc s01/t*.txt | sort | tail -2 | head -1 | cut -d' ' -f1
      316  wc -l s01/t*.txt | sort | tail -2 | head -1
      317  wc -l < s01/t*.txt | sort | tail -2 | head -1
      319  cat s01/t*.txt | wc -l | sort | tail -2 | head -1
      320  cat s01/t*.txt | wc -l | sort | tail -2 | head -1
      321  cat s01/t*.txt | wc -l
      323  cat s01/t*.txt | wc -
      324  wc -l s01/t*.txt | sort | tail -2 | head -1
      350  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d / -f 2
      352  wc -l s01/t*.txt | sort | tail -2 | head -1 | cut -d / -f 2
      353  history | grep wc

We can also save our history to a file after a session, in case we want to come back to it later:

    $ history > history.txt

