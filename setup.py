from setuptools import setup, find_packages

setup(
    name='dvcli-k8s',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click==7.1.2',
        'pykeepass==3.2.0',
        'Jinja2==2.11.3'
    ],
    entry_points='''
        [dvcli.plugins]
        k8s=k8s.cli:k8s
    ''',
    include_package_data=True,
    package_data={'k8s': ['templates/*.yaml']},
)
