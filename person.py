#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PERSON CLASS"""

class Person():
    """Person class"""

    def __init__(self, name, last_name, age):
        """Inits information about person"""
        self.name = name
        self.last_name = last_name
        self.age = age

    def hello_world(self):
        """Hello world"""

        return "hello world, av" + self.name

    def info(self):
        """Print general info about person, as greeting"""
        return "Hej, mitt namn är {} {} och jag är {} år." \
                .format(self.name, self.last_name, self.age)
