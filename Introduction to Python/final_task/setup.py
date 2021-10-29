from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


setup(
    name="rss_reader",
    version="1.2",
    packages=find_packages(),
    include_package_date=True,
    install_requires=[],
    entry_points="""
        [console_scripts]
        rss_reader=rss_reader:main
    """
)