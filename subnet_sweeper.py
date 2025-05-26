#!/usr/bin/env python3

# This script is a concurrent version of the other subnet sweeper allowing users to concurrently ping multiple subnets
# This script builds on ip scanner and checks whole subnets
# Pulled from: https://www.packetswitch.co.uk/how-to-ping-sweep-your-network-with-python/

import datetime
import ipaddress
import concurrent.futures
import threading
import csv
from ping3 import ping

def load_subnets(csv_file_path):
    subnets = []
    try:
        with open(csv_file_path, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            if not{'Subnet', 'Prefix'}.issubset(reader.fieldnames):
                raise ValueError("CSV must contain 'Subnet' and 'Prefix' columns")
            for row in reader:
                subnet = f"{row['Subnet']}/{row['Prefix']}"
                # Validating the subnet format
                ipaddress.ip_network(subnet, strict=False)
                subnets.append(subnet)
        return subnets
    except FileNotFoundError:
        print(f"Error: {csv_file_path} not found")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

subnet_csv_file = 'subnets.csv'
subnets = load_subnets(subnet_csv_file)
if not subnets:
    print("No valid subnets loaded, exiting.")
    exit(1)

timestamp_file = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
output_file = f"subnet_sweep_results_{timestamp_file}.csv"
output_lock = threading.Lock()

def ping_sweep(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    results = []

    for ip in network.hosts():
        ip_str = str(ip)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            response_time = ping(ip_str, timeout=1)
            if response_time is not None:
                status = "reachable"
            else:
                status = "unreachable"
        except Exception:
            status = "error"
        # Storing the sweep results as a dictionary for a CSV
        results.append({
            "Timestamp": timestamp,
            "Subnet": subnet,
            "IP": ip_str,
            "Status": status
         })

    with output_lock:
        print(f"Ping results for subnet {subnet}:")
        with open (output_file, 'a',newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Timestamp", "Subnet", "IP", "Status"])
            if f.tell() == 0:
                writer.writeheader()
            for result in results:
                    print(f"{result['Timestamp']} - {result['IP']} is {result['Status']}")
                    writer.writerow(result)
        print()

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(ping_sweep, subnets)
