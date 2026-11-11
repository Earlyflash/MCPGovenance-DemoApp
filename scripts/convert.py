"""Convert the nightly report. The command is a constant string, so a shell is safe here."""

import subprocess


def convert_report():
    subprocess.run("pandoc report.md -o report.pdf", shell=True, check=True)
