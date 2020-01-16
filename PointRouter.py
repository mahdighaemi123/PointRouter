import time

Relations = []

Relations.append(["A", "Q", 3])
Relations.append(["A", "B", 1])
Relations.append(["A", "G", 4])

Relations.append(["B", "E", 7])
Relations.append(["B", "C", 2])

Relations.append(["E", "C", 4])
Relations.append(["E", "S", 1])
Relations.append(["E", "D", 3])

Relations.append(["D", "F", 3])

Relations.append(["F", "S", 3])
Relations.append(["F", "O", 5])

Relations.append(["O", "C", 2])
Relations.append(["O", "S", 1])
Relations.append(["O", "G", 4])

Relations.append(["C", "G", 1])


Relations.append(["H", "A", 20])
Relations.append(["H", "B", 10])
Relations.append(["H", "Z", 20])
Relations.append(["H", "E", 10])


Relations.append(["Z", "E", 20])
Relations.append(["Z", "W", 30])
Relations.append(["D", "W", 30])
Relations.append(["E", "W", 30])

OptimizeRelations = []
FastestRelations = []
LongestRelations = []
WorstRelations = []
AllRelations = []
Points = []


def FindPoints():
    for Relation in Relations:
        if Relation[0] not in Points:
            Points.append(Relation[0])
        if Relation[1] not in Points:
            Points.append(Relation[1])


def FindAllRelations():
    for Point_1 in Points:
        for Point_2 in Points:
            if Point_1 != Point_2:
                RelationFinder([Point_1], Point_2)


def RelationFinder(Routes, Goal):
    NowPoint = Routes[len(Routes) - 1]

    for Relation in Relations:

        if Relation[0] == NowPoint and Relation[1] not in Routes:

            if Relation[1] == Goal:
                AllRoutes = Routes.copy()
                AllRoutes.append(Goal)
                AllCost = CalculateCost(AllRoutes)

                AddNewRelation(Routes[0], Goal, AllCost, AllRoutes)
                return

            NewRoutes = Routes.copy()
            NewRoutes.append(Relation[1])

            RelationFinder(NewRoutes, Goal)

        if Relation[1] == NowPoint and Relation[0] not in Routes:

            if Relation[0] == Goal:
                AllRoutes = Routes.copy()
                AllRoutes.append(Goal)
                AllCost = CalculateCost(AllRoutes)

                AddNewRelation(Routes[0], Goal, AllCost, AllRoutes)
                return

            NewRoutes = Routes.copy()
            NewRoutes.append(Relation[0])

            RelationFinder(NewRoutes, Goal)


def CalculateCost(AllRoutes):
    AllCost = 0
    for i in range(0, len(AllRoutes) - 1):
        AllCost = AllCost + GetRelationCost(AllRoutes[i], AllRoutes[i + 1])
    return AllCost


def GetRelationCost(Point_1, Point_2):
    for Relation in Relations:
        if Relation[0] == Point_1 and Relation[1] == Point_2:
            return Relation[2]

        if Relation[0] == Point_2 and Relation[1] == Point_1:
            return Relation[2]
    return 0


def FindOptimizeRelations():
    for MainRelation in AllRelations:
        if not IsBestRelationToAddOptimize(MainRelation):
            OptimizeRelations.append(MainRelation)


def FindWorstRelations():
    for MainRelation in AllRelations:
        if not IsWorstRelationToAddWorsts(MainRelation):
            WorstRelations.append(MainRelation)


def FindFastRelations():
    for MainRelation in AllRelations:
        if not IsFastRelationToAddFastest(MainRelation):
            FastestRelations.append(MainRelation)


def FindLongRelations():
    for MainRelation in AllRelations:
        if not IsLongRelationToAddLongest(MainRelation):
            LongestRelations.append(MainRelation)


def IsBestRelationToAddOptimize(MainRelation):
    Point_1 = MainRelation[0]
    Point_2 = MainRelation[1]
    AllCost = MainRelation[2]
    Routes = MainRelation[3]

    for Relation in AllRelations:
        if Relation[0] == Point_1 and Relation[1] == Point_2 and Relation[2] < AllCost:
            return True

        if Relation[0] == Point_2 and Relation[1] == Point_1 and Relation[2] < AllCost:
            return True

        if Relation[0] == Point_1 and Relation[1] == Point_2 and Relation[2] == AllCost and len(Routes) > len(
                Relation[3]):
            return True

        if Relation[0] == Point_2 and Relation[1] == Point_1 and Relation[2] == AllCost and len(Routes) > len(
                Relation[3]):
            return True

    return False


