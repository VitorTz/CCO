cmake_minimum_required(VERSION 3.29)
project(VJudge)

set(CMAKE_CXX_STANDARD 11)

add_executable(VJudge main.cpp
        Solution.h
        ThrowingCardsAway.h
        IDCodes.h
        Rails.h
        Conformity.h
        ClosestSums.h
        Exhibition.h
        Multitasking.h
        HoaxOrwhat.h
        ContestScoreboard.h)
