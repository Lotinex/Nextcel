from distutils.core import setup
setup(
  name = 'nextcel',     
  packages = ['nextcel', 'nextcel.lib'], 
  version = '1.1.1',      
  license='MIT',       
  description = 'Library for analyze Excel data',   
  author = 'Lotinex',  
  author_email = 'loard969@gmail.com',
  url = 'https://github.com/Lotinex/Nextcel', 
  download_url = 'https://github.com/Lotinex/Nextcel/archive/refs/tags/v1.1.1.tar.gz',
  keywords = ['Excel', 'analyze', 'python'],
  install_requires=['numpy', 'pandas'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
  ],
)