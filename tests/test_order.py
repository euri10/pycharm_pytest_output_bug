import logging

def generate_logs():
    for i in range(1000000):
        logger.info(i)


logger = logging.getLogger(__name__)
def test1():
    generate_logs()
    assert True


def test2():
    assert True

