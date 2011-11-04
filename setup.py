from distutils.core import setup

setup(
    name = "loft",
    version='0.4',
    author = "Ludwik Trammer and Tim Fletcher",
    author_email = "ludwik@gmail.com, fletcher@liftinteractive.com",
    description = "A fork of dimasbka's django-tagging-autocomplete app",
    license = "GNU",
    url = "http://github.com/l1f7/django-tagging-autocomplete",
    packages = [
        "django-tagging-autocomplete"
    ],
    classifiers = [
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)