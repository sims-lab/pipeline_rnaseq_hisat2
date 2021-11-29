expected_files=(
    results/qc/fastqc/sample_01_1.html
    results/qc/fastqc/sample_01_2.html
    results/qc/fastqc/sample_01_1.html
    results/qc/fastqc/sample_01_2.html
    results/qc/fastqc/sample_01_1.zip
    results/qc/fastqc/sample_01_2.zip
    results/qc/fastqc/sample_02_1.zip
    results/qc/fastqc/sample_02_2.zip
    results/qc/multiqc/fastqc.html
    results/qc/multiqc/fastqc_data/multiqc_fastqc.txt
    results/qc/multiqc/fastqc_data/multiqc_general_stats.txt
    results/qc/multiqc/fastqc_data/multiqc_sources.txt
    results/hisat2/sample_01.bam
    results/hisat2/sample_02.bam
    results/hisat2/sample_01.bam.bai
    results/hisat2/sample_02.bam.bai
    results/qc/samtools/idxstats/sample_01
    results/qc/samtools/idxstats/sample_02
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
