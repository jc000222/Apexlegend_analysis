from distutils.core import setup

setup(
    name="src/apex_analysis_package",
    version="2.0.1",
    description="project 2 for Analytics Programming",
    author="Ruoyu Chen",
    author_email="rchen2@mail.yu.edu",
    license="MIT",
    url="https://github.com/jc000222/Apexlegend_analysis",
    packages=[
        "src.apex_analysis_package",
        "src.img",
        "src",
        "src.apex_analysis_package.XML",
        "src.apex_analysis_package.API",
        "src.apex_analysis_package.Scrape",
        "src.apex_analysis_package.Analysis",
        "src.apex_analysis_package.Selenium",
    ],
    install_requires=[
        "matplotlib>=3.0.2",
        "mplfinance>=0.12.7a4",
        "numpy>=1.15.2",
        "pandas>=0.23.4",
        "pandas-datareader>=0.7.0",
        "seaborn>=0.11.0",
        "statsmodels>=0.11.1",
        "yfinance>=0.2.4",
        "selenium>=4.15.2",
    ],
)
