click or press right arrow key...

# Pageshow

**Disclaimer**: i made this tool for my own courses; use at your own risk. there are things that could be made safer / more user friendly, but this works for my purposes so that's how it is

Turn a markdown document into a series of html pages (using [pandoc](https://pandoc.org)) that you can navigate through like a slide show, like the markdown-to-slideshow tools that are out there ([Remarkable](https://github.com/Muffo/remarkable), [Marp](https://marp.app), etc)
- ^ except there's explicitly no slide formatting. no rules about making everything the same sized block. if a "slide" is too big, you just scroll down during the presentation
  - ^ this isn't how normal slideshows work, but that's the point. if you want to make a standard slide show you should use those tools

**Motivation**: markdown is amazing, but trying to format slides using plaintext markdown _SUCKS_; but i like plaintext too much to give it up. the main reason it sucks comes from trying to correctly format everything into a uniformly sized rectangle <-- with this tool you don't have to
- the inspiration for this came from my advisor, who teaches a cognition course using a word doc instead of a slide show. this tool is meant to be a happy medium between slides and documents

I got the sweet latex styling from [David Zollikofer](https://github.com/davidrzs)'s [latex.css](https://github.com/davidrzs/latexcss)

# Dependencies
- [ ] [python](https://www.python.org)
- [ ] [pandoc](https://pandoc.org)


# Usage

0. Download this repo
1. Install pandoc and python (probably have to use a unix based os) if you don't have them
2. edit `make.py` file; change the `doc` variable to the path of the document you want to convert
  - you can also change the heading level you want to split at (1,2,3,... -> #,##,###,...)
3. run the `make.py` file in the terminal with:
```bash
python3 make.py
```
^ or whatever it is you use to call a python script
4. open up the `index.html` file in your browser to view
- use right/left arrow keys or mouse click to navigate

Also, I'm just gunna add some text in this readme so you can hopefully see what happens when the page is too big (you just scroll down during the presentation, rather than stressing over formatting <-- tradeoffs)
- some more text
- even more
- whats this? more text?
- keep it going
- hopefully this will cause you to have to scroll
- if not...
- maybe this will...
- just in case,
- we'll add some more
- if you haven't had to scroll yet, use a smaller screen like the rest of us

## CAREFUL!!
- Don't have a folder called "figures/" in the head directory of this repo. in fact, probably best to avoid messing with this repo at all. 

# RoadMap / TODO
- [ ] turn this into a command lineable function
- [ ] make sure it's accessible to screen readers (i think i have to do something with the iFrame html object)
- [ ] this was a pretty quick and dirty implementation of this idea; in the future it'd be cool if you could make the whole thing a self-contained html file
  - ^ probably wouldn't be too hard; just turn everything into divs with numeric IDs and make the "change_page" function turn on/off divs rather than importing html scripts; would also require a fancier html generator in the `make.py` script
- [x] figure out how to handle figures <-- not the best solution but it works
