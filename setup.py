from distutils.core import setup

setup(
    name = "loft",
    version='0.4',
    author = "Ludwik Trammer and Tim Fletcher",
    author_email = "ludwik@gmail.com, fletcher@liftinteractive.com",
    description = "A fork of dimasbka's django-tagging-autocomplete app",
    license = "GNU",
    url = "https://github.com/JordanReiter/django-tagging-autocomplete",
    packages = [
        "tagging_autocomplete"
    ],
    classifiers = [
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)