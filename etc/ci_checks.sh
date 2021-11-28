expected_files=(
    results/fastqc/sample_01_1_fastqc.html
    results/fastqc/sample_01_2_fastqc.html
    results/fastqc/sample_01_1_fastqc.html
    results/fastqc/sample_01_2_fastqc.html
)

for file in "${expected_files[@]}"
do
    if [ -f "$file" ]; then
        echo "[OK] $file"
    else
        echo "[FAIL] $file"
        exit 1
    fi
done
