# Test for one implementation of the interface
from unittest import TestCase

import pytest
from integration_tests import IntegrationTests
from lexicon.providers.luadns import Provider


# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from define_tests.TheTests


class LuaDNSProviderTests(TestCase, IntegrationTests):

    Provider = Provider
    provider_name = 'luadns'
    domain = 'capsulecd.com'

    def _filter_headers(self):
        return ['Authorization']

    @pytest.mark.skip(reason="CNAME requires FQDN for this provider")
    def test_Provider_when_calling_create_record_for_CNAME_with_valid_name_and_content(self):
        return

    # TODO: the following skipped suite and fixtures should be enabled
    @pytest.mark.skip(reason="new test, missing recording")
    def test_Provider_when_calling_update_record_should_modify_record_name_specified(self):
        return
