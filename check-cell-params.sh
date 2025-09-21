# Extract lattice vectors from POSCAR (lines 3-5, skip first 2 lines)
if [[ ! -e "POSCAR" ]]; then
    echo "Error: POSCAR file not found in current directory" >&2
    exit 1
fi

# Create temporary file with lattice vectors
head POSCAR | head -n 5 | tail -n 4 > TEMP

python $HOME/Skrypty/unitcell.py TEMP 

# Clean up temporary file
rm -f TEMP