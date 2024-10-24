from setuptools import setup, find_packages

setup(
    name='Okapi',
    version="0.0.4",  # Bump2version mettra à jour cette valeur
    description='Un outil pour synchroniser les données entre Raspberry Pi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Daniel VALLON',
    author_email='d.vallon@icloud.com',
    url='https://github.com/dvallon906/Okapi',
    packages=find_packages(),
    install_requires=[
        'ntplib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'sync-manager = my_project.sync_manager:main',
        ],
    },
)
