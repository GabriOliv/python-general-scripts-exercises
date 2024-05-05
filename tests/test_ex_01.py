import pytest
import ex_01


def test_get_name(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda _: 'John')
	assert ex_01.get_name() == 'John'

	monkeypatch.setattr('builtins.input', lambda _: 'Alice')
	assert ex_01.get_name() == 'Alice'

	monkeypatch.setattr('builtins.input', lambda _: 'Bob')
	assert ex_01.get_name() == 'Bob'


def test_get_age(monkeypatch):
	# Test v
	monkeypatch.setattr('builtins.input', lambda _: '25')
	assert ex_01.get_age() == 25

	monkeypatch.setattr('builtins.input', lambda _: '50')
	assert ex_01.get_age() == 50

	monkeypatch.setattr('builtins.input', lambda _: '100')
	assert ex_01.get_age() == 100

	# Test x-v
	inputs = ['a', '100']
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	assert ex_01.get_age() == 100

	# Test x-x-v
	inputs = ['not a number', '-1', '25']
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	assert ex_01.get_age() == 25

	# Test x-x-x
	inputs = ['a', 'ab', 'abc']
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	with pytest.raises(SystemExit):
		ex_01.get_age()


def test_calculate_year_to_turn_100():
	assert ex_01.calculate_year_to_turn_100(25, 2024) == 2099
	assert ex_01.calculate_year_to_turn_100(50, 2024) == 2074
	assert ex_01.calculate_year_to_turn_100(100, 2024) == 2024
	assert ex_01.calculate_year_to_turn_100(120, 2024) is None


def test_print_message(capsys):
	ex_01.print_message("John", 25, 2099)
	captured = capsys.readouterr()
	assert captured.out == "\n\nName: \t John \nAge: \t 25\n\nYou will get 100 years old in  2099 \n\n\n"

	ex_01.print_message("Alice", 50, 2074)
	captured = capsys.readouterr()
	assert captured.out == "\n\nName: \t Alice \nAge: \t 50\n\nYou will get 100 years old in  2074 \n\n\n"

	ex_01.print_message("Bob", 100, 2024)
	captured = capsys.readouterr()
	assert captured.out == "\n\nName: \t Bob \nAge: \t 100\n\nYou will get 100 years old in  2024 \n\n\n"

	ex_01.print_message("Alice", 120, None)
	captured = capsys.readouterr()
	assert captured.out == "\n\nName: \t Alice \nAge: \t 120\n\nYou already got 100 years old\n\n\n"


def test_get_message(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda _: 'Hello World')
	assert ex_01.get_message() == 'Hello World'

	monkeypatch.setattr('builtins.input', lambda _: 'This is a test')
	assert ex_01.get_message() == 'This is a test'

	monkeypatch.setattr('builtins.input', lambda _: 'Python is awesome')
	assert ex_01.get_message() == 'Python is awesome'


def test_get_repeat_times(monkeypatch):
	# Test v
	monkeypatch.setattr('builtins.input', lambda _: '12')
	assert ex_01.get_repeat_times() == 12

	monkeypatch.setattr('builtins.input', lambda _: '123')
	assert ex_01.get_repeat_times() == 123

	monkeypatch.setattr('builtins.input', lambda _: '1234')
	assert ex_01.get_repeat_times() == 1234

	# Test x-v
	inputs = ['a', '100']
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	assert ex_01.get_repeat_times() == 100

	# Test x-x-v
	inputs = ['not a number', '-1', '25']
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	assert ex_01.get_repeat_times() == 25

	# Test x-x-x
	inputs = ['a', 'ab', 'abc']
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	with pytest.raises(SystemExit):
		ex_01.get_repeat_times()


def test_repeat_message(capsys):
	ex_01.repeat_message("Hello", 3)
	captured = capsys.readouterr()
	assert captured.out == "[  1  ] \t Hello\n[  2  ] \t Hello\n[  3  ] \t Hello\n"

	ex_01.repeat_message("World", 0)
	captured = capsys.readouterr()
	assert captured.out == ""

	ex_01.repeat_message("Code", -1)
	captured = capsys.readouterr()
	assert captured.out == ""

	ex_01.repeat_message("Test", 5)
	captured = capsys.readouterr()
	assert captured.out == "[  1  ] \t Test\n[  2  ] \t Test\n[  3  ] \t Test\n[  4  ] \t Test\n[  5  ] \t Test\n"

	ex_01.repeat_message("Python", 1)
	captured = capsys.readouterr()
	assert captured.out == "[  1  ] \t Python\n"
