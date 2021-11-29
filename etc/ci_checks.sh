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
    results/hisat2/sample_01.bam
    results/hisat2/sample_02.bam
    results/hisat2/sample_01.bam.bai
    results/hisat2/sample_02.bam.bai
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
