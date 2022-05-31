from setuptools import setup

setup(
    name = 'pyrootplots',
    author = 'Bastien Voirin',
    author_email = 'bastien.voirin@ens-lyon.org',
    url = 'https://github.com/bastienvoirin/pyrootplots',
    packages = ['pyrootplots'],
    package_dir = {'pyrootplots': 'src/pyrootplots'},
    install_requires = [
        'numpy',
        'pandas',
        'matplotlib',
        'sphinx',
        'sphinx_rtd_theme',
        'sphinx_toolbox'
    ],
    scripts = ['src/pyrootplots/__main__.py']
)
