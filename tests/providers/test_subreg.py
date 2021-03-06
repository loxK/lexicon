# Test for one implementation of the interface

from unittest import TestCase

from integration_tests import IntegrationTests
from lexicon.providers.subreg import Provider


# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests


class SubregProviderTests(TestCase, IntegrationTests):

    Provider = Provider
    provider_name = 'subreg'
    domain = 'oldium.xyz'
