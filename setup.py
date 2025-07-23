from setuptools import setup, find_packages

setup(
    name="code_fixer",
    version="0.1.0",
    author="Your Name",
    description="🛠 A CLI tool that fixes or explains code using AI (powered by Aider)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add any Python package dependencies here, e.g. 'requests', 'typer', etc.
    ],
    entry_points={
        "console_scripts": [
            "code_fixer = code_fixer.main:main"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
