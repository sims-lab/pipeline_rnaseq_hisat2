import pandas as pd

def get_sample_identifiers():
    """
    Get the identifiers of samples present in files.tsv.
    """
    config_files = pd.read_csv("config/files.tsv", sep="\t")
    ans = config_files["sample_id"].unique().tolist()
    return ans


def concatenate_files_fastq(index):
    '''
    Concatenate the list of FASTQ files in one column of files.tsv.

    Argument 'index' must be either 'fastq1' or 'fastq2'.
    '''
    config_files = pd.read_csv("config/files.tsv", sep="\t")
    ans = config_files[index].groupby(
        config_files['sample_id']
    ).aggregate(
        lambda x: " ".join(x)
    ).to_dict()
    return(ans)

def build_commands_hisat2(
        output_file_name_root, hisat2_threads, hisat2_genome, hisat2_options
    ):
    '''
    Build the list of commands to run HISAT2 for each sample.
    '''
    fastq1_list = concatenate_files_fastq('fastq1')
    fastq2_list = concatenate_files_fastq('fastq2')

    sample_ids = get_sample_identifiers()

    statements = []

    for sample_id in sample_ids:
        output_file_name = "{output_file_name_root}/{sample_id}.bam".format(**locals())
        fastqs1 = fastq1_list[sample_id]
        fastqs2 = fastq2_list[sample_id]

        statements.append(
        """
            hisat2
                --threads %(hisat2_threads)s
                -x %(hisat2_genome)s
                -1 %(fastqs1)s
                -2 %(fastqs2)s
                %(hisat2_options)s
                --summary-file %(output_file_name)s.log
            | samtools sort
                -@ %(hisat2_threads)s
                -o %(output_file_name)s
                -
            && samtools index
                %(output_file_name)s
        """ % locals()
    )

    return(statements)
