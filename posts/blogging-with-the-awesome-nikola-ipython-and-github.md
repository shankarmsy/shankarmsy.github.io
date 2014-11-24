<!-- 
.. title: Blogging with the awesome Nikola, IPython and Github
.. slug: blogging-with-the-awesome-nikola-ipython-and-github
.. date: 2014-09-23 01:57:19 UTC-08:00
.. tags: Blogging, Nikola, IPython, Github, Octopress
.. link: 
.. description: blogging with the awesome nikola, ipython and github
.. type: text
-->

So glad to finally be writing my first post with [**Nikola**](https://www.getnikola.com). It truly provides an awesome, fun way of setting up a static website/blog and gives you complete control every step of the way. It took me a while to get this setup working but boy am I pleased with the results. It's written completely in Python, is blazingly fast, features an **IPython** plugin that lets you create and share IPython content directly and deploys easily to **Github**, giving you version control for your blog. Everything is 100% customizable and to top it off, is completely free. *Can it get any better?*

So without further ado, below I will attempt explain the steps I followed to successfully set up a site with Nikola, configure the IPython plugin for Nikola and setup a Github page to deploy the website. Before I begin, a quick disclaimer. These are steps that worked well for me and I hope will help you too. But I would recommend you take a look at [Damian Avila's blog posts](http://www.damian.oquanta.info/index.html).

Let's get started.
<!-- TEASER_END -->

#So What is Nikola?
Nikola is a python-based static site generator that takes its name from the great [Nikola Tesla](http://http://en.wikipedia.org/wiki/Nikola_Tesla), best known for his contributions to alternating current (AC), the electricity that powers everything we do.

Funnily enough though, I remember him best (the character, not the man) from the classic movie Prestige by Christopher Nolan (big fan!).

![ ](https://raw.githubusercontent.com/ShankarMsy/shankarmsy.github.io/master/galleries/Inserts/nikola.jpg  "A still from Prestige, source BBC")

Ok, so a natural first question to ask is, what is a static website?

In the words of Roberto Aslina, the creator of Nikola:
>*In a static site, the whole site, every page, everything, is created before the first user even sees it and uploaded to the server as a simple folder full of HTML files (and images, CSS, etc).*

So what is the difference between Nikola and a blogging platform like Wordpress? With Wordpress, the contents of your site live in a database known only to Wordpress and your blog is generated, in other words, converted to a presentation-ready HTML only when someone wants to see the page. Whereas with Nikola, the entire site lives in a folder on your laptop (or on Github if you maintain your source there) and is built and published, by you. The site is pre-built (you get to see it before anyone else does) and available once you deploy, whether or not someone wants to see the page. What's the benefit? Static websites will always load faster simply because it doesn't waste time re-building the site everytime.

That does it for me but Roberto below nicely illustrates more advantages:

[http://getnikola.com/handbook.html#why-static](http://getnikola.com/handbook.html#why-static)

###Features
Nikola has some wonderful features, excerpt below from their [website](https://getnikola.com):

- Blogs, with tags, feeds, archives, comments, etc.
- Themable
- Fast builds, thanks to doit
- Flexible, extensible via plugins
- Small codebase (programmers can understand all of Nikola core in a day)
- reStructuredText [Cheatsheet] or Markdown as input language (also Wiki, BBCode, Textile, AsciiDoc, Python Notebooks, Misaka, Pandoc, txt2tags, orgmode, and HTML)
- Easy image galleries (just drop files in a folder!)
- Syntax highlighting for almost any programming language or markup
- Multilingual sites, translated to 18 languages.
- Doesn't reinvent wheels, leverages existing tools.
- Python 2 and 3 compatible.

For me the killer feature is the **IPython plugin**, integrating the capabilities of IPython seamlessly with Nikola and makes blogging with IPython a snap. You can even go one step further and setup bi-directional communicaton between IPython and Nikola, as damien has shown [here](http://www.damian.oquanta.info/posts/bidirectional-ipython-nikola-workflow-to-write-your-blog-post.html).

#A few words on Octopress
One of the reasons I started this blog is primarily to learn and share content related to Data Science, see my [About Page](https://shankarmsy.github.io/stories/about.html) to learn more about me. When I began this quest, there was one thing I was sure of and that was hosting the site on Github. In case you're wondering, it's super easy to host a [page](https://pages.github.com/) on Github (more on this later).

###Step in, Jekyll
Naturally, the first place I looked was Jekyll, a blog-aware static site generator for Github. As a matter of fact, Jekyll powers the Github pages. It works on the same lines of Nikola, using markdown syntax to render plain-old text files as HTML pages. Basically you type in a text file in Markdown syntax and it gets rendered as HTML. The catch? With Jekyll, you still have to write all your own HTML, CSS, etc. Pretty sure any good front-end dev would jump at the opportunity but I am not sure I had the time to invest and learn through the process of hand-building my site. That's where Octopress came in handy!

###Hello Octopress
Octopress is a framework designed by Brandon Mathis and it's based on Jekyll. The difference, it takes care of HTML templates, CSS and so on for you. Similar to Nikola, it gives you more pre-built content that you can choose from and there are plenty of themes available to choose from. I tried and eventually succeeded in setting up a site based on Octopress, but two things turned me away:

**No Support for IPython**

This was the dealbreaker. I've chosen Python as my primary toolset for Data Science and my whole idea is to use IPython as the delivery mechanism to share my code snippets, learning/demonstrations etc. and I found no good way to convert the .ipynb notebooks to render well on an Octopress site. Even converting to HTML basic (without formatting) using nbconvert seemed to break the site somehow.

Jake Vanderplas explains the difficulties in configuring IPython for Octopress below:

[https://jakevdp.github.io/blog/2012/10/04/blogging-with-ipython/](https://jakevdp.github.io/blog/2012/10/04/blogging-with-ipython/)

Jake provided a workaround in his article but unfortunately I couldn't get it working. Moreover (with all respect to Jake) I really needed a more convenient solution if I am going to be doing this on a daily basis.

**Octopress is based on Ruby**

Not that there is anything wrong with it, but I am a total Ruby noob and I found it a bit cumbersome to install and configure the environment. Also, considering my need to focus on Python it made more sense to work in a Python based environment. I also found Octopress to be a tad slow compared to Nikola, but that's just my personal opinion.

Nevertheless, take nothing away from Octopress, it still is a great way to static blog. Check out these sites to learn more if you're interested:

Octopress site has great documentation:

[http://octopress.org/docs/setup/](http://octopress.org/docs/setup/)

I also found Chris Bernadski's blog to be an invaluable resource for installing Ruby with rbenv.

[http://cbednarski.com/articles/installing-ruby/](http://cbednarski.com/articles/installing-ruby/)

#Standing up a static site with Nikola & Github

Ok so let's get to it then. Here are the steps I followed to get my site functional with Nikola.

>**Note:** These instructions are for Linux, specifically Ubuntu but they should work for other distros as well. If you're not running Linux, you should definitely consider it (but that's for another day :-)
>
Before proceeding make sure you have Python installed :-)

##Install Virtualenv
Why do we need a virtual environment, you ask. Well, Nikola has a ton of dependencies. What if Nikola needs version 1 of a package while you need version 2 for some other purposes. That is one of the basic reasons why we'd ever need virtualenv.

Go ahead and install virtualenv with the commands below. I've also included a couple of libraries which are dependencies for Nikola. 

	sudo apt-get install python-virtualenv virtualenvwrapper libxml2-dev libxslt-dev
	
Note that we're also installing virtualenvwrapper, a set of extensions that make working with virtual environments a snap. Read more about this [here](http://virtualenvwrapper.readthedocs.org/en/latest/).

Add a working directory (path) for virtualenv by adding the below line to ~/.bashrc. Note that you could change ~/Envs to anything you like.

	sudo gedit ~/.bashrc

Add the below line and save the file

	export WORKON_HOME=~/Envs

Now, go ahead and create a virtual environment for Nikola. You will use this every time you want to update your site so give it a friendly name you can remember.

	mkvirtualenv -p /usr/bin/python Nikola

##Install Nikola and its dependencies

All right, now let's begin by starting a working session with the virtualenv Nikola we just set up. 

	workon Nikola

Notice that your cmd prompt now shows that you're inside the virtualenv Nikola. Go ahead and install Nikola along with all its dependencies like markdown, sphinx and so on.

	pip install nikola pyzmq tornado jinja2 requests sphinx markdown

We're now ready to initialize the new site. Navigate to the parent folder where you'd like to save your site. The site will be created as a folder in this directory. Once you're in the correct location enter:

	nikola init myblog

Nikola 7+ has a great command line interface that should prompt you with questions about your new site like Title, URL, Description etc. You can always fill this up later so you can just keep hitting return if you like.

CD into myblog and notice that your site has now been generated in the form of several folders. The key mentions here are:  

- blog posts go in the Posts folder
- web pages go in the Stories folder
- static content goes in the Files folder
- the actual generated site goes in the Output folder

So, the Output folder essentially is your site in its entirety. Right now of course it will be empty since we haven't built anything yet.

*There's one more thing that's more important than everything else and that's your conf.py file. This is your ultimate destination to customize most things in your site. *

##Configuring your new Nikola site

Believe it or not you're almost ready to write your first post already. But before we begin, open up conf.py and update some important fields.

- Title
- Author
- URL - Leave this at default if you don't have an existing domain name
- Timezone
- Email
- Description
- Language preferences

As I mentioned earlier, Nikola has several themes available that are ready-to-use. You can get a list of available themes by issuing the command `Nikola install_theme -l`

Alternatively visit, [http://themes.getnikola.com/](http://themes.getnikola.com/) to view available themes.

Once you find sometihng you like, issue `nikola install_theme <theme>` to install the theme. Then go into conf.py and change the following line to the name of the theme you just installed.

	# Name of the theme to use.
	THEME = "bootstrap3"

You can also get fancy and look at [bootswatch.com](bootswatch.com) to further customize your bootstrap themes. Check out my post here to learn more.

##Writing your first Blog Post

Nikola has several built-in commands to help with most mundane tasks for your site. For example, to create a new post, just type:

	nikola new_post 

This will prompt you for a title and create a new rst (reStructured Text) file with the name you enter in the Posts folder. It will also create a meta file that holds some key info about your new post such as Title, Date/Time, Tags etc. You could also just manually create both these files.

If you prefer Markdown format for your post instead, simply issue

	nikola new_post -f markdown

Open up the post file in your favorite markdown/rst editor and type your heart's content. In case you're wondering I use [Atom](https://atom.io/) or [Remarkable](http://remarkableapp.net/) for Markdown and [online 
reStructured Text editor](http://rst.ninjs.org/) for rst.

##Building your site

Great, now lets build your site. Issue the following commands:

	nikola build
	nikola serve

The former generates your site and copies it to the Output folder while the latter serves up your site in port 8000 on your laptop so you can review. Go to the following location and voila the site shows itself magically.

	http://localhost:8000

###Nikola in Auto mode
Imagine constantly changing your website and having to issue those two comands one at a time. Sound frustrating? In comes, `nikola auto`. It serves up your website in port 8000 and automatically keep track of things. The moment something changes, it jumps in and refreshes your page so you can work on and preview at the same time. Awesome!

To get this to work, you need to install `livereload`

	pip install livereload

##Deploying to Github
Github pages is a great way to host personal websites/blogs. It’s free, fast, reliable, gives you version control and makes you feel like a geek. In fact, Github these days is the perfect platform for you to showcase your skills.

If you're new to git, I suggest you take a tutorial such as this one.

[http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1)

To test publish your blog in github pages, follow these steps:
 
- Sign up for a free github account 
- Create an empty repository for a user/organization or project page as described [here](https://pages.github.com/)
- Publish the contents of the Output folder (this is your actual blog) to the master (default for user/organization pages) or the gh-pages (for project pages) branch of your repository
- Your new site should kick in in a few minutes and will be available at <username>.github.io 
- You can also setup a custom domain using CNAME easily, justcreate a file called CNAME in your repository with the name of your domain

Of course, this isn't a workflow you should follow going forward. You need an automated (or manual) workflow to do two things:

1. Maintain a full copy of your blog source (the entire blog/site folder) in the source branch of your repository. Tis dows two things:
	- Maintains a full backup of your blog in case you lose your local copy
	- Provides you version control in case you want to rollback to a prior version
2. Commit only the Output folder to the master/gh-pages branch of your repository for user or project pages respectively.

Check out [Damian Avila's article](http://www.damian.oquanta.info/posts/one-line-deployment-of-your-site-to-gh-pages.html) where he provides a way to automate this workflow.

##Blogging with IPython

I truly love IPython notebooks and as I highlighted earlier, Nikola make this super snappy. Follow the steps below and IPy-blog on!

1. Ensure you have IPython 1.0 installed (If you'll be using Python more often than not, give [anaconda](https://store.continuum.io/cshop/anaconda/) a shot, its super cool!)

2. Install a theme that has IPython in it. For example `nikola install_theme ipython`

3. Modify your conf.py to include the following lines under POSTS and PAGES respectively:

		("posts/*.ipynb", "posts", "post.tmpl"),
		("stories/*.ipynb", "stories", "story.tmpl"),

4. You're all set, to write a post in IPython (yes, Nikola automatically converts it for you, no more nbconvert) just do

			nikola new_post -f ipynb

If you will blog all the time with IPython keep the lines in bullet 3 as the first line under POSTS/PAGES, then you can just do `nikola new_post`

There you have it, a brand new, customizable, fully functional site powered by Nikola, IPython and Github. It can't get better than this.

Happy Blogging!
