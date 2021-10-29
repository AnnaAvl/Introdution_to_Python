from setuptools import setup, find_packages

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
