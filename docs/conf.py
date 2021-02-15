from recommonmark.parser import CommonMarkParser

project = "tdocs"

master_doc = 'index'

source_parsers = {
    '.md': CommonMarkParser,
}

#extensions = [
#    'sphinx_markdown_tables',
#]

source_suffix = ['.md']#, '.rst']

