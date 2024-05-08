import pytest
import ex_01

@pytest.mark.parametrize("name", ["John", "Alice", "Bob"])
def test_get_name(monkeypatch, name):
	monkeypatch.setattr('builtins.input', lambda _: name)
	assert ex_01.get_name() == name

@pytest.mark.parametrize("age", [25, 50, 100])
def test_get_age_first_pass(monkeypatch, age):
	# Test v
	monkeypatch.setattr('builtins.input', lambda _: age)
	assert ex_01.get_age() == age

@pytest.mark.parametrize("age,expected", [
	(['a', '100'], 100),
	(['-1', '25'], 25)
])
def test_get_age_second_pass(monkeypatch, age, expected):
	# Test x-v
	inputs = age
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	assert ex_01.get_age() == expected

@pytest.mark.parametrize("age,expected", [
	(['a', 'ab', '25'], 25),
	(['a', '-1', '50'], 50),
	(['-30', 'a', '100'], 100),
	(['-1', '-40', '150'], 150)
])
def test_get_age_third_pass(monkeypatch, age, expected):
	# Test x-x-v
	inputs = age
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	assert ex_01.get_age() == expected

@pytest.mark.parametrize("age", [
	('a', 'ab', 'abc'),
	('a', '-1', 'ab'),
	('-10', 'a', 'ab'),
	('-30', '-20', 'abc'),
	('-10', '-20', '-30')
])
def test_get_age_fail(monkeypatch, age):
	# Test x-x-x
	inputs = age
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	with pytest.raises(SystemExit):
		ex_01.get_age()

@pytest.mark.parametrize("age,year,expected", [
	(25, 2024, 2099),
	(50, 2024, 2074),
	(100, 2024, 2024),
	(120, 2024, None)
])
def test_calculate_year_to_turn_100(age, year, expected):
	assert ex_01.calculate_year_to_turn_100(age, year) == expected

@pytest.mark.parametrize("name, age, year, expected_output", [
	("John", 25, 2099, "\n\nName: \t John \nAge: \t 25\n\nYou will get 100 years old in  2099 \n\n\n"),
	("Alice", 50, 2074, "\n\nName: \t Alice \nAge: \t 50\n\nYou will get 100 years old in  2074 \n\n\n"),
	("Bob", 100, 2024, "\n\nName: \t Bob \nAge: \t 100\n\nYou will get 100 years old in  2024 \n\n\n"),
	("Alice", 120, None, "\n\nName: \t Alice \nAge: \t 120\n\nYou already got 100 years old\n\n\n")
])
def test_print_message(capsys, name, age, year, expected_output):
	ex_01.print_message(name, age, year)
	captured = capsys.readouterr()
	assert captured.out == expected_output

@pytest.mark.parametrize("message", [
	'Hello World',
	'This is a test',
	'Python is awesome'
])
def test_get_message(monkeypatch, message):
	monkeypatch.setattr('builtins.input', lambda _: message)
	assert ex_01.get_message() == message

@pytest.mark.parametrize("number", [25, 50, 100])
def test_get_repeat_times_first_pass(monkeypatch, number):
	# Test v
	monkeypatch.setattr('builtins.input', lambda _: number)
	assert ex_01.get_repeat_times() == number

@pytest.mark.parametrize("number,expected", [
	(['a', '100'], 100),
	(['-1', '25'], 25)
])
def test_get_repeat_times_second_pass(monkeypatch, number, expected):
	# Test x-v
	inputs = number
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	assert ex_01.get_repeat_times() == expected

@pytest.mark.parametrize("number,expected", [
	(['a', 'ab', '25'], 25),
	(['a', '-1', '50'], 50),
	(['-30', 'a', '100'], 100),
	(['-1', '-40', '150'], 150)
])
def test_get_repeat_times_third_pass(monkeypatch, number, expected):
	# Test x-x-v
	inputs = number
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	assert ex_01.get_repeat_times() == expected

@pytest.mark.parametrize("number", [
	('a', 'ab', 'abc'),
	('a', '-1', 'ab'),
	('-10', 'a', 'ab'),
	('-30', '-20', 'abc'),
	('-10', '-20', '-30')
])
def test_get_repeat_times_fail(monkeypatch, number):
	# Test x-x-x
	inputs = number
	input_generator = (i for i in inputs)
	monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
	with pytest.raises(SystemExit):
		ex_01.get_repeat_times()

@pytest.mark.parametrize("message, times, expected_output", [
	("Hello", 3, "[  1  ] \t Hello\n[  2  ] \t Hello\n[  3  ] \t Hello\n"),
	("World", 0, ""),
	("Code", -1, ""),
	("Test", 5, "[  1  ] \t Test\n[  2  ] \t Test\n[  3  ] \t Test\n[  4  ] \t Test\n[  5  ] \t Test\n"),
	("Python", 1, "[  1  ] \t Python\n")
])
def test_repeat_message(capsys, message, times, expected_output):
	ex_01.repeat_message(message, times)
	captured = capsys.readouterr()
	assert captured.out == expected_output
