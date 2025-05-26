from setuptools import setup, find_packages

setup(
    name='emotion_inference',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'joblib',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'inference=scripts.cli:main'
        ]
    },
    author='Eli Homsi',
    description='A CLI tool to infer emotions from text',
    python_requires='>=3.6',
)
