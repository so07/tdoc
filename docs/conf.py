from recommonmark.parser import CommonMarkParser
import recommonmark

from recommonmark.transform import AutoStructify

# At the bottom of conf.py
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
project = "tdocs"

master_doc = 'index'

source_parsers = {
    '.md': CommonMarkParser,
}

extensions = ['recommonmark']

#extensions = [
#    'sphinx_markdown_tables',
#]

source_suffix = ['.md', '.rst']

