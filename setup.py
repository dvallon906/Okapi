from distutils.core import setup

setup(
    name='Okapi',
    version='1.0.1',
    packages=[''],
    url='',
    license='',
    author='Daniel VALLON',
    author_email='d.vallon@icloud.com',
    description=''
)


from setuptools import setup, find_packages

setup(
    name='Okapi',  # Nom de votre projet
    version='0.1.1',    # Version du projet
    description='Un outil pour synchroniser les données entre Raspberry Pi',  # Brève description
    long_description=open('README.md').read(),  # Description détaillée (le contenu de README.md)
    long_description_content_type='text/markdown',
    author='Daniel VALLON',  # Auteur du projet
    author_email='d.vallon@icloud.com',  # E-mail de l'auteur
    url='https://github.com/votre-utilisateur/my_project',  # URL du projet (GitHub, etc.)
    packages=find_packages(),  # Trouver et inclure tous les paquets Python du répertoire
    install_requires=[
        'requests',  # Liste des dépendances
        'flask',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Version minimale de Python requise
)
