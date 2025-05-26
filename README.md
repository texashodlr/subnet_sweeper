# subnet_sweeper
This repository contains a simple Python script that performs concurrent ping (ICMP Echo Requests) sweeps of subnets specified in a CSV file

## Prerequisites
- A 64-bit Windows or Linux (RHEL; coming soon) System
- Administrative/Root privileges (root, for ping/file ops. on Linux)
- For Linux: Ensure `tar` is available to extract Python

## Repository Contents
- `subnet_sweeper.py`: The main script.
- `subnets.csv`: Input file specifiying the desired subnets to scan (with relevant prefix sizing)
- `requirements.txt`: Lists the `ping3` dependency.
- `ping3_deps/`: Contains the `ping3` wheel file.
- `python/`: Contains the portable Python and `get-pip.py` file.
- `setup.bat` (Windows) or `setup.sh` (Linux): Setup and run script.

## Setup instructions
### For Windows/Linux
1. Clone this entire repo then export it to your media of choice.
2. Copy+paste the repo onto the airgapped machine
3. Open the airgapped machine's CLI and navigate to the project directory
4. Run the relevant setup script this will also run the subnet sweeper
5. Outputs will be written to `subnet_sweep_results{timestamp}.csv`

## Todo
- Add MAC Address retrieval so that the script saves the MAC Address of a host at a particular IP
- Add hostname retrieval so that the script saves the hostname of a host at a particular IPi 
