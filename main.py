import os
import nmap
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox


os.environ['PATH'] += r";C:\Program Files (x86)\Nmap"
scanner = nmap.PortScanner()


def run_scan():
    ip_addr = ip_entry.get()
    if not ip_addr:
        messagebox.showerror("Input Error", "Please enter an IP address")
        return

    scan_choice = scan_type.get()
    resp_dict = {
        'SYN ACK Scan': ['-v -sS', 'tcp'],
        'UDP Scan': ['-v -sU', 'udp'],
        'Comprehensive Scan': ['-v -sS -sV -sC -A -O', 'tcp']
    }

    if scan_choice not in resp_dict:
        messagebox.showerror("Input Error", "Please select a valid scan type")
        return

    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, f"Running {scan_choice} on {ip_addr}...\n")
    text_area.update()

    try:
        scanner.scan(ip_addr, '1-1024', resp_dict[scan_choice][0])
        state = scanner[ip_addr].state()
        text_area.insert(tk.END, f"Host status: {state}\n")

        protocols = scanner[ip_addr].all_protocols()
        text_area.insert(tk.END, f"Protocols: {protocols}\n")

        proto = resp_dict[scan_choice][1]
        if proto in protocols:
            open_ports = list(scanner[ip_addr][proto].keys())
            text_area.insert(tk.END, f"Open {proto.upper()} ports: {open_ports}\n")
        else:
            text_area.insert(tk.END, f"No open {proto.upper()} ports found.\n")

    except Exception as e:
        text_area.insert(tk.END, f"Error: {e}\n")



root = tk.Tk()
root.title("Nmap Automation Tool")
root.geometry("600x400")

tk.Label(root, text="IP Address:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
ip_entry = tk.Entry(root, width=30)
ip_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Scan Type:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
scan_type = ttk.Combobox(root, values=['SYN ACK Scan', 'UDP Scan', 'Comprehensive Scan'], state='readonly')
scan_type.grid(row=1, column=1, padx=10, pady=10)
scan_type.current(0)


run_button = tk.Button(root, text="Run Scan", command=run_scan)
run_button.grid(row=2, column=0, columnspan=2, pady=10)


text_area = scrolledtext.ScrolledText(root, width=70, height=15)
text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
