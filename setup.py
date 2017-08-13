from setuptools import setup, find_packages

entry_points = """
[pygments.lexers]
oftlisplexer = oftlisplexer.lexer:OftlispLexer
"""

setup(name="oftlisplexer", packages=find_packages(), entry_points=entry_points)
