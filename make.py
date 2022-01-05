import subprocess, os
# import re # <-- i though i was smart enough to figure out how to do this with regular expressiongs; i was wrong


## global settings
doc = 'README.md'
style_sheet_link = "style.css"
headSplit = 2 # <-- determines the level you want to split the document at. 1 means only H1 get their own page; 2 means H1 and H2 get their own page; ...

## get rid of the previous pages
for file in os.listdir('pages/'):
    if os.path.isfile(os.path.join('pages/', file)):
        os.remove(os.path.join('pages/', file))




## convert markdown file to a bunch of smaller html files
pagefiles = []
with open(doc, 'r') as file:
    newlines = []

    # Parse Markdown Section (this is a very lazy way to do this)
    _ = 0
    for line in file.readlines():
        if line[0] == "#":
            if len(line.split(' ')[0]) <= headSplit:

                filename = os.path.join('pages', str(_) + '.html')
                with open(filename, 'w') as file:
                    file.write(
                        '<link rel="stylesheet" type="text/css" href="../{}">\n'.format(style_sheet_link)
                    )

                    test = subprocess.Popen(
                        ["pandoc", "-t", "html", "--resource-path", os.path.sep.join(doc.split(os.path.sep)[:-1]), "--extract-media=figures/"], 
                        stdin = subprocess.PIPE, stdout = subprocess.PIPE
                    )

                    htmlDoc = test.communicate(bytes('\n'.join(newlines), 'UTF-8'))[0]
                    file.write(htmlDoc.decode('UTF-8'))

                    pagefiles.append(filename)
                    _ += 1 

                newlines = []

        newlines.append(line)

# v-- im not happy about this part; i could make it cleaner by making the "write" process it's own function (just too lazy atm), but the purpose of this was to make this "memoryless" sort of
filename = os.path.join('pages', str(_) + '.html')
with open(filename, 'w') as file:
    file.write(
        '<link rel="stylesheet" type="text/css" href="../{}">\n'.format(style_sheet_link)
    )

    test = subprocess.Popen(
        ["pandoc", "-t", "html", "--resource-path", os.path.sep.join(doc.split(os.path.sep)[:-1]), "--extract-media=figures/"], 
        stdin = subprocess.PIPE, stdout = subprocess.PIPE
    )

    htmlDoc = test.communicate(bytes('\n'.join(newlines), 'UTF-8'))[0]
    file.write(htmlDoc.decode('UTF-8'))

    pagefiles.append(filename)


## Move figures to pages/figures folder
if os.path.isdir('figures/'):
    for file in os.listdir('figures/'):
        os.rename(os.path.join('figures/',file), os.path.join('pages','figures',file)) # <-- for some reason i cant get --extract-media to save in the right spot so this is a quick and dirty solution. just make sure not to have a folder called "figures"
    os.rmdir('figures/')




## Write the main index file that serves as the slide show navigator (the reason im doing it this way is because i need to know the names of the pages in the `pages/` directory, but i dont think a web browser will ever allow you to look at the contents of a folder (though they let you link to css and js files for some reason), and doing it this way in python does the trick)
with open('index.html', 'w') as newIndexFile:

    newIndexFile.write(
'''<!DOCTYPE html>
<html>
<head>
    <!-- This whole document was generated with the `make.py` script -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>pageshow</title>
</head>
<body>

    <div id='main'>
        <iframe id='mainFrame' title='main page' type='text/html' src='pages/0.html' style='height: 95vh; width: 100%; pointer-events: none; overflow-y: auto;' frameborder="0" seamless></iframe>
    </div>

    <!-- you could probably make this program even simpler by saving the whole html text for each page in the pages list, and save the whole thing as a single html file, eliminated the need for the "pages" folder (it might be annoying if you add images, you'd probably want those saved in the html file too. for now it's fine as is) -->
    <script type="text/javascript">
        var current_page = 0
        var pages = {}

        // change spot in page list
        function change_page(direction) {{
            current_page = Math.min(Math.max(current_page + direction,0), pages.length - 1 ) // <-- the min/max keeps you in the range of possible slides. i feel bad i had to look that up; thanks: https://stackoverflow.com/a/5842770/6794367
            document.getElementById('mainFrame').src = pages[current_page]
        }}
        
        // change page based on arrow keys
        document.onkeydown = function (event) {{
            if (event.keyCode == '37') {{
                change_page(-1)
            }} else if (event.keyCode == '39') {{
                change_page(1)
            }}
        }}

        // change based on click
        document.onclick = function (event) {{
            change_page(1)
        }}
    </script>
</body>
</html>
'''.format(str(pagefiles))
    )



