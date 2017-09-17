# Goal
Get job offers data from a major French IT recruitment site.

_This simple scraper is part of a larger project whose goal is to analyse the skills asked on the IT job maket at any point in time and render this data clearly to developers._

## Capabilities

Data is extracted and cleaned (no DB pipeline set here).

The spider is able to perceive and deal with 2 different job offer patterns.

## Built-on

[Scrapy](https://scrapy.org/), a powerfull python framework for building ETLs.

## Install

Pre-requisites:
- python
- an Internet connection

```
virtualenv scrapyenv

source scrapyenv/bin/activate

pip install -r requirements.txt
```

## Use

To see the generated items on the terminal screen: `scrapy crawl lesjeudis`

To store the file on a json file: `scrapy crawl lesjeudis -o offers.json`
