import os.path
import subprocess


class test:
    def __init__(self, name, filesToSolve, filesSolved):
        self.name = name
        self.filesToSolve = filesToSolve
        self.filesSolved = filesSolved
        self.failed = 0
        self.success = 0

    def execTest(self):
        for file in self.filesToSolve:
            idx = self.filesToSolve.index(file)
            outputToSolve = subprocess.check_output(['./bsq', file])
            retValTest = os.system("./bsq " + file + "> /dev/null")
            if outputToSolve == subprocess.check_output(['cat', self.filesSolved[idx]]) and retValTest == 0:
                self.success += 1
            else:
                self.failed += 1

    def result(self):
        print("\033[7;49;96m" + self.name)
        print("\033[7;49;92mSucess: " + str(self.success))
        print("\033[7;49;91mFailed: " + str(self.failed))
        print("\033[0m")


if __name__ == "__main__":
    retVal = subprocess.call(['make', 're'])
    if retVal != 0:
        build_error = "\033[7;49;91mBUILD ERROR"
        print(build_error)
        exit(-1)
    if not os.path.exists("maps-intermediate"):
        print("Please bring the maps given in the subject")
    if os.path.exists("maps-intermediate"):
        t = test("Basics", [
            "maps-intermediate/mouli_maps/intermediate_map_97_21_with_obstacles_25pc",
            "maps-intermediate/mouli_maps/intermediate_map_97_21_with_obstacles_50pc",
            "maps-intermediate/mouli_maps/intermediate_map_97_21_with_obstacles_75pc"
        ], [
            "maps-intermediate/mouli_maps_solved/intermediate_map_97_21_with_obstacles_25pc",
            "maps-intermediate/mouli_maps_solved/intermediate_map_97_21_with_obstacles_50pc",
            "maps-intermediate/mouli_maps_solved/intermediate_map_97_21_with_obstacles_75pc"
        ])
        t.execTest()
        t.result()
        t = test("Algorithm app. - Opening rectangle", [
            "maps-intermediate/mouli_maps/intermediate_map_34_137_with_obstacles_25pc",
            "maps-intermediate/mouli_maps/intermediate_map_34_137_with_obstacles_50pc",
            "maps-intermediate/mouli_maps/intermediate_map_34_137_with_obstacles_75pc"
        ], [
                     "maps-intermediate/mouli_maps_solved/intermediate_map_34_137_with_obstacles_25pc",
                     "maps-intermediate/mouli_maps_solved/intermediate_map_34_137_with_obstacles_50pc",
                     "maps-intermediate/mouli_maps_solved/intermediate_map_34_137_with_obstacles_75pc"
                 ])
        t.execTest()
        t.result()
        t = test("Algorithm app. - Opening 100 to 500", [
            "maps-intermediate/mouli_maps/intermediate_map_100_100",
            "maps-intermediate/mouli_maps/intermediate_map_200_200",
            "maps-intermediate/mouli_maps/intermediate_map_500_500",
            "maps-intermediate/mouli_maps/intermediate_map_500_500_2",
            "maps-intermediate/mouli_maps/intermediate_map_500_500_3",
        ], [
             "maps-intermediate/mouli_maps_solved/intermediate_map_100_100",
             "maps-intermediate/mouli_maps_solved/intermediate_map_200_200",
             "maps-intermediate/mouli_maps_solved/intermediate_map_500_500",
             "maps-intermediate/mouli_maps_solved/intermediate_map_500_500_2",
             "maps-intermediate/mouli_maps_solved/intermediate_map_500_500_3",
        ])
        t.execTest()
        t.result()
        t = test("Algorithm app. - Opening 1000 to 2000", [
            "maps-intermediate/mouli_maps/intermediate_map_1000_1000",
            "maps-intermediate/mouli_maps/intermediate_map_1000_1000_2",
            "maps-intermediate/mouli_maps/intermediate_map_2000_2000"
        ], [
            "maps-intermediate/mouli_maps_solved/intermediate_map_1000_1000",
            "maps-intermediate/mouli_maps_solved/intermediate_map_1000_1000_2",
            "maps-intermediate/mouli_maps_solved/intermediate_map_2000_2000"
         ])
        t.execTest()
        t.result()
        t = test("Algorithm app. - Opening 5000 to 10000", [
            "maps-intermediate/mouli_maps/intermediate_map_5000_5000",
            "maps-intermediate/mouli_maps/intermediate_map_10000_10000"
        ], [
             "maps-intermediate/mouli_maps_solved/intermediate_map_5000_5000",
             "maps-intermediate/mouli_maps_solved/intermediate_map_10000_10000"
         ])
        t.execTest()
        t.result()
