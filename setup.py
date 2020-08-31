from setuptools import setup
setup(
  name = 'dicBySimilarity',
  packages = ['dicBySimilarity'],
  version = '0.04',
  description = 'Python dictionary, but the keys are recognized by text similarity ratio!',
  author = 'Wang Qi',
  author_email = 'wangmarkqi@gmail.com',
  url = 'https://github.com/wangmarkqi/dicBySimilarity',
  download_url = 'https://github.com/wangmarkqi/dicBySimilarity.git',
    install_requires=[ 'Python-Levenshtein>=0.12'],
  keywords = ['fuzzy recognition', 'text similarity'],
  classifiers = []

)

'''
# 上传source 包
python setup.py sdist
twine upload dist/*

'''
