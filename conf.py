import sphinx_rtd_theme

project = 'TOP Doc '
copyright = '2023, EPFL'
html_logo = '_static/img/Oates_Logo-300x120.png'
html_favicon = '_static/img/favicon.ico'
html_theme = 'sphinx_rtd_theme'

exclude_patterns = [
    'venv',
    '.github',
    'README.md',
    'archive'
]

html_theme = "sphinx_rtd_theme"

html_context = {
    'display_github': True,
    'github_user': 'EPFL-STD',
    'github_repo': 'documentation',
    'github_version': 'main/',
}

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_togglebutton',
    'sphinx_copybutton',
    'sphinx.ext.autosectionlabel'
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    'colon_fence',
    'html_admonition'
]

myst_heading_anchors = 3

html_static_path = [
    '_static'
]

html_css_files = [
    'css/custom-admonitions.css'
]

linkcheck_ignore = [
    # FIXME: The URLs have changed
    r'https://research\.cs\.wisc\.edu/htcondor/.*',
]
