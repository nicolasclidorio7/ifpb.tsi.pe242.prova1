import mock
import builtins
import main


def test_q01(capfd):
    input_outputexpected = {
        '2':'Par\n',
    }
    for _input, _outputexpected in input_outputexpected.items():
        with mock.patch.object(builtins, 'input', lambda _: _input):
            main.q1()
            output, _ = capfd.readouterr()
            assert output == _outputexpected

def test_q02(capfd):
    input_outputexpected = {
        '2':'Par\n',
    }
    for _input, _outputexpected in input_outputexpected.items():
        with mock.patch.object(builtins, 'input', lambda _: _input):
            main.q2()
            output, _ = capfd.readouterr()
            assert output == _outputexpected

def test_q03(capfd):
    input_outputexpected = {
        '2':'Par\n',
    }
    for _input, _outputexpected in input_outputexpected.items():
        with mock.patch.object(builtins, 'input', lambda _: _input):
            main.q2()
            output, _ = capfd.readouterr()
            assert output == _outputexpected

def test_q04(capfd):
    input_outputexpected = {
        '2':'Par\n',
    }
    for _input, _outputexpected in input_outputexpected.items():
        with mock.patch.object(builtins, 'input', lambda _: _input):
            main.q4()
            output, _ = capfd.readouterr()
            assert output == _outputexpected