This dataset was generated from a full copy of the data file
`2018.annual.singlefile.csv` using a version of `tt.py` containing the
`startgrep` subcommand and this sequence of commands:

    python tt.py head -n 1 2018.annual.singlefile.csv > header.csv
    python tt.py startgrep '"11' 2018.annual.singlefile.csv > dat.csv
    python tt.py grep '"0","10"' dat.csv > trimmed.csv
    python tt.py cat header.csv trimmed.csv > 2018.annual.singlefile.csv
    rm header.csv dat.csv trimmed.csv
