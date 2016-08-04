from __future__ import absolute_import, division, print_function, unicode_literals

from gratipay.testing import BrowserHarness


class Tests(BrowserHarness):

    def test_homepage_renders_copy_correctly_for_anon(self):
        assert self.css('#content h1').html == 'Teams'
        assert self.css('#header .sign-in button').html.strip()[:7] == 'Sign in'

    def test_homepage_renders_copy_correctly_for_authed(self):
        self.make_participant('alice', claimed_time='now')
        self.sign_in('alice')
        self.reload()
        assert self.css('#content h1').html == 'Teams'
        assert self.css('.you-are a').html.strip()[:6] == '~alice'

    def test_homepage_pops_the_welcome_modal(self):
        assert self.has_text('Welcome to Gratipay!')
