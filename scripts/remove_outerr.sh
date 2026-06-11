#!/usr/bin/env bash

if [ -f "out_err" ]; then
    echo "Remove the last created out_err."
    rm out_err
else
    echo "out_err does not exist."
fi
