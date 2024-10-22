from setuptools import setup, find_packages


# Lire requirements.txt
def read_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]


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
    url='https://github.com/dvallon906/Okapi',  # URL du projet (GitHub, etc.)
    packages=find_packages(),  # Trouver et inclure tous les paquets Python du répertoire
    install_requires=read_requirements(),  # Utiliser la fonction pour inclure les dépendances
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Version minimale de Python requise
)
