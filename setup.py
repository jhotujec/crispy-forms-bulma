from setuptools import find_packages, setup
import os

setup(
    name="django-crispy-bulma",
    version="0.3",
    description="Django application to add 'django-crispy-forms' layout objects for Bulma.io",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Python Discord",
    author_email="staff@pythondiscord.com",
    url="https://github.com/python-discord/django-crispy-bulma",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    extras_require={
        "dev": open(
            os.path.join(os.path.dirname(__file__), "dev_requirements.txt")
        ).read(),
    },
    include_package_data=True,
    zip_safe=False,
)
