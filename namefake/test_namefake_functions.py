from namefake_tt import createUrlList, countSameNames, getNames, sortAndOutput


def test_createUrlList_func():
    assert (len(createUrlList(10)) == 10), "Function returns incorrect list size"
    assert (type(createUrlList(10)) == list), "Fucntion returns incorrect type"


def test_getNames_func():
    assert type(getNames(['{"name":"Jack Glum"}', '{"name":"Mark Plum"}',
                          '{"name":"Josh Tlum"}'])) == list, "Fucntion returns incorrect type"
    assert len(getNames(['{"name":"Jack Glum"}', '{"name":"Mark Plum"}',
                         '{"name":"Josh Tlum"}'])) / 2 == 3, "Function returns incorrect number of fullnames collected"


def test_countSameNames_func():
    assert type(countSameNames(['Jack', 'Mark', 'Janny'])) == list, "Fucntion returns incorrect type"
    assert len(countSameNames(
        ['Jack', 'Mark', 'Janny'])) == 3, "Function returns incorrect list size when all names are different"
    assert len(countSameNames(['Jack', 'Mark', 'Jack',
                               'Janny', 'Jack'])) == 3, "Function returns incorrect list size if there are simila names in perameter list"


def test_sortAndOutput_func():
    counted = list(
        ("John" + str(i), str(i)) for i in range(0, 100)
    )

    assert len(sortAndOutput(counted)) == 5, "Fucntion returns incorrect number of results"
