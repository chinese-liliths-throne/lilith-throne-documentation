## 莉莉丝的王座Mod文档
### 贡献

该网站使用[Sphinx](https://github.com/sphinx-doc/sphinx)构建，并且依赖[Read the Docs](https://github.com/readthedocs/readthedocs.org)托管。网站内容由[ReStructuredText](https://docutils.sourceforge.io/rst.html)编写，位于`docs`文件夹中。对于简单的编辑，你可以直接在Github上编辑文件并生成拉取请求(Pull Request)。

若要进行本地开发，需要安装[Python](https://www.python.org/)及`pip`，并且安装相关依赖。

``` shell
	pip install -r requirements.txt
```

若要构建html网页，只需
``` shell
	# Linux
	make html 
	# Wubdiws
	./make.bat html

	#  英语
	sphinx-build -M html . _build
	#  中文(需要在对应分支branch)
	sphinx-build -b html . _build/html/zh -D language=zh 
```

### 提示

 - Vscode扩展`reStructuredText`和`reStructuredText Syntax hightlighting`。
 - 使用预览或者构建网页，保证修改有效且没有错误。