#!/bin/bash

set -e

echo "Setting up VR24 B.Tech CSE repo structure..."

# Helper: create Unit-1..5 for theory subjects
create_units() {
    local base="$1"
    shift
    for sub in "$@"; do
        for u in {1..5}; do
            mkdir -p "$base/$sub/Unit-$u"
        done
    done
}

# Helper: create 01-Experiment .. NN-Experiment for labs
create_lab_exps() {
    local base="$1"
    local count="$2"
    for i in $(seq -f "%02g" 1 "$count"); do
        mkdir -p "$base/$i-Experiment"
    done
}

# ----------------------------------------------------------------------
# 1-1
# ----------------------------------------------------------------------
echo "[1-1] Theory"
create_units "1-1" MA Chemistry PPS BEE CAEG ECS
echo "[1-1] Labs"
for lab in Chemistry-Lab PPS-Lab BEE-Lab; do
    create_lab_exps "1-1/$lab" 10
done

# ----------------------------------------------------------------------
# 1-2
# ----------------------------------------------------------------------
echo "[1-2] Theory"
create_units "1-2" ODE Physics Workshop English EDC
echo "[1-2] Labs"
for lab in Python-Lab Physics-Lab English-Lab IT-Lab; do
    create_lab_exps "1-2/$lab" 8
done

# ----------------------------------------------------------------------
# 2-1
# ----------------------------------------------------------------------
echo "[2-1] Theory"
create_units "2-1" DE DS PnS CO Java
echo "[2-1] Labs"
for lab in DS-Lab Java-Lab DataVis-Lab; do
    create_lab_exps "2-1/$lab" 10
done

# ----------------------------------------------------------------------
# 2-2
# ----------------------------------------------------------------------
echo "[2-2] Theory"
create_units "2-2" DM BEFA OS DBMS SE
echo "[2-2] Labs"
for lab in OS-Lab DBMS-Lab Web-Lab; do
    create_lab_exps "2-2/$lab" 10
done

# ----------------------------------------------------------------------
# 3-1 (existing – only add missing Unit-*; labs already have 01-*)
# ----------------------------------------------------------------------
echo "[3-1] Updating units for existing theory"
create_units "3-1" DAA CN DevOps AECS DA NLP
echo "[3-1] Labs already exist, skipping"

# ----------------------------------------------------------------------
# 3-2
# ----------------------------------------------------------------------
echo "[3-2] Theory"
create_units "3-2" ML FLAT AI
echo "[3-2] Labs"
for lab in ML-Lab AI-Lab PE-III-Lab Mini-Project; do
    create_lab_exps "3-2/$lab" 10
done

# ----------------------------------------------------------------------
# 4-1
# ----------------------------------------------------------------------
echo "[4-1] Theory"
create_units "4-1" CNS CD
echo "[4-1] Labs"
for lab in CNS-Lab CD-Lab Project-I; do
    create_lab_exps "4-1/$lab" 10
done

# ----------------------------------------------------------------------
# 4-2
# ----------------------------------------------------------------------
echo "[4-2] Theory"
create_units "4-2" OB
echo "[4-2] Labs"
create_lab_exps "4-2/Project-II" 5

# ----------------------------------------------------------------------
# DSA
# ----------------------------------------------------------------------
echo "[DSA]"
for u in {1..5}; do
    mkdir -p "DSA/Unit-$u"
done

echo "Done."