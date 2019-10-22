try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'autor': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'My email.',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': 'projectname'
}

setup(**config)
