from setuptools import setup, find_packages

setup(
    name='klearn',
    version='0.0.3',
    keywords='machine-learning',
    description='toolbox for machine learning',
    url='https://github.com/kanyuanzhi/klearn',
    author='Kan Yuanzhi',
    author_email='kanyuanzhi@gmail.com',
    packages=['kan_ml'],
    include_package_data=True,
    platforms='any',
    install_requires=['numpy', 'matplotlib'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

)
