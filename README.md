# probdist
Creates histogram files (.png and .dat) from a .xyz of two atoms.

Make sure to remove effects of periodic boundary conditions, with, for example:
```
pbc unwrap -sel "not type 11 12 13" -all
```

# Multiple files
To process several files at one, that have the same filename beggining, use the command:
```
/bin/ls dist_*.xyz | sed 's/\.xyz//' | xargs -I % probdist.py -i %.xyz -o %.dat
```
