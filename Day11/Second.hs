module Day11.Second (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day11.Monkey ( State, getCount, getItems, getDivider, composeOp, simulate )

import Day11.Input ( readInput )

import Data.List (sort)

megaDivider :: State -> Int
megaDivider [] = 1
megaDivider (monkey:monkeys) = (left * right) `quot` gcd left right
    where
        left = getDivider monkey
        right = megaDivider monkeys

updateOps :: State -> State
updateOps monkeys = map (composeOp f) monkeys
    where
        n = megaDivider monkeys
        f = (`mod` n)

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
    let (count, newMonkeys) = solve monkeys 10000
    print $ output count
    hClose handler
