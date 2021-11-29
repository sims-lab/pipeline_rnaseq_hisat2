"""
===========================
Pipeline template
===========================

.. Replace the documentation below with your own description of the
   pipeline's purpose

Overview
========

This pipeline computes the word frequencies in the configuration
files :file:``config.yml` and :file:`conf.py`.

Usage
=====

See :ref:`PipelineSettingUp` and :ref:`PipelineRunning` on general
information how to use cgat pipelines.

Configuration
-------------

The pipeline requires a configured :file:`pipeline.yml` file.
cgatReport report requires a :file:`conf.py` and optionally a
:file:`cgatreport.yml` file (see :ref:`PipelineReporting`).

Default configuration files can be generated by executing:

   python <srcdir>/pipeline_@template@.py config

Input files
-----------

None required except the pipeline configuration files.

Requirements
------------

The pipeline requires the results from
:doc:`pipeline_annotations`. Set the configuration variable
:py:data:`annotations_database` and :py:data:`annotations_dir`.

Pipeline output
===============

.. Describe output files of the pipeline here

Glossary
========

.. glossary::


Code
====

"""

###########
# Imports #
###########

from ruffus import *
import sys
import os
import cgatcore.experiment as E
from cgatcore import pipeline as P

#################
# Configuration #
#################

# Load parameters from config file(s).
# Files are parsed in order; later files override options defined in earlier files.
PARAMS = P.get_parameters(
    ["%s/config.yml" % os.path.splitext(__file__)[0], "../config.yml", "config.yml"]
)

############
# Workflow #
############


@follows(mkdir("results/qc/fastqc"))
@transform("data/*.fastq.gz", regex(r".*/(.*).fastq.gz"), r"results/qc/fastqc/\1.html")
def fastqc_on_fastq(infile, outfile):
    """
    Run FastQC on the FASTQ files.
    """

    statement = """
        fastqc 
            -o results/qc/fastqc
            --nogroup
            %(infile)s
            > %(outfile)s.log
            2>&1
    """

    P.run(statement, job_condaenv="pipeline_rnaseq_hisat2")


@follows(mkdir("results/reports/multiqc"))
@merge(fastqc_on_fastq, "results/reports/multiqc/fastqc.html")
def multiqc_on_fastqc(infiles, outfile):
    """
    Run MultiQC on the output of FastQC.
    """

    statement = """
        multiqc 
            -n fastqc.html
            -o results/reports/multiqc
            results/qc/fastqc
            > %(outfile)s.log
            2>&1
    """

    P.run(statement, job_condaenv="pipeline_rnaseq_hisat2")


@follows(mkdir("results/hisat2"))
@collate("data/*.fastq.gz", regex(r".*/(.*)_[12].fastq.gz"), r"results/hisat2/\1.bam")
def hisat2_on_fastq(infiles, outfile):
    """
    Run HISAT2 on the paired-end FASTQ files.
    """

    infile1, infile2 = infiles

    statement = """
        hisat2
            --threads %(hisat2_threads)s
            -x %(hisat2_genome)s
            -1 %(infile1)s
            -2 %(infile2)s
            %(hisat2_options)s
            --summary-file %(outfile)s.log
        | samtools sort
            -@ %(hisat2_threads)s
            -o %(outfile)s
            -
        && samtools index
            %(outfile)s
    """

    P.run(
        statement,
        job_condaenv="pipeline_rnaseq_hisat2",
        job_threads=PARAMS["hisat2_threads"],
    )


@follows(mkdir("results/qc/samtools/idxstats"))
@transform(
    hisat2_on_fastq,
    regex(r"results/hisat2/(.*).bam"),
    r"results/qc/samtools/idxstats/\1",
)
def idxstats_on_bam(infile, outfile):
    """
    Run `samtools idxstats` on the BAM files produced by HISAT2.
    """

    statement = """
        samtools idxstats
        %(infile)s
        > %(outfile)s
    """

    P.run(statement, job_condaenv="pipeline_rnaseq_hisat2")


@follows(fastqc_on_fastq, idxstats_on_bam)
def full():
    pass


##################
# Main execution #
##################


def main(argv=None):
    if argv is None:
        argv = sys.argv
    P.main(argv)


if __name__ == "__main__":
    sys.exit(P.main(sys.argv))
