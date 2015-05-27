#!/usr/bin/python
#
# Copyright 2011 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Paths used by BITE Build."""

__author__ = ('ralphj@google.com (Julie Ralph)'
              'jason.stredwick@gmail.com (Jason Stredwick)')


import os


GENFILES_ROOT = 'genfiles'
OUTPUT_ROOT = 'output'
DEPS_ROOT = 'deps'

# Common roots
BUG_ROOT = os.path.join('tools', 'bugs', 'extension')
RPF_ROOT = os.path.join('tools', 'rpf', 'extension')

# Output paths
EXTENSION_DST = os.path.join(OUTPUT_ROOT, 'extension')
SERVER_DST = os.path.join(OUTPUT_ROOT, 'server')
IMGS_DST = os.path.join(EXTENSION_DST, 'imgs')
OPTIONS_DST = os.path.join(EXTENSION_DST, 'options')
STYLES_DST = os.path.join(EXTENSION_DST, 'styles')

RPF_DST = os.path.join(OUTPUT_ROOT, 'rpf')
RPF_IMGS_DST = os.path.join(RPF_DST, 'imgs')
RPF_OPTIONS_DST = os.path.join(RPF_DST, 'options')
RPF_STYLES_DST = os.path.join(RPF_DST, 'styles')
