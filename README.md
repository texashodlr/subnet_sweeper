# subnet_sweeper
A simple python script to sweep the subnets of your choosing

This repository contains a Python script that performs concurrent ping sweeps of subnets specified in a CSV file

## Prerequisites
- A 64-bit Windows or Linux (coming soon) System
- Administrative/Root privileges (root, for ping/file ops. on Linux)
- For Linux (tm): Ensure `tar` is available to extract Python

## Repository Contents
- `subnet_sweeper.py`: The main script.
- `subnets.csv`: Input file specifiying the desired subnets to scan (with relevant prefix sizing)
- `requirements.txt`: Lists the `ping3` dependency.
- `ping3_deps/`: Cotnains the `ping3` wheel file.
- `python/`: Contains the portable Python and `get-pip.py` file.
- `setup.bat` (Windows) or `setup.sh` (Linux): Setup and run script.

## Setup instructions
### For Windows/Linux
1. Clone this entire repo then export it to your media of choice.
2. Copy+paste the repo onto the airgapped machine
3. Open the airgapped machine's CLI and navigate to the project directory
4. Run the relevant setup script this will also run the subnet sweeper
5. Outputs will be written to `subnet_sweep_results{timestamp}.csv` 
