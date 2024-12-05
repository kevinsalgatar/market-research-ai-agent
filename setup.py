from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="market-research-ai-agent",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI agent system for market research using CrewAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinsalgatar/market-research-ai-agent",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
    install_requires=[
        "crewai>=0.11.0",
        "python-dotenv>=1.0.0",
        "langchain>=0.0.350",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.2",
        "pandas>=2.1.3",
        "numpy>=1.24.3",
        "openai>=1.3.5",
        "duckduckgo-search>=3.9.9",
        "google-search-results>=2.4.2",
        "playwright>=1.40.0",
        "click>=8.0.0",
        "jinja2>=3.0.0",
        "markdown2>=2.4.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0"
    ],
    entry_points={
        'console_scripts': [
            'market-research=cli:cli',
            'run-scenario=run_scenario:run_scenario',
        ],
    },
    include_package_data=True,
    package_data={
        "": ["examples/templates/*.md", "examples/scenarios/*.json"],
    },
)