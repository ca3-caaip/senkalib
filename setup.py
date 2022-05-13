# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['senkalib',
 'senkalib.chain',
 'senkalib.chain.bsc',
 'senkalib.chain.kava',
 'senkalib.chain.osmosis']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'bscscan-python>=2.0.0,<3.0.0',
 'pandas>=1.4.2,<2.0.0',
 'web3>=5.29.0,<6.0.0']

setup_kwargs = {
    'name': 'senkalib',
    'version': '0.2.4',
    'description': '',
    'long_description': 'None',
    'author': 'settler',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
