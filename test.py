#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Mihai Criveti
Description: This Python script executes commands listed in a text file, reports their execution status, output, and execution time,
then generates a report. It now accepts configurable paths for the output file and commands file from the CLI.
"""

import argparse
import subprocess
from datetime import datetime

# Default paths
DEFAULT_OUTPUT_FILE = "test/test_commands.md"
DEFAULT_OUTPUT_FILE_FULL = "test/test_commands_full.md"
DEFAULT_SUMMARY_FILE = "test/test_commands_summary.md"
DEFAULT_COMMANDS_FILE = "test/test_commands.sh"

# Emoji constants
SUCCESS_EMOJI = "✅"
FAILURE_EMOJI = "❌"
INFO_EMOJI = "🧪"


def parse_arguments():
    """
    Parses command line arguments to configure paths.
    """
    parser = argparse.ArgumentParser(description="Execute commands from a file and generate a report.")
    parser.add_argument(
        "--output-file",
        default=DEFAULT_OUTPUT_FILE,
        help="Path to the output markdown file.",
    )
    parser.add_argument(
        "--output-file-full",
        default=DEFAULT_OUTPUT_FILE_FULL,
        help="Path to the full output markdown file.",
    )
    parser.add_argument(
        "--summary-file",
        default=DEFAULT_SUMMARY_FILE,
        help="Path to the summary markdown file.",
    )
    parser.add_argument(
        "--commands-file",
        default=DEFAULT_COMMANDS_FILE,
        help="Path to the file containing commands to execute.",
    )
    parser.add_argument(
        "--max-output-lines",
        type=int,
        default=10,
        help="Maximum number of lines to include in the default output file.",
    )
    return parser.parse_args()


def read_commands(file_path: str) -> list:
    """
    Reads commands and comments from a specified text file.
    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"{FAILURE_EMOJI} Commands file {file_path} not found.")
        exit(1)


def execute_command(command: str) -> tuple:
    """
    Executes a given command and captures its output, error, and execution time.
    """
    print(f"{INFO_EMOJI} Executing: {command}")
    start_time = datetime.now()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
    stdout, _ = process.communicate()
    end_time = datetime.now()

    duration = (end_time - start_time).total_seconds()
    success = process.returncode == 0

    status_emoji = SUCCESS_EMOJI if success else FAILURE_EMOJI
    output_log = f"{status_emoji} Command: `{command}` executed in ⏱️  {duration:.2f} seconds.\n\nOutput:\n\n```\n{stdout}\n```\n\n"
    print(output_log)

    return stdout, duration, success, output_log


def write_report(
    lines: list,
    output_file: str,
    output_file_full: str,
    summary_file: str,
    max_output_lines: int,
):
    """
    Executes commands, captures their outputs, adds comments, and writes three separate reports.
    """
    successful_commands = []
    failed_commands = []
    header = "# Command Execution Report\n\n> Report generated on: {}\n\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    try:
        with open(output_file, "w") as file, open(output_file_full, "w") as full_file, open(summary_file, "w") as summary:
            file.write(header)
            full_file.write(header)
            summary.write(header)

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("#"):  # It's a comment
                    comment_log = f"{line}\n\n"
                    file.write(comment_log)
                    full_file.write(comment_log)
                else:
                    output, duration, success, output_log = execute_command(line)
                    lines_output = output.split("\n")

                    truncated_output = "\n".join(lines_output[:max_output_lines])
                    truncated_output_log = f"{SUCCESS_EMOJI if success else FAILURE_EMOJI} Command: `{line}` executed in ⏱️  {duration:.2f} seconds.\n\nOutput:\n\n```\n{truncated_output}\n"

                    if len(lines_output) > max_output_lines:
                        more_lines_count = len(lines_output) - max_output_lines
                        truncated_output_log += f"\n[{more_lines_count} more lines - written to full.md]\n"
                    truncated_output_log += "```\n\n"

                    file.write(truncated_output_log)
                    full_file.write(output_log)

                    if success:
                        successful_commands.append(line)
                    else:
                        failed_commands.append(line)

            count_successful = len(successful_commands)
            count_failed = len(failed_commands)
            total_commands = count_successful + count_failed
            summary_content = f"## Summary\n**Total Commands Executed:** {total_commands}\n**Successful Commands:** {count_successful}\n**Failed Commands:** {count_failed}\n\n"

            if successful_commands:
                summary_content += "### Successful Commands:\n"
                for command in successful_commands:
                    summary_content += f"- `{command}`\n"
            if failed_commands:
                summary_content += "\n### Failed Commands:\n"
                for command in failed_commands:
                    summary_content += f"- `{command}`\n"
            if not failed_commands:
                summary_content += "\nAll commands executed successfully. 🎉\n"

            summary.write(summary_content)

    except Exception as e:
        print(f"{FAILURE_EMOJI} Error writing report: {e}")


if __name__ == "__main__":
    args = parse_arguments()
    lines = read_commands(args.commands_file)
    # Pass all required arguments to the write_report function
    write_report(
        lines,
        args.output_file,
        args.output_file_full,
        args.summary_file,
        args.max_output_lines,
    )
    completion_message = f"{INFO_EMOJI} Command execution reports have been written to {args.output_file}, {args.output_file_full}, and {args.summary_file}"
    print(completion_message)
