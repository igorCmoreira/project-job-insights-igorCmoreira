from src.counter import count_ocurrences


def test_counter():
    countP = count_ocurrences("src/jobs.csv", "Python")
    countJ = count_ocurrences("src/jobs.csv", "Javascript")

    assert 1639 == countP
    assert 122 == countJ
