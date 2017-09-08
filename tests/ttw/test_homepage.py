from __future__ import absolute_import, division, print_function, unicode_literals

from gratipay.testing import BrowserHarness


class Tests(BrowserHarness):

    def test_loads_for_anon(self):
        assert self.css('#banner h1').html == 'Pay for open source.'
        assert self.css('#header .sign-in button').html.strip()[:17] == 'Sign in / Sign up'

    def test_redirects_for_authed_exclamation_point(self):
        self.make_participant('alice', claimed_time='now')
        self.sign_in('alice')
        self.reload()
        assert self.css('#banner h1').html == 'Browse'
        assert self.css('.you-are a').html.strip()[:6] == '~alice'
