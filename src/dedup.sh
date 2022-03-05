#!/bin/bash

deduplicate_bismark  --bam  --paired  -o s_8_cell $1
deduplicate_bismark  --bam  --paired  -o s_epiblast $2
deduplicate_bismark  --bam  --paired  -o s_icm $3