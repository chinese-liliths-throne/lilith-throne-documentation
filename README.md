## Lilith's Throne Mod Documentation
### Contributing

This site is build with [Sphinx](https://github.com/sphinx-doc/sphinx) and hosted by [Read the Docs](https://github.com/readthedocs/readthedocs.org). Site content is weitten in [ReStructuredText](https://docutils.sourceforge.io/rst.html) located in docs. For simple edits, you can directly edit the file on GitHub and generate a Pull Request.

For local development, you need a [Python](https://www.python.org/) and pip. And install dependency first.

``` shell
	pip install -r requirements.txt
```

To build the html, just use
``` shell
	# Linux
	make html 
	# Wubdiws
	./make.bat html

	#  Build English
	sphinx-build -M html . _build
	#  Build Chinese
	sphinx-build -b html . _build/html/zh -D language=zh 
```

### Working Tips

 - Vscode extension `reStructuredText` and `reStructuredText Syntax hightlighting`.
 - Use preview or build the html to make sure the changes are valid.