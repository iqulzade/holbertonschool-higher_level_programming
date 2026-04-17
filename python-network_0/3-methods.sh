#!/bin/bash
# 3-methods
curl -sI "$1" | grep -i Allow | cut -d' ' -f2-