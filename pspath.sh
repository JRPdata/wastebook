#!/bin/bash
# print PID and command with full PATH and ARGS
# uses readlink, pgrep, ps, bash

if [ $# -eq 0 ]; then
  echo "Usage: $0 <partial_program_name>"
  exit 1
fi

SCRIPT_NAME=$1

for PID in $(pgrep -f "$SCRIPT_NAME" | grep -v $$); do
  CMD=$(ps -p "$PID" -o args=)   # Get the command line
  PROG_PATH=$(readlink -f /proc/"$PID"/exe)  # Get the program path
  
  # Extract the first word of the CMD (i.e., the program name)
  FIRST_WORD=$(echo "$CMD" | awk '{print $1}')


  # Skip iteration if CMD or PROG_PATH is empty
  if [ -z "$CMD" ] || [ -z "$PROG_PATH" ]; then
    continue
  fi

  # Check if the first word starts with a '/', './', or '../' (absolute or relative path)
  if [[ "$FIRST_WORD" != /* && "$FIRST_WORD" != ./* && "$FIRST_WORD" != ../* ]]; then
    # If it's not a path, replace it with the program path
    CMD="$PROG_PATH ${CMD#* }"  # Replace the first word with PROG_PATH and keep the rest of the CMD
  fi

  echo "PID: $PID, CMD: $CMD"
done
