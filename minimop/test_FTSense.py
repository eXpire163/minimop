from ftSense import FTSense


class TestMoterManager(object):

    def test_init(self):
        """If you would MoterManager() stop motor when you build it your test looks like follow code"""
        sense = FTSense()
        dist = sense.get_distance()
        print dist
        assert dist >= -20

