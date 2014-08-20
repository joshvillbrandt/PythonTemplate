from setuptools import setup

setup(
    name='PythonTemplate',
    version='0.1.0',
    description='An example Python project.',
    url='https://github.com/joshvillbrandt/PythonTemplate',
    author='Josh Villbrandt',
    author_email='josh@javconcepts.com',
    license='Apache',
    setup_requires=['tox'],
    install_requires=[],
    packages=['PythonTemplate'],
    scripts=['scripts/pytemplate'],
    test_suite='tests',
    zip_safe=False
)
