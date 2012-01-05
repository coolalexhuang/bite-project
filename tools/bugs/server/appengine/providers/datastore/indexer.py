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


"""Datastore indexer object."""

__author__ = 'jason.stredwick@gmail.com (Jason Stredwick)'

from bugs.models.url_bug_map import create
from bugs.providers import indexer_base


class Error(indexer_base.Error):
  pass


class Indexer(indexer_base.IndexerBase):
  """Indexer base class.

  Indexer is responsible creating search indices for bug from a specific
  provider.
  """

  def __init__(self):
    pass

  def Index(self, bug):
    """Creates search indices for the bug specified by the given bug.

    Args:
      bug: The bug. (bugs.models.bug.Bug)
    Returns:
      The id for the newly created UrlBugMap. (integer)
    Raises:
      Error: Raised if there was an error creating an index.
    """
    try:
      return create.Create(bug)
    except create.Error, e:
      raise Error(e)
