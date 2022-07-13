#!/usr/bin/env python

# https://www.lucypark.kr/courses/2015-ba/text-mining.html

import pprint

# 영어
'''
from nltk.corpus import gutenberg   # Docs from project gutenberg.org
files_en = gutenberg.fileids()      # Get file ids
doc_en = gutenberg.open('austen-emma.txt').read()

from nltk import regexp_tokenize
pattern = r'(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\. | [][.,;"\'?():-_`]'
tokens_en = regexp_tokenize(doc_en, pattern)

import nltk
en = nltk.Text(tokens_en)

print(len(en.tokens))       # returns number of tokens (document length)
print(len(set(en.tokens)))  # returns number of unique tokens
en.vocab()                  # returns frequency distribution
en.plot(50)     # Plot sorted frequency of top 50 tokens
en.count('Emma')
en.dispersion_plot(['Emma', 'Frank', 'Jane'])
'''

# 한국어
from konlpy.corpus import kobill    # Docs from pokr.kr/bill
files_ko = kobill.fileids()         # Get file ids
doc_ko = kobill.open('1809890.txt').read()
#print(doc_ko)

from konlpy.tag import Twitter; t = Twitter()
tokens_ko = t.morphs(doc_ko)
#print(tokens_ko)

import nltk
ko = nltk.Text(tokens_ko, name='대한민국 국회 의안 제 1809890호')   # For Python 2, input `name` as u'유니코드'
#print(ko)

print("total ko.tokens:", len(ko.tokens))       # returns number of tokens (document length)
print("unique ko.tokens:", len(set(ko.tokens)))  # returns number of unique tokens
vocab = ko.vocab()                  # returns frequency distribution
print("vocab:", end=" ")
pprint.pprint(vocab)
ko.plot(50)     # Plot sorted frequency of top 50 tokens
ko.count('초등학교')
ko.dispersion_plot(['육아휴직', '초등학교', '공무원'])

from matplotlib import pylab, rc
pylab.show = lambda: pylab.savefig('some_filename.png')
rc('font', family='NanumGothic')
