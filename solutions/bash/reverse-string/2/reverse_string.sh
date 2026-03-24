#!/usr/bin/env bash

reverse_string() {
	text="$1"
	length=${#text}
	reversed=""
	for ((i = length - 1; i >= 0; i--)); do
		reversed="$reversed${text:i:1}"
	done
	echo "$reversed"
}

main() {
	reverse_string "$@"
}

main "$@"
