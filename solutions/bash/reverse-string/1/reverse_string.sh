#!/usr/bin/env bash

reverse_string() {
	echo "$1" | rev
}

main() {
	reverse_string "$@"
}

main "$@"
