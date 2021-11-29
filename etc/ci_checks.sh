expected_files=(
    results/fastqc/sample_01_1_fastqc.html
    results/fastqc/sample_01_2_fastqc.html
    results/fastqc/sample_01_1_fastqc.html
    results/fastqc/sample_01_2_fastqc.html
    results/fastqc/sample_01_1_fastqc.zip
    results/fastqc/sample_01_2_fastqc.zip
    results/fastqc/sample_02_1_fastqc.zip
    results/fastqc/sample_02_2_fastqc.zip
    results/multiqc/fastqc.html
    results/multiqc/fastqc_data/multiqc_fastqc.txt
    results/multiqc/fastqc_data/multiqc_general_stats.txt
    results/multiqc/fastqc_data/multiqc_sources.txt
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
