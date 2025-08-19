from setuptools import setup, find_packages

setup(
    name="trustra",
    version="1.0.0",
    description="Trust-first AutoML: Automated ML with built-in fairness, drift, and reliability.",
    author="Devansh Singh",
    author_email="devansh.jay.singh@gmail.com",
    url="https://github.com/Devansh-567/Trustra---Trust-First-AutoML-Framework",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5",
        "numpy>=1.21",
        "scikit-learn>=1.3",
        "optuna>=3.0",
        "plotly>=5.10",
        "jinja2>=3.1",
        "streamlit>=1.24",
        "fairlearn>=0.10",
        "xgboost>=1.7"
        # Remove exact versions unless necessary
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "trustra-dashboard = trustra.dashboard:main"
        ]
    }
)
