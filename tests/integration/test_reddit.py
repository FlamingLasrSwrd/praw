"""Test praw.reddit."""
import mock

from praw.models import LiveThread

from . import IntegrationTest


class TestReddit(IntegrationTest):
    @mock.patch('time.sleep', return_value=None)
    def test_live_create(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette('TestReddit.test_live_create'):
            live = self.reddit.live.create('PRAW Create Test')
            assert isinstance(live, LiveThread)
            assert live.title == 'PRAW Create Test'

    def test_random_subreddit(self):
        names = set()
        with self.recorder.use_cassette(
                'TestReddit.test_random_subreddit'):
            for i in range(3):
                names.add(self.reddit.random_subreddit().display_name)
        assert len(names) == 3

    def test_subreddit_with_randnsfw(self):
        with self.recorder.use_cassette(
                'TestReddit.test_subreddit_with_randnsfw'):
            subreddit = self.reddit.subreddit('randnsfw')
            assert subreddit.display_name != 'randnsfw'
            assert subreddit.over18

    def test_subreddit_with_random(self):
        with self.recorder.use_cassette(
                'TestReddit.test_subreddit_with_random'):
            assert self.reddit.subreddit('random').display_name != 'random'


class TestDomainListing(IntegrationTest):
    def test_controversial(self):
        with self.recorder.use_cassette(
                'TestDomainListing.test_controversial'):
            submissions = list(self.reddit.domain('youtube.com')
                               .controversial())
        assert len(submissions) == 100

    def test_hot(self):
        with self.recorder.use_cassette('TestDomainListing.test_hot'):
            submissions = list(self.reddit.domain('youtube.com').hot())
        assert len(submissions) == 100

    def test_new(self):
        with self.recorder.use_cassette('TestDomainListing.test_new'):
            submissions = list(self.reddit.domain('youtube.com').new())
        assert len(submissions) == 100

    def test_random_rising(self):
        with self.recorder.use_cassette(
                'TestDomainListing.test_random_rising'):
            submissions = list(self.reddit.domain('youtube.com')
                               .random_rising())
        assert len(submissions) == 100

    def test_rising(self):
        with self.recorder.use_cassette('TestDomainListing.test_rising'):
            list(self.reddit.domain('youtube.com').rising())

    def test_top(self):
        with self.recorder.use_cassette('TestDomainListing.test_top'):
            submissions = list(self.reddit.domain('youtube.com').top())
        assert len(submissions) == 100
