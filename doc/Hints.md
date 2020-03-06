# CS 1440 Assignment 2 Hints

## area_titles.csv

*   Read this file line-by-line. As you read it in:
    *   Discard unwanted FIPS areas as you read.
    *   Collect this data into a Python dictionary mapping FIPS codes to area
        titles.
*   FIPS area codes follow a simple pattern which makes it easy to exclude the
    national aggregate, statewide aggregate metropolitan and micropolitan
    areas.
*   `area_titles.csv` contains 4,724 lines of text, of which the first is a CSV
    header line.  After discarding unwanted FIPS areas you will be left with
    3,461 FIPS areas.


## 2018.annual.singlefile.csv

*   Read this file line-by-line. As you read it in:
    *   Discard lines from FIPS areas which do not belong in the report.
    *   Discard lines from industries which do not belong in the report.
*   Keep track of the data required for the report. You must accumulate totals
    as well as store maximum values for three categories.
*   This is a very big file and your program will take a long time to read it
    (my implimentation takes ~6.5 seconds to read it once on my laptop).
    Strive to minimize the number of times your program reads through it.
*   Make sure that you have a program that *works* before you worry about
    having a program that is *fast*.

> Programmers waste enormous amounts of time thinking about, or worrying about,
> the speed of noncritical parts of their programs, and these attempts at
> efficiency actually have a strong negative impact when debugging and
> maintenance are considered. We should forget about small efficiencies, say
> about 97% of the time: premature optimization is the root of all evil. Yet we
> should not pass up our opportunities in that critical 3%.
> 
> – Donald Knuth
> "Structured Programming With Go To Statements"
> Computing Surveys, Vol 6, No 4, December 1974


## Cite external sources in your repository's `README.md`.
