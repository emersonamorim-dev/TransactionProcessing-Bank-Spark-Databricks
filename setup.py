from setuptools import setup, find_packages

setup(
    name='transacoesAPI',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        # outras dependências que sua aplicação pode precisar
    ],
    entry_points={
        'console_scripts': [
            'transacoesAPI=yourmodule:main_function',
        ],
    },
)
