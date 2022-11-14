from random import randrange
from piskvorky import  evaluation, move_of_computer, format_of_field

def test_empty_field():
    field = move_of_computer('--------------------', 'o')
    assert len(field) == 20
    assert field.count('o') == 1
    assert field.count('-') == 19

def test_turn_of_x():
    field = move_of_computer('-ox--x--oo-x-o-o-x-x', 'o')
    assert len(field) == 20
    assert field.count('o') == field.count('x') + 1

def test_turn_of_o():
    field = move_of_computer('-ox--o---o-x-o-o-x-x', 'x')
    assert len(field) == 20
    assert field.count('o') == field.count('x')

def test_randrange():
    assert randrange(19) <= 20
    assert randrange(19) >= 0
    assert randrange(19) != 21
    assert randrange(19) in range(0,20)

def test_evaluation():
    field_a = 'xxooxxooxxooxxooxxoo'
    field_b = 'xoxoxoxoxoxoxoxoxoxo'
    field_c = 'xoxxxoxoxoxoxoxoxoxo'
    field_d = 'xoxoxoxoxoooxoxoxoxo'
    field_e = '--xo--xo--oo--xx--ox'
    assert evaluation(field_a) == 'no one'
    assert evaluation(field_b) == 'no one'
    assert evaluation(field_c) == '"x"'
    assert evaluation(field_d) == '"o"'
    assert evaluation(field_e) == None

def test_format_of_field():
    field_a_input  ='--x--x--oo-x-o-----x'
    field_a_output = '--x-ox--oo-x-o-----x'
    field_b_input = '--x--o--oo-x-o---x-x'
    field_b_output = '--x--o--oo-x-ox--x-x'
    assert format_of_field(field_a_input, 4, 'o') == field_a_output
    assert format_of_field(field_b_input, 14, 'x') == field_b_output
