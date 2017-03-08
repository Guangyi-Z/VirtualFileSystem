# -*- coding: utf-8 -*-
import os

class Directory(object):

    def __init__(self, parent, name):
        self._parent = parent
        if parent:
            self._cur = os.path.join(parent.get_name(), name)
        else:
            self._cur = name
        self._childs = dict()

    def get_name(self):
        return self._cur

    def add_child(self, name, content):
        if name in self._childs:
            return False

        self._childs[name] = content
        return True

    def get_child(self, name):
        return self._childs.get(name, None)

    def get_child_list(self):
        return self._childs.keys()

    def get_parent(self):
        return self._parent

    def rm_child(self, name):
        if name not in self._childs:
            return False

        del self._childs[name]
        return True

    def search(self, paths):
        ret = self
        for p in paths:
            if p == '.':
                pass
            elif p == '..':
                if ret.get_parent():
                    ret = ret.get_parent()
                else:
                    return None
            else:
                if ret.get_child(p):
                    ret = ret.get_child(p)
                else:
                    return None

        return ret


class FileSystem(object):

    def __init__(self):
        self._root = Directory(None, '/')
        self._cur = self._root

    def mkdir(self, name):
        return self._cur.add_child(name, Directory(self._cur, name))

    def ls(self):
        return self._cur.get_child_list()

    def touch(self, name):
        return self._cur.add_child(name, None)

    def rm(self, name):
        return self._cur.rm_child(name)

    def cd(self, name):
        cur = None
        if name.startswith('/'):
            cur = self._root.search(name[1:].split('/'))
        else:
            cur = self._cur.search(name.rstrip('/').split('/'))

        if cur:
            self._cur = cur
            return True
        else:
            return False
