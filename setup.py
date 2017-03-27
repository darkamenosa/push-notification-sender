from setuptools import setup

config = {
	'name': 'pushnoti',
	'version': '0.1.0',
	'packages': ['pushnoti'],
	'author': 'darkamenosa',
	'author_email': 'hxtxmu@gmail.com',
	'url': '',
	'description': 'My first python program, a website to test push notification [APNS, GCM]',
	'classifiers': [
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'License :: OSI Approved :: MIT License',
		'Environment :: Web Environment',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX :: Linux',
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Utilities'
	],
    'include_package_data': True,
    'install_requires':[
        'flask',
    ],
    'setup_requires':[
        'pytest-runner',
    ],
    'tests_require':[
        'pytest',
    ],
}

setup(**config)
