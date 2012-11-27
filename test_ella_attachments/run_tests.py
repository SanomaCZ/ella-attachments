#!/usr/bin/env python
import sys
from os.path import abspath, dirname

import nose

def run_all():
    argv = ['nosetests',
            '--nocapture', '--nologcapture',
            '--with-coverage', '--cover-package=ella_attachments', '--cover-erase',
            '--with-xunit', ]

    nose.run_exit(
        argv=argv,
        defaultTest=abspath(dirname(__file__)),
    )

if __name__ == '__main__':
    run_all()
