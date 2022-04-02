# QoubDiscordBot

This is a Discord bot that will call the Qoub API when summoned, and reply with a relevant coub.

This bot is part of the larger Qoub project I have going on, which will serve as a way for myself to access my archive of Coubs, in various different ways.

# Commands

The default prefix for accessing this bot is !qoub and to this, you can supply some arguments:


- -help <br />
Replies with a link to this repository and section.
- -cat &lt;category&gt; <br />
Replies with a random coub from a specific category.
- -pop <br/>
Replies with the most popular coub in the archive.
- -pop &lt;nth-popular&gt; <br />
Replies with the nth-most popular coub in the archive.
- -order &lt;likes / views&gt;

Some of these arguments can be mixed together, to construct more detailed queries.

## Example of some commands

- !qoub <br />
Returns a random coub from a random category.
- !qoub help <br />
Replies with a link to this repository and section.
- !qoub -cat &lt;category&gt; <br />
Replies with a random coub from a specific category.
- !qoub -pop <br/>
Replies with the most popular coub in the archive.
- !qoub -pop &lt;nth-popular&gt; <br />
Replies with the nth-most popular coub in the archive.
- !qoub -ord &lt;likes / views&gt; <br />
Changes the fildering mode for the popular argument.
- !qoub -cat &lt;category&gt; -pop &lt;nth-popular&gt; <br/>
Replies with the nth-most popular coub from a specific category.

# To-do

- Make sure, after downloading a video and displaying it, that said video is deleted from local storage.
- Yeet all code over to a src folder.