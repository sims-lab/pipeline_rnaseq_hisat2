expected_files=(
    results/fastqc/sample_01_1_fastqc.html
    results/fastqc/sample_01_2_fastqc.html
    results/fastqc/sample_01_1_fastqc.html
    results/fastqc/sample_01_2_fastqc.html
    dummy_fail
)

for file in $expected_files
do
    if [ ! -f $file ]; then
        echo "File not found: $file"
        exit 1
    fi
done
