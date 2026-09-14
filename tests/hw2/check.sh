#!/bin/bash
# Check that actual output matches expected output
# Usage: stella typecheck < input_file | ./chech.sh input_file expected_output_file
#
# Expected output file format:
#   - Contains ERROR_... tags (one per line) if errors are expected
#   - Empty if no errors are expected (well-typed program)
#
# Actual output (stdin):
#   - Full stella typecheck output
#   - Should contain exactly one ERROR_... tag matching expected, or no tags if expected is empty

set -e

if [ $# -ne 2 ]; then
    echo "Usage: $0 <input_file> <expected_output_file>" >&2
    echo "Actual output should be piped via stdin" >&2
    exit 1
fi

input_file="$1"
expected_file="$2"

if [ ! -f "$expected_file" ]; then
    echo "Error: Expected output file '$expected_file' not found" >&2
    exit 1
fi

# Read actual output from stdin
actual_output=$(cat)

# Check if stdin was empty (user didn't pipe input)
if [ -z "$actual_output" ] && [ -t 0 ]; then
    echo "Error: No input provided via stdin. Please pipe stella typecheck output:" >&2
    echo "  cat input_file | stella typecheck 2>&1 | $0 input_file expected_output_file" >&2
    exit 1
fi

# Extract ERROR_... tags from expected output (one per line, already extracted)
expected_tags=$(cat "$expected_file" | grep -E '^ERROR_' || true)

# Extract ERROR_... tags from actual output (full stella output)
# Look for patterns like "Type Error Tag: [ERROR_...]" or "[ERROR_...]" or "ERROR_..."
# Handle both bracketed and unbracketed tags
actual_tags=$(echo "$actual_output" | grep -oE '(\[ERROR_[A-Z_]+\]|ERROR_[A-Z_]+)' | sed 's/\[\(.*\)\]/\1/' | sort -u || true)

# Count tags (count non-empty lines)
if [ -z "$expected_tags" ]; then
    expected_count=0
else
    expected_count=$(echo "$expected_tags" | wc -l | tr -d ' ')
fi

if [ -z "$actual_tags" ]; then
    actual_count=0
else
    actual_count=$(echo "$actual_tags" | wc -l | tr -d ' ')
fi

# Check conditions
if [ "$expected_count" -eq 0 ]; then
    # Expected: no errors (well-typed program)
    if [ "$actual_count" -eq 0 ]; then
        exit 0  # Success: no errors expected and none found
    else
        echo "Error: Expected no errors but found $actual_count error tag(s):" >&2
        echo "$actual_tags" | sed 's/^/  - /' >&2
        exit 1
    fi
else
    # Expected: at least one error tag
    if [ "$actual_count" -eq 0 ]; then
        echo "Error: Expected error tag(s) but found none" >&2
        echo "Expected:" >&2
        echo "$expected_tags" | sed 's/^/  - /' >&2
        exit 1
    elif [ "$actual_count" -gt 1 ]; then
        echo "Error: Expected exactly one error tag but found $actual_count:" >&2
        echo "$actual_tags" | sed 's/^/  - /' >&2
        exit 1
    else
        # Exactly one actual tag - check if it matches one of the expected tags
        actual_tag=$(echo "$actual_tags" | head -1)
        if echo "$expected_tags" | grep -qFx "$actual_tag"; then
            exit 0  # Success: actual tag matches one of the expected tags
        else
            echo "Error: Actual error tag '$actual_tag' does not match any expected tag" >&2
            echo "Expected:" >&2
            echo "$expected_tags" | sed 's/^/  - /' >&2
            echo "Actual:" >&2
            echo "  - $actual_tag" >&2
            exit 1
        fi
    fi
fi
