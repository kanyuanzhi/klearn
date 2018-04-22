from setuptools import setup, find_packages

setup(
    name='kan-ml',
    version='0.0.1',
    keywords='machine learning',
    description='machine learning tools',
    url='https://github.com/kanyuanzhi/kan-ml',
    author='Yuanzhi Kan',
    author_email='kanyuanzhi@gmail.com',
    packages=find_packages(),
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
