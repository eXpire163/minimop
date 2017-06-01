from distutils.core import setup
setup(name='Minimop',
      version='0.1',
      description='Fischertechnik Robot',
      author='Christian Wiedemann',
      author_email='eXpire163@mms2k.de',
      url='http://hellofheaven.org',
      license='GNU General Public License v2.0',
      platforms='Raspberry Pi',
      packages=['minimop',
                'minimop.hardware',
                'minimop.helper',
                'minimop.log',
                'minimop.mocks',
                'minimop.run',
                'minimop.tests'
                ],
      data_files={'fonts': ['fonts/*.'],
                  'images': ['images/*'],
                  'fx': ['fx/*']
                  }
      )
