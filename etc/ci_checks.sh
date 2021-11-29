expected_files=(
    results/qc/fastqc/sample_01_1_fastqc.html
    results/qc/fastqc/sample_01_2_fastqc.html
    results/qc/fastqc/sample_01_1_fastqc.html
    results/qc/fastqc/sample_01_2_fastqc.html
    results/qc/fastqc/sample_01_1_fastqc.zip
    results/qc/fastqc/sample_01_2_fastqc.zip
    results/qc/fastqc/sample_02_1_fastqc.zip
    results/qc/fastqc/sample_02_2_fastqc.zip
    results/reports/multiqc/fastqc.html
    results/reports/multiqc/fastqc_data/multiqc_fastqc.txt
    results/reports/multiqc/fastqc_data/multiqc_general_stats.txt
    results/reports/multiqc/fastqc_data/multiqc_sources.txt
    results/hisat2/sample_01.bam
    results/hisat2/sample_02.bam
    results/hisat2/sample_01.bam.bai
    results/hisat2/sample_02.bam.bai
    results/qc/samtools/idxstats/sample_01
    results/qc/samtools/idxstats/sample_02
    results/qc/samtools/flagstat/sample_01
    results/qc/samtools/flagstat/sample_02
    results/qc/picard/CollectAlignmentSummaryMetrics/sample_01
    results/qc/picard/CollectAlignmentSummaryMetrics/sample_02
    results/qc/picard/CollectInsertSizeMetrics/sample_01
    results/qc/picard/CollectInsertSizeMetrics/sample_02
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
