# Test for one implementation of the interface
from unittest import TestCase

import pytest
from integration_tests import IntegrationTests
from lexicon.providers.online import Provider


# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests


class OnlineProviderTests(TestCase, IntegrationTests):

    Provider = Provider
    provider_name = 'online'
    domain = 'capsulecd.com'

    def _filter_headers(self):
        return ['Authorization', 'x-recruitment']

    def _test_fallback_fn(self):
        return lambda x: 'placeholder_' + x if x != 'priority' else ''

    @pytest.mark.skip(reason="manipulating records by id is not supported")
    def test_Provider_when_calling_delete_record_by_identifier_should_remove_record(self):
        return
