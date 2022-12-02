module Day02.FirstInput where

import Day02.Hand ( Hand(Rock, Paper, Scissors) )

readInput :: [String] -> [(Hand, Hand)]
readInput = map readHands

readHands :: String -> (Hand, Hand)
readHands s = (readHand . head $ s, readHand . last $ s)

readHand :: Char -> Hand
readHand 'A' = Rock
readHand 'B' = Paper
readHand 'C' = Scissors
readHand 'X' = Rock
readHand 'Y' = Paper
readHand 'Z' = Scissors
