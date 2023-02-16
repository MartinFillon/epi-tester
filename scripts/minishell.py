import subprocess

errorCode = 84
segfaultMessage = b"Segmentation fault\n"
commandNotFound = b"["
noErr = b""
noOut = b""
successCode = 0
testCount = 0


def TEST(command, sucess, errOut, stdOut):
    global testCount
    testCount += 1
    if errOut == b"[":
        errOut = bytes(command, 'utf-8')
        errOut += b": Command not found.\n"
    print("Test " + str(testCount) + ' => echo ' + command)
    cm = subprocess.Popen(['echo', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sh = subprocess.Popen(['./mysh'], stdin=cm.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cm.wait()
    out, err = sh.communicate()
    if not sucess:
        if sh.returncode != errorCode:
            print("Wrong error code")
        if err != errOut:
            print("Wrong error output")
        if err == errOut and sh.returncode == errorCode and not sucess:
            print("Passed")
    if sucess:
        if stdOut == b"":
            res = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            resOut, resErr = res.communicate()
        else:
            resOut = stdOut
        if sh.returncode != successCode:
            print("Wrong error code")
        if resOut != out:
            print("Wrong standard output")
        if out == resOut and sh.returncode == successCode and sucess:
            print("Passed")


def main():
    subprocess.run(['make', 're', '-s'])
    print("minishell1 tester")
    TEST("./seg", False, segfaultMessage, noOut)
    TEST("ls", True, noErr, noOut)
    TEST("exitt", False, commandNotFound, noOut)
    TEST("echo test", True, noErr, b"test\n")
    TEST("env", True, noErr, noOut)
    subprocess.run(['make', 'clean', '-s'])


if __name__ == "__main__":
    main()
