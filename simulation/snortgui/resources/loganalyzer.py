# src/loganalyzer.py
import matplotlib.pyplot as plt
import re
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Fonction principale pour analyser les logs
def analyze_logs():
    # Demander le mot de passe administrateur
    sudo_password = simpledialog.askstring("Password", "Enter your administrator password:", show='*')
    if sudo_password:
        # Sélection du fichier de logs
        filename = filedialog.askopenfilename(initialdir='/etc/snort/logs/', title='Select Alert')
        if filename:
            with open(filename, 'r') as file:
                file_contents = file.read()
                if not file_contents:
                    messagebox.showerror("Error", "No Alerts detected!")
                else:
                    # Analyse des logs
                    tcp_count, icmp_count, ip_count, udp_count, total_count = 0, 0, 0, 0, 0
                    for line in file_contents.split('\n'):
                        total_count += 1
                        if "{TCP}" in line: tcp_count += 1
                        if "{ICMP}" in line: icmp_count += 1
                        if "{IP}" in line: ip_count += 1
                        if "{UDP}" in line: udp_count += 1

                    # Affichage des résultats sous forme de graphique
                    display_results(tcp_count, icmp_count, ip_count, udp_count)

def display_results(tcp_count, icmp_count, ip_count, udp_count):
    labels, counts, colors = [], [], []
    if tcp_count > 0:
        labels.append("TCP")
        counts.append(tcp_count)
        colors.append('tab:blue')
    if icmp_count > 0:
        labels.append("ICMP")
        counts.append(icmp_count)
        colors.append('tab:orange')
    if ip_count > 0:
        labels.append("IP")
        counts.append(ip_count)
        colors.append('tab:green')
    if udp_count > 0:
        labels.append("UDP")
        counts.append(udp_count)
        colors.append('tab:red')

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(counts, labels=labels, colors=colors, wedgeprops={'width': 0.2, 'edgecolor': 'w'}, autopct='%1.1f%%')
    plt.setp(autotexts, size=12, weight="bold")

    plt.show()

if __name__ == "__main__":
    analyze_logs()
