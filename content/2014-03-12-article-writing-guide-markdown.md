Title: Article writing guide in markdown
Category: guide
Tags: pelican, markdown, guide

[TOC]

# Template

```md

Title:
Category:
Tags:

[TOC]

# Heading 1

```python
def foo(): pass

\``` (remove leading backticks)

## Heading 1.1

## Heading 1.1.1


```

# Pelican

- [Pelican getting started](http://docs.getpelican.com/en/latest/getting_started.html)

## Syntax

- Use `Status: hidden` to hide the article / page
- Use `Status: draft` to create draft article / page (under `/drafts`)
- Use `[link]({filename}/cat/article2.rst)` to link to content root
- Use `[link]({filename}cat/article2.rst)` to link to current root
- Use `{tag}tagname` and `{category}catname` to link to tags and categories

# Markdown

- [Pandoc Markdown and ReST Compared](http://www.unexpected-vortices.com/doc-notes/markdown-and-rest-compared.html)
- [GitHub Flavored Markdown · GitHub Help](https://help.github.com/articles/github-flavored-markdown)
- [GitLab Flavored Markdown](https://github.com/gitlabhq/gitlabhq/blob/master/doc/markdown/markdown.md)

## Online tools

- [Markable.in](http://markable.in/editor/)
- [Dillinger](http://dillinger.io/)
- [online markdown viewer](http://www.markdownviewer.com/)







---

# Sample

## Format

*italic*, **bold**, `code`, ~~strikeout text~~

## Ordered list

1. numbered list 1
1. numbered list 2
    1. sub item 1
    1. sub item 2

## Unordered list

* unordered 1

    second paragraph (4 spaces)

* unordered 2
    * unordered 2.1
    * unordered 2.2

## Definition

foo
  : a foo-like object


## Blockquote

> I said *this*.
> He said *taht*.


## Links and images

A link to [Python](http://www.python.com). A link to [Python].

http://www.python.com

<http://www.python.com>

[Python]: http://www.python.com

Another link method to [Python][1]

[1]: http://www.python.com

Leave reference link empty [link to python][]

[link to python]: http://www.python.com

Alan Turing's 100th birthday

![alan](http://2.bp.blogspot.com/-PQv5GPMlNBA/T-T5RtCVJlI/AAAAAAAAAWQ/NqFyh4TUkS8/s1600/turing-timeline.png)


## Misc

Triple * or - for horizontal line.

***

---

One minor footnote [^1] to be aware of.

[^1]: footnote text goes here.


## Blocks

    block of code (use for spaces indentation)
    goes like this


```
block of code **triple-backtick**
goes like this
```

~~~
block of code **triple-tide**
goes like this
~~~


## Tables

Size  Color   Fragrance
----  ------  ----------------
9     Red     Excelsior
10    Blue    Icey Cool


-------------------------------------------
Orientation  Reasoning
-----------  ------------------------------
leftward     Because it works well under
             extreme depths and pressures.

spinward     There's no reason to use
             spinward. It will only
             cause apoplexia.
-------------------------------------------


| Name | Description          |
| ------------- | ----------- |
| Help      | ~~Display the~~ help window.|
| Close     | _Closes_ a window     |

