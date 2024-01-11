from setuptools import setup, find_packages

setup(
    name='dvcli-k8s',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'click==8.0.1',
        'pykeepass==4.0.1',
        'Jinja2==3.1.3'
    ],
    entry_points='''
        [dvcli.plugins]
        k8s=k8s.cli:k8s
    ''',
    include_package_data=True,
    package_data={'k8s': ['templates/*.yaml']},
)
