# Wordpress to Octopress Migrator

A python script to convert Wordpress XML dump to a set of plain text/[markdown](http://daringfireball.net/projects/markdown) files. Intended to be used for migration from Wordpress to [public-static](http://github.com/dreikanter/public-static) website generator, but could also be helpful as general purpose Wordpress content processor.We support Wordpress post-name including Chinese and Japanese .

## 0
最简单的教程
在rexdf.wordpress.2014-01-29.xml所在的目录执行下面三条命令即可

	pip install -e git+git://github.com/rexdf/wp2octopress#egg=wp2oct
	wget --no-check-certificate https://raw.github.com/rexdf/wp2octopress/master/wp2oct/convert-utf-8.txt
	wp2oct rexdf.wordpress.2014-01-29.xml
然后复制post目录里面的到source/_post/目录下面。`rake generate` 可能还有极少少部分报错。具体参考我的[博客](http://i.rexdf.org/blog/2014/01/30/qian-yi-wordpressbo-wen-dao-octopress/)。

## Installation

The script could be installed by command:

	pip install -e git+git://github.com/rexdf/wp2octopress#egg=wp2oct

It will install wp2octopress and the following dependencies:

* [html2text](https://github.com/aaronsw/html2text/)
* [python-markdown](http://pypi.python.org/pypi/Markdown/)


## Usage

[Export](http://en.support.wordpress.com/export/) Wordpress data to XML file (Tools → Export → All content):

![Wordpress content export](http://img-fotki.yandex.ru/get/6403/988666.0/0_a05db_af845b23_L.jpg)

Then wget convert-utf-8.txt for Chinese to pinyin ( It is what octopress does when you type `rake new_post["新博客"]` ) 

	wget --no-check-certificate https://raw.github.com/rexdf/wp2octopress/master/wp2oct/convert-utf-8.txt
**If you donnot need Chinese the ignore it,And type following in where the wordpress.xml is:**

	touch convert-utf-8.txt

Must be as following:

![convert-utf-8.txt](http://photo2.rexdf.org/f/c6/)

And then run the following command:

	wp2octmd -d /export/path/ wordpress-dump.xml

Or simply type:

	wp2octmd wordpress-dump.xml

Where `/export/path/` is the directory where post and page files will be generated, and `wordpress-dump.xml` is the XML file exported by Wordpress.

Use `--help` parameter to see the complete list of command line options:

	usage: wp2octmd [options] source

	Export Wordpress XML dump to markdown files

	positional arguments:
	  source      source XML dump exported from Wordpress

	optional arguments:
	  -h, --help  show this help message and exit
	  -v          verbose logging
	  -l FILE     log to file
	  -d PATH     destination path for generated files
	  -u FMT      <pubDate> date/time parsing format
	  -o FMT      <wp:post_date> and <wp:post_date_gmt> parsing format
	  -f FMT      date/time fields format for exported data
	  -p FMT      date prefix format for generated files
	  -m          preprocess content with Markdown (helpful for MD input)
	  -n LEN      post name (slug) length limit for file naming
	  -r          generate reference links instead of inline
	  -ps PATH    post files path (see docs for variable names)
	  -pg PATH    page files path
	  -dr PATH    draft files path
	  -url        keep absolute URLs in hrefs and image srcs
	  -b URL      base URL to subtract from hrefs (default is the root)


## The output

The script generates a separate file for each post, page and draft, and groups it by configurable directory structure. By default posts are grouped by year-named directories and pages are just stored to the output folder.

![Exported files](http://photo.rexdf.org/linkuse/output.png)

But you could specify different directory structure and file naming pattern using `-ps`, `-pg` and `-dr` parameters for posts, pages and drafts respectively. For example `-ps {year}/{month}/{day}/{title}.md` will produce date-based subfolders for blog posts.

Each exported file has a straightforward structure intended for further processing with [public-static](http://github.com/dreikanter/public-static) website generator. It has an INI-like formatted header followed by markdown-formatted post (or page) contents:

	---
	layout: post
	title: "重装系统如何删除cygwin文件夹"
	date: 2014-01-19 22:02
	comments: true
	categories: 
	---
	
	# 重装系统如何删除cygwin文件夹
	...

If the post contains comments, they will be included below.

![](http://i.rexdf.org/images/wp2oct_cmd.png)

Japanese supported
![](http://i.rexdf.org/images/wp2oct.png)
## See also

* How to [export Wordpress data](http://codex.wordpress.org/Tools_Export_Screen)
* How to [export Wordpress.com data](http://en.support.wordpress.com/export/)
* Refer [https://github.com/dreikanter/wp2md](https://github.com/dreikanter/wp2md "wp2md")


## Copyright and licensing

Copyright &copy; 2013 by [Rexdf](http://blog.rexdf.org).  
License: GNU (see [LICENSE](https://github.com/rexdf/wp2octopress/master/LICENSE)).

Project home: [https://github.com/rexdf/wp2octopress](https://github.com/rexdf/wp2octopress).
