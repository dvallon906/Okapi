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
    install_requires=[
        'ntplib'
    ],  # Utiliser la fonction pour inclure les dépendances
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Version minimale de Python requise
    entry_points={
        'console_scripts': [
            'sync-manager = my_project.sync_manager:main',  # Point d'entrée pour exécuter le script
        ],
    },
)
