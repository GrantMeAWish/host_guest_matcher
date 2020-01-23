# host_guest_matcher

This repo contains a host guest matching algorithm.

The matcher reads in csv files of host and guest information, runs the matching algorithm that outputs host guest
pairs, and writes the matches to a new csv file. It is tested on python version 3.6.7 and 2.7.10

## Running the matcher
Make sure you are in the home directory. Then run the following.

```
$ python main.py
```

The outputted match csv file will be saved in the `csv_files` directory