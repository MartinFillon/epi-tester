import subprocess

errorCode = 84
segfaultMessage = b"[Segmentation fault]\n\x00"
commandNotFound = b"["
noErr = b""
successCode = 0
testCount = 0


def TEST(command, sucess, errOut, stdOut):
    global testCount
    testCount += 1
    if errOut == b"[":
        errOut += bytes(command, 'utf-8')
        errOut += b": Command not found.]\n\x00"
    print("Test " + str(testCount) + ' => echo ' + command)
    command = subprocess.Popen(['echo', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sh = subprocess.Popen(['./mysh'], stdin=command.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    command.wait()
    out, err = sh.communicate()
    if not sucess:
        if sh.returncode != errorCode:
            print("Wrong error code")
        if err != errOut:
            print("Wrong error output")
        if err.decode('utf-8') == errOut and sh.returncode == errorCode and not sucess:
            print("Passed")
    if sucess:
        if sh.returncode != successCode:
            print("Wrong error code")
        if err != errOut:
            print("Wrong error output")
        if err.decode('utf-8') == errOut and sh.returncode == errorCode and not sucess:
            print("Passed")


subprocess.run(['make'])
print("minishell1 tester")
TEST("./seg", False, segfaultMessage, noErr)
TEST("ls", True, noErr, noErr)
TEST("exitt", False, commandNotFound, noErr)
