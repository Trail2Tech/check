import check50

@check50.check()
def fileExists():
    """ Check if the file even exists """
    check50.exists("rectangle.py")
    check50.include("2w5h.txt", "3w3h.txt")


@check50.check(fileExists)
def test0():
    program_output = check50.run("python3 rectangle.py").stdin(5).stdin(5).stdout()
    expected_output = 25
    if program_output != expected_output:
        help = "W = 5, H = 5, expected 25"
        check50.Mismatch(expected_output, program_output, help=help)


@check50.check(fileExists)
def test1():
    program_output = check50.run("python rectangle.py").stdin(6).stdin(9).stdout()
    expected_output = 54
    if program_output != expected_output:
        help = "W = 6, H = 9, expected 54"
        check50.Mismatch(expected_output, program_output, help=help)