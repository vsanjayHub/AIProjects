from setuptools import setup, find_packages

setup(
    name='YourProjectName',  # Replace 'YourProjectName' with the name of your project
    version='0.1',  # Project version
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'tensorflow',
        'nltk'
    ],  # List of dependencies, same as in requirements.txt
    python_requires='>=3.8',  # Minimum version requirement of Python
    author='Your Name',  # Optional: your name
    author_email='your.email@example.com',  # Optional: your email
    description='A machine learning project analyzing Airbnb data using NLP and deep learning techniques',  # Optional: a short project description
    url='https://github.com/your_username/your_project_name',  # Optional: the URL to the project's repository
    classifiers=[
        'Development Status :: 3 - Alpha',  # Optional: Development status
        'Intended Audience :: Developers',  # Optional: Define the audience
        'License :: OSI Approved :: MIT License',  # Optional: License information
        'Programming Language :: Python :: 3',  # Optional: Supported programming languages
        'Programming Language :: Python :: 3.8',  # Optional: Supported Python versions
        'Topic :: Software Development :: Libraries :: Python Modules',  # Optional: Topic categories
    ],
)

