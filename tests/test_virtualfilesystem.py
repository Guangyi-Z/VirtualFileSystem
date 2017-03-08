#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_virtualfilesystem
----------------------------------

Tests for `virtualfilesystem` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from virtualfilesystem.virtualfilesystem import Directory,FileSystem
from virtualfilesystem import cli



class TestVirtualfilesystem(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'virtualfilesystem.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_directory(self):
        d = Directory(None, '/')
        d.add_child('tmp1', 'xxx\nyyy\n')
        d.add_child('dir2', Directory(d, 'dir2'))
        assert len(d.get_child_list()) == 2

    def test_fs(self):
        fs = FileSystem()
        assert fs.cd('') is False

