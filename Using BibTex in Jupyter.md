---
jupyter:
  jupytext:
    formats: ipynb,py:light,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Using BibTex in Jupyter


Following [How to add automatically extension to Jupyter (ipython) notebook?](https://stackoverflow.com/questions/32046241/how-to-add-automatically-extension-to-jupyter-ipython-notebook)
we make Calico Document Tools for using BibTex available as follows.

```python
#!jupyter nbextension install https://bitbucket.org/ipre/calico/downloads/calico-document-tools-1.0.zip
```

instead of `sudo ipython install-nbextension` and

```python
!jupyter nbextension enable calico-document-tools
```

instead of `IPython.load_extensions('calico-document-tools');`.

```python

```
