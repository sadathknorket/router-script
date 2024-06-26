from setuptools import setup, find_packages

setup(
    name='ziti_router',
    version='0.5.0',
    author='sadath',
    author_email='sadathsadu2002@gmail.com',
    description='A description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ziti-router = ziti_router.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
       install_requires=[
        'requests',
        'pylint',
        'pylint-exit',
        'pyinstaller',
        'tqdm',
        'psutil',
        'packaging',
        'pyjwt',
        'colorama',
        'jinja2',
        'distro',
        'pyyaml',
        # Add more dependencies as needed
    ]
  
)
