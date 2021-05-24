# probdist
pbc unwrap -sel "not type 11 12 13" -all


# Multiple files
To process several files at one, that have the same filename beggining, use the command:
```
/bin/ls dist_* | sed 's/\.xyz//' | xargs -I % probdist.py -i %.xyz -o %.dat
```
