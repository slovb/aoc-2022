module Day07.Input ( readInput, MyFiles(..), getSize ) where

import Data.Char ( isDigit )

import Data.List ( isPrefixOf ) 

data MyFiles = EmptyNode
           | MyFile { name :: String, size :: Int }
           | MyFolder { name :: String, size :: Int, children :: [MyFiles] }
           deriving (Show) 

getSize :: MyFiles -> Int
getSize (MyFile _ size) = size
getSize (MyFolder _ size _) = size

readInput :: [String] -> MyFiles
readInput lines = files
    where (files:_, _) = readLevel ([], lines)

readLevel :: ([MyFiles], [String]) -> ([MyFiles], [String])
readLevel (files, []) = (files, [])
readLevel (files, line:rest)
    | isCdUp line = (files, rest)
    | isCd line = readLevel (files ++ [folder], nextRest)
    | isFile line = readLevel (files ++ [file], rest)
    | otherwise = readLevel (files, rest)
    where
        folderName = drop 5 line
        (children, nextRest) = readLevel ([], rest)
        size = sum $ map getSize children
        folder = MyFolder folderName size children
        file = readMyFile line

isCdUp :: String -> Bool
isCdUp "$ cd .." = True
isCdUp _ = False

isCd :: String -> Bool
isCd line
    | "$ cd " `isPrefixOf` line = True
    | otherwise = False

isFile :: String -> Bool
isFile line
    | all isDigit $ take 1 line = True
    | otherwise = False

readMyFile :: String -> MyFiles
readMyFile line = MyFile name size
    where
        (sizeAsString, _:name) = span (/= ' ') line
        size = read sizeAsString :: Int
