def test_miscellaneous(tracer):
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = [1, 2, 3]

    tracer.init()

    x = f"{a} {b:4} {c!r} {d!r:4}"  # FORMAT_VALUE, BUILD_STRING
    x = a == b == c  # ROT_THREE, _COMPARE_OP
    e[0] += e.pop()  # DUP_TOP_TWO

    tracer.register()

    assert tracer.logger.mutations == [
        {"target": "x", "value": "a b    'c' 'd' ", "sources": {"a", "b", "d", "c"}},
        {"target": "x", "value": False, "sources": {"a", "b"}},
        {"target": "e", "value": [4, 2], "sources": {"e"}},
    ]