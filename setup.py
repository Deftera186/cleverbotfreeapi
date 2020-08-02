from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf8') as f:
	long_description = f.read()

with open('requirements.txt') as f:
	requirements = f.read().splitlines()

setup(
	name='cleverbotfreeapi',
	version='1.1.0',
	author='Liav Mordouch',
	author_email='liavmordouch@gmail.com',
	description='Simple unofficial package to interact with the same API that the Cleverbot website uses for free.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/Deftera186/cleverbotfreeapi',
	packages=find_packages(),
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
            ],
	install_requires=requirements
)
