#!/usr/bin/env python3
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestVerboseOutput(unittest.TestCase):
    def test_private_info_arg(self):
        outp = subprocess.Popen(
            [
                sys.executable, 'yt_dlp/__main__.py', '-v',
                '--username', 'johnsmith@gmail.com',
                '--password', 'my_secret_password',
            ], cwd=rootDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sout, serr = outp.communicate()
        self.assertTrue(b'--username' in serr)
        self.assertTrue(b'johnsmith' not in serr)
        self.assertTrue(b'--password' in serr)
        self.assertTrue(b'my_secret_password' not in serr)

    def test_private_info_shortarg(self):
        outp = subprocess.Popen(
            [
                sys.executable, 'yt_dlp/__main__.py', '-v',
                '-u', 'johnsmith@gmail.com',
                '-p', 'my_secret_password',
            ], cwd=rootDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sout, serr = outp.communicate()
        self.assertTrue(b'-u' in serr)
        self.assertTrue(b'johnsmith' not in serr)
        self.assertTrue(b'-p' in serr)
        self.assertTrue(b'my_secret_password' not in serr)

    def test_private_info_eq(self):
        outp = subprocess.Popen(
            [
                sys.executable, 'yt_dlp/__main__.py', '-v',
                '--username=johnsmith@gmail.com',
                '--password=my_secret_password',
            ], cwd=rootDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sout, serr = outp.communicate()
        self.assertTrue(b'--username' in serr)
        self.assertTrue(b'johnsmith' not in serr)
        self.assertTrue(b'--password' in serr)
        self.assertTrue(b'my_secret_password' not in serr)

    def test_private_info_shortarg_eq(self):
        outp = subprocess.Popen(
            [
                sys.executable, 'yt_dlp/__main__.py', '-v',
                '-u=johnsmith@gmail.com',
                '-p=my_secret_password',
            ], cwd=rootDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sout, serr = outp.communicate()
        self.assertTrue(b'-u' in serr)
        self.assertTrue(b'johnsmith' not in serr)
        self.assertTrue(b'-p' in serr)
        self.assertTrue(b'my_secret_password' not in serr)


if __name__ == '__main__':
    unittest.main()