def IsWorstRelationToAddWorsts(MainRelation):
    Point_1 = MainRelation[0]
    Point_2 = MainRelation[1]
    AllCost = MainRelation[2]
    Routes = MainRelation[3]

    for Relation in AllRelations:
        if Relation[0] == Point_1 and Relation[1] == Point_2 and Relation[2] > AllCost:
            return True

        if Relation[0] == Point_2 and Relation[1] == Point_1 and Relation[2] > AllCost:
            return True

        if Relation[0] == Point_1 and Relation[1] == Point_2 and Relation[2] == AllCost and len(Routes) < len(
                Relation[3]):
            return True

        if Relation[0] == Point_2 and Relation[1] == Point_1 and Relation[2] == AllCost and len(Routes) < len(
                Relation[3]):
            return True

    return False


def IsFastRelationToAddFastest(MainRelation):
    Point_1 = MainRelation[0]
    Point_2 = MainRelation[1]
    AllCost = MainRelation[2]
    Routes = MainRelation[3]

    for Relation in AllRelations:
        if Relation[0] == Point_1 and Relation[1] == Point_2 and len(Routes) > len(Relation[3]):
            return True

        if Relation[0] == Point_2 and Relation[1] == Point_1 and len(Routes) > len(Relation[3]):
            return True

        if Relation[0] == Point_1 and Relation[1] == Point_2 and Relation[2] < AllCost and len(Routes) == len(
                Relation[3]):
            return True

        if Relation[0] == Point_2 and Relation[1] == Point_1 and Relation[2] < AllCost and len(Routes) == len(
                Relation[3]):
            return True

    return False


def IsLongRelationToAddLongest(MainRelation):
    Point_1 = MainRelation[0]
    Point_2 = MainRelation[1]
    AllCost = MainRelation[2]
    Routes = MainRelation[3]

    for Relation in AllRelations:
        if Relation[0] == Point_1 and Relation[1] == Point_2 and len(Routes) < len(Relation[3]):
            return True

        if Relation[0] == Point_2 and Relation[1] == Point_1 and len(Routes) < len(Relation[3]):
            return True

        if Relation[0] == Point_1 and Relation[1] == Point_2 and Relation[2] < AllCost and len(Routes) == len(
                Relation[3]):
            return True

        if Relation[0] == Point_2 and Relation[1] == Point_1 and Relation[2] < AllCost and len(Routes) == len(
                Relation[3]):
            return True

    return False


def AddNewRelation(Point_1, Point_2, AllCost, Routes):
    AllRelations.append([Point_1, Point_2, AllCost, Routes])


def FindBestWay(Point_1, Point_2):
    for Relation in OptimizeRelations:
        if Relation[0] == Point_1 and Relation[1] == Point_2:
            return Relation

        if Relation[0] == Point_2 and Relation[1] == Point_1:
            return Relation


def FindWorstWay(Point_1, Point_2):
    for Relation in WorstRelations:
        if Relation[0] == Point_1 and Relation[1] == Point_2:
            return Relation

        if Relation[0] == Point_2 and Relation[1] == Point_1:
            return Relation


def FindLongWay(Point_1, Point_2):
    for Relation in LongestRelations:
        if Relation[0] == Point_1 and Relation[1] == Point_2:
            return Relation

        if Relation[0] == Point_2 and Relation[1] == Point_1:
            return Relation


def FindFastWay(Point_1, Point_2):
    for Relation in FastestRelations:
        if Relation[0] == Point_1 and Relation[1] == Point_2:
            return Relation

        if Relation[0] == Point_2 and Relation[1] == Point_1:
            return Relation


startTime = time.time()

FindPoints()
FindAllRelations()
FindFastRelations()
FindLongRelations()
FindWorstRelations()
FindOptimizeRelations()

endTime = time.time()
calculateTime = endTime-startTime

print("PointRouter v1")
print("CalculateTime -> ", calculateTime)
print()

print("# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #")
print()

print("Points            ", "[", len(Points), "]", Points)
print("Relations         ", "[", len(Relations), "]", Relations)
print("AllRelations      ", "[", len(AllRelations), "]", AllRelations)
print("WorstRelations    ", "[", len(WorstRelations), "]", WorstRelations)
print("FastestRelations  ", "[", len(FastestRelations), "]", FastestRelations)
print("LongestRelations  ", "[", len(LongestRelations), "]", LongestRelations)
print("OptimizeRelations ", "[", len(OptimizeRelations), "]", OptimizeRelations)
print()

print("# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #")
print()

print("A TO D")
print("LowestCostAndFastWay      ", FindBestWay("A", "D"))
print("MostExpensiveAndLongWay   ", FindWorstWay("A", "D"))
print("FastAndCheapWay           ", FindFastWay("A", "D"))
print("LongAndCheapWay           ", FindLongWay("A", "D"))