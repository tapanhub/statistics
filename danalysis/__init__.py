#!/usr/bin/env python
from os.path import dirname, join
import pkgutil
__all__ = list(module for _, module, _ in
               pkgutil.iter_modules([join(dirname(__file__), 'lib')]))
