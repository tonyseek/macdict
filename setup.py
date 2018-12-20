from setuptools import setup, find_packages


with open('README.rst') as readme:
    next(readme)
    long_description = ''.join(readme).strip()


setup(
    name='macdict',
    version='0.1.4',
    description='CLI and library to look up dictionary in macOS.',
    long_description=long_description,
    keywords=['Dictionary.app'],
    url='https://github.com/tonyseek/macdict',
    author='Jiangge Zhang',
    author_email='tonyseek@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    platforms=['darwin'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: MacOS X',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Education',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'macdict-lookup = macdict.cli:main',
        ],
    },
)
