#!/bin/python
"""
nmap_port_scanner.py

Purpose: Python wrapper for nmap scanner

Author: Cody Jackson

Date: 12/30/2018
########################
Version 0.1
    Initial build
"""
import argparse
import nmap


def argument_parser():
    """Allow user to specify target host and port."""
    parser = argparse.ArgumentParser(description="TCP port scanner. Accepts a hostname/IP address and list of ports to "
                                                 "scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated port list, such as '25,80,8080'")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary

    return var_args


def nmap_scan(host_id, port_num):
    """Use nmap utility to check host ports for status."""
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id, port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']  # Indicate the type of scan and port number
    result = ("[*] {host} tcp/{port} {state}".format(host=host_id, port=port_num, state=state))

    return result


if __name__ == "__main__":
    try:
        user_args = argument_parser()
        host = user_args["host"]
        ports = user_args["ports"].split(",")  # Make a list from port numbers
        for port in ports:
            print(nmap_scan(host, port))
    except AttributeError:
        print("Error. Please provide the command-line arguments before running.")
