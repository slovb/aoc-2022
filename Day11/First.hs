module Day11.First (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day11.Monkey ( State, getCount, getItems, composeOp, simulate )

import Day11.Input ( readInput )

import Data.List (sort)

updateOps :: State -> State
updateOps [] = []
updateOps (monkey:monkeys) = newMonkey:updateOps monkeys
    where
        newMonkey = composeOp (`quot` 3) monkey 

solve :: State -> Int -> ([Int], State)
solve monkeys 0 = (map getCount monkeys, monkeys)
solve monkeys i = solve (simulate 0 monkeys) (i - 1)

output :: [Int] -> Int
output count = a * b
    where
        a:b:_ = reverse $ sort count

main :: IO ()
main = do
    let day = "Day11"
    let test = False
    let filename = day ++ if test then "/test.txt" else "/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let monkeys = updateOps $ readInput xs
    -- print [getItems monkey | monkey <- monkeys]
    let (count, newMonkeys) = solve monkeys 20
    print $ output count
    hClose handler
