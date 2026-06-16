#!/bin/bash

build_generator() {
    docker build -t csv-generator -f generator/Dockerfile generator/
}

run_generator() {
    mkdir -p data
    docker run --rm -v $(pwd)/data:/data csv-generator
}

create_local_data() {
    mkdir -p local_data
    python3 generator/generate.py local_data
}

build_reporter() {
    docker build -t csv-reporter -f reporter/Dockerfile reporter/
}

run_reporter() {
    if [ ! -f data/data.csv ]; then
        echo "Error: data/data.csv not found"
        exit 1
    fi
    docker run --rm -v $(pwd)/data:/data csv-reporter
}

structure() {
    find . -type f -not -path "*/\.*" -not -path "*/__pycache__/*" -not -path "*/node_modules/*" | sort | sed 's|^\./||'
}

clear_data() {
    rm -f data/*.csv data/*.html
}

inside_generator() {
    docker run --rm -v $(pwd)/data:/data csv-generator ls -la /data
}

inside_reporter() {
    docker run --rm -v $(pwd)/data:/data csv-reporter ls -la /data
}

case "$1" in
    build_generator|run_generator|create_local_data|build_reporter|run_reporter|structure|clear_data|inside_generator|inside_reporter)
        $1
        ;;
    *)
        echo "Usage: $0 {build_generator|run_generator|create_local_data|build_reporter|run_reporter|structure|clear_data|inside_generator|inside_reporter}"
        exit 1
        ;;
esac