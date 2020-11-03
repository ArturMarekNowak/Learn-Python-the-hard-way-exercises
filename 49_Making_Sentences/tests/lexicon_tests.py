from nose.tools import *
from ex49 import ex49, lexicon

def test_directions(): 
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'), 
                          ('direction', 'south'), 
                          ('direction', 'east')])

def test_verbs(): 
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'), 
                          ('verb', 'kill'), 
                          ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'), 
                          ('stop', 'in'), 
                          ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'), 
                          ('noun', 'princess')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3), 
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', "ASDFADFASDF")])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'), 
                          ('noun', 'princess')])




def test_Sentence():
    first_sentence = ex49.Sentence(('noun', 'princess'), ('verb', 'go'), ('direction', 'north'))

    assert_equal(first_sentence.subject, "princess")
    assert_equal(first_sentence.verb, "go")
    assert_equal(first_sentence.object, "north")

def test_peek():
    assert_equal(ex49.peek([('noun', 'princess')]), 'noun')

def test_match(): 
    assert_equal(ex49.match([('noun', 'princess'), ('verb', 'go'), ('direction', 'north')], 'noun'), ('noun', 'princess'))
    assert_equal(ex49.match([('princess', 'error')], 'noun'), None)

def test_parse_verb():
    assert_equal(ex49.parse_verb([('verb', 'go'), ('stop', 'the'), ('direction', 'north')]), ('verb', 'go'))
    assert_raises(Exception, ex49.parse_verb, ([('noun', 'princess'), ('verb', 'go'), ('stop', 'the'), ('direction', 'north')]))
 
def test_parse_object():
    assert_equal(ex49.parse_object([('stop', 'the'), ('direction', 'north'), ('verb', 'go')]), ('direction', 'north'))
    assert_equal(ex49.parse_object([('stop', 'the'), ('noun', 'bear'), ('verb', 'go')]), ('noun', 'bear')) 
    assert_raises(Exception, ex49.parse_object, ([('verb', 'go'), ('noun', 'princess'), ('verb', 'go'), ('stop', 'the'), ('direction', 'north')]))

def test_parse_subject():
    second_sentence = ex49.parse_subject([('verb', 'go'), ('direction', 'north')], ('noun', 'princess'))
    
    assert_equal(second_sentence.object, 'north')
    assert_equal(second_sentence.subject, 'princess')
    assert_equal(second_sentence.verb, 'go')

def test_parse_sentence():
    s1 = ex49.parse_sentence(lexicon.scan("princess go north"))
    
    assert_equal(s1.object, 'north')
    assert_equal(s1.subject, 'princess')
    assert_equal(s1.verb, 'go')

