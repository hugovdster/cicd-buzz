from buzz import generator

def test_sample_single_word():
    one = ('foo', 'bar', 'foobar')
    word = generator.sample(l)
    assert word in one

def test_sample_multiple_words():
    one = ('foo', 'bar', 'foobar')
    words = generator.sample(l, 2)
    assert len(words) == 2
    assert words[0] in one
    assert words[1] in one
    assert words[0] is not words[1]

def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
