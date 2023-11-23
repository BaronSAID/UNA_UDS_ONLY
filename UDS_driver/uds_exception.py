# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 20.01.2022
class Error(Exception):
    """Base class for other exceptions"""
    pass


class oracle_lib_1072(Error):
    def __init__(self, exc):
        raise ValueError('Oracle Client library has already been initialized')
