from setuptools import setup, find_packages

setup(
    name='geek-blog',
    version='1.3.4',
    packages=find_packages(),
    license=open('../LICENSE.txt').read(),
    description='Full blog based on django',
    long_description=open('README.txt').read(),
    author='WuXianglong',
    author_email='wuxianglong098@gmail.com',
    maintainer='WuXianglong',
    url='http://www.xianglong.me/',
    download_url='http://github.com/sshwsfc/django-xadmin/archive/master.zip',
    packages=['geekblog'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        'django==1.6.5',
        'pymongo==2.4.1',
        'PIL',
        'PyJWT',
        'django-pipeline',
    ],
    keywords=['django', 'geekblog', 'ueditor'],
)
