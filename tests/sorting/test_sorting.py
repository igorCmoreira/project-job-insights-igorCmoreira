from src.sorting import sort_by

mock = [
    {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-12-25"},
    {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-12-22"},
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-12-23"},
    {"min_salary": 4000, "max_salary": 5000, "date_posted": "2021-12-24"},
]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock[0]['min_salary'] == 1000
    assert mock[0]['max_salary'] == 2000
    assert mock[0]['date_posted'] == "2021-12-25"

    sort_by(mock, "max_salary")
    assert mock[0]['min_salary'] == 4000
    assert mock[0]['max_salary'] == 5000
    assert mock[0]['date_posted'] == "2021-12-24"

    sort_by(mock, "date_posted")
    assert mock[0]['min_salary'] == 1000
    assert mock[0]['max_salary'] == 2000
    assert mock[0]['date_posted'] == "2021-12-25"
