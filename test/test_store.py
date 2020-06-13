# The MIT License (MIT)
# Copyright (c) 2020 by the xcube development team and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest

from xcube.core.store.accessor import find_data_opener_extensions
from xcube.core.store.accessor import new_data_opener
from xcube.core.store.store import find_data_store_extensions
from xcube.core.store.store import new_data_store
from xcube_sh.constants import SH_DATA_OPENER_ID
from xcube_sh.constants import SH_DATA_STORE_ID
from xcube_sh.store import SentinelHubDataStore
from xcube_sh.store import SentinelHubDataOpener
from .test_sentinelhub import HAS_SH_CREDENTIALS
from .test_sentinelhub import REQUIRE_SH_CREDENTIALS


class SentinelHubDataAccessorTest(unittest.TestCase):
    def test_find_data_store_extensions(self):
        extensions = find_data_store_extensions()
        actual_ext = set(ext.name for ext in extensions)
        self.assertIn(SH_DATA_STORE_ID, actual_ext)

    def test_find_data_opener_extensions(self):
        extensions = find_data_opener_extensions()
        actual_ext = set(ext.name for ext in extensions)
        self.assertIn(SH_DATA_OPENER_ID, actual_ext)

    @unittest.skipUnless(HAS_SH_CREDENTIALS, REQUIRE_SH_CREDENTIALS)
    def test_new_data_store(self):
        store = new_data_store(SH_DATA_STORE_ID)
        self.assertIsInstance(store, SentinelHubDataStore)

    def test_new_data_opener(self):
        store = new_data_opener(SH_DATA_OPENER_ID)
        self.assertIsInstance(store, SentinelHubDataOpener)
