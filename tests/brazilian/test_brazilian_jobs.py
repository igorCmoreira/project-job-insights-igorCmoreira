from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    coverted_jobs = read_brazilian_file('tests/mocks/brazilian_jobs.csv')
    english_keys = {
        "title": "str",
        "salary": "str",
        "type": 'str'
    }

    for job in coverted_jobs:
        assert job.keys() == english_keys.keys()
