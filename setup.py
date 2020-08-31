from setuptools import setup
setup(
  name = 'dicBySimilarity',
  packages = ['dicBySimilarity'],
  version = '0.03',
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
python setup.py sdist build
python setup.py sdist upload
# 上传pre-compiled包
python setup.py bdist_wheel --universal
python setup.py bdist_wheel upload
'''
