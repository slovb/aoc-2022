module Day06.Solution (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Data.Set ( fromList )

test :: Int -> String -> Bool
test len xs | len == length (fromList $ take len xs) = True
            | otherwise = False

solve :: Int -> Int -> String -> Int
solve len i xs | test len xs = i + len
               | otherwise = solve len (i + 1) $ tail xs

main :: IO ()
main = do
    let filename = "Day06/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    print xs
    print $ map (solve 4 0) xs
    print $ map (solve 14 0) xs
    hClose handler
