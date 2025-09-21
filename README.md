# Unit Cell Parameter Calculator

A utility for extracting and calculating crystallographic unit cell parameters from VASP POSCAR files.

## Overview

This tool consists of two scripts that work together to calculate unit cell parameters (lattice constants a, b, c and angles α, β, γ) from VASP structure files:

- **`check-cell-params.sh`**: Shell script that extracts lattice vectors from POSCAR
- **`unitcell.py`**: Python script that calculates unit cell parameters from lattice vectors

## What It Does

The scripts analyze the lattice vectors in a VASP POSCAR file and output the six fundamental crystallographic parameters:

1. **Lattice constants** (a, b, c) - lengths of the unit cell edges in Angstroms
2. **Lattice angles** (α, β, γ) - angles between the unit cell edges in degrees

This is useful for:
- Determining crystal system (cubic, hexagonal, orthorhombic, etc.)
- Comparing structures before and after relaxation
- Reporting crystallographic data in publications
- Analyzing structural distortions

## Requirements

- **Bash shell** (Linux/macOS)
- **Python 2 or 3**
- **POSCAR file** in the current directory

## Installation

1. Place both files in your script directory (e.g., `$HOME/Skrypty/`)
2. Make the shell script executable:
   ```bash
   chmod +x check-cell-params.sh
   ```

## Usage

Navigate to a directory containing a POSCAR file and run:

```bash
./check-cell-params.sh
```

Or if the script is in your PATH:
```bash
check-cell-params.sh
```

## Input File Format

The script reads from a standard VASP POSCAR file. It specifically extracts:
- **Line 2**: Scaling factor
- **Lines 3-5**: Three lattice vectors (a, b, c) as x, y, z components

Example POSCAR structure:
```
System Name
5.64          # Scaling factor
1.0  0.0  0.0 # a vector
0.0  1.0  0.0 # b vector  
0.0  0.0  1.0 # c vector
Element_names
Element_counts
...
```

## Output Format

The script outputs six numbers in this order:
```
12.345678    # a (lattice constant)
12.345678    # b (lattice constant)
12.345678    # c (lattice constant)
90.000       # α (alpha angle in degrees)
90.000       # β (beta angle in degrees)  
90.000       # γ (gamma angle in degrees)
```

## How It Works

1. **`check-cell-params.sh`** extracts the scaling factor and lattice vectors from POSCAR
2. Creates a temporary file (`TEMP`) with this data
3. Calls **`unitcell.py`** to process the lattice vectors
4. **`unitcell.py`** calculates:
   - Vector lengths: `|v| = √(x² + y² + z²) × scale`
   - Angles using dot product: `θ = arccos(u·v / |u||v|)`
5. Outputs the results and cleans up temporary files

## Key Features

- **Scaling factor support**: Properly handles VASP scaling factors from line 2 of POSCAR
- **Automatic cleanup**: Removes temporary files after processing
- **Error checking**: Verifies POSCAR file exists before processing
- **Standard output**: Results can be piped to other programs or files

## Example Usage Scenarios

**Check if structure is cubic:**
```bash
./check-cell-params.sh
# If a=b=c and α=β=γ=90°, it's cubic
```

**Compare before/after relaxation:**
```bash
# In initial structure directory
./check-cell-params.sh > initial_params.txt

# In relaxed structure directory  
./check-cell-params.sh > final_params.txt

diff initial_params.txt final_params.txt
```

**Use in scripts:**
```bash
# Extract just the volume-related parameters
params=$(./check-cell-params.sh)
a=$(echo "$params" | sed -n '1p')
b=$(echo "$params" | sed -n '2p')
c=$(echo "$params" | sed -n '3p')
volume=$(echo "$a * $b * $c" | bc -l)
```

## Crystal System Identification

Based on the output, you can identify crystal systems:

| Crystal System | Conditions |
|----------------|------------|
| Cubic | a = b = c, α = β = γ = 90° |
| Tetragonal | a = b ≠ c, α = β = γ = 90° |
| Orthorhombic | a ≠ b ≠ c, α = β = γ = 90° |
| Hexagonal | a = b ≠ c, α = β = 90°, γ = 120° |
| Trigonal | a = b = c, α = β = γ ≠ 90° |
| Monoclinic | a ≠ b ≠ c, α = γ = 90° ≠ β |
| Triclinic | a ≠ b ≠ c, α ≠ β ≠ γ |

## Troubleshooting

**Error: POSCAR file not found**
- Ensure you're in a directory containing a POSCAR file
- Check file name is exactly "POSCAR" (case-sensitive)

**Python errors**
- Verify Python is installed: `python --version`
- Check the path to unitcell.py in check-cell-params.sh matches your setup

**Incorrect results**
- Verify POSCAR format is correct
- Check that lattice vectors are on lines 3-5
- Ensure scaling factor on line 2 is a valid number

## File Structure

```
your_project/
├── POSCAR              # VASP structure file
├── check-cell-params.sh # Main script
└── unitcell.py         # Calculation engine
```

## Technical Details

The calculations use standard crystallographic formulas:
- **Lattice constants**: `a = |a_vector| × scale`
- **Angles**: `cos(θ) = (u · v) / (|u| × |v|)`

Where the dot product accounts for the scaling factor: `(u · v) × scale²`

## License

This tool is provided as-is for research and educational purposes.

## See Also

- [VASP Manual - POSCAR format](https://www.vasp.at/wiki/index.php/POSCAR)
- [Crystallographic unit cell parameters](https://en.wikipedia.org/wiki/Crystal_system)
- VESTA or XCrySDen for structure visualization
