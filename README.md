[![CI](https://github.com/sims-lab/pipeline_rnaseq_hisat2/actions/workflows/build.yml/badge.svg)](https://github.com/sims-lab/pipeline_rnaseq_hisat2/actions/workflows/build.yml)

# pipeline_rnaseq_hisat2

Pipeline for processing paired-end RNA-sequencing using [cgatcore][link-cgatcore] and [HISAT2](http://www.ccb.jhu.edu/software/hisat/index.shtml).

[link-cgatcore]: https://github.com/cgat-developers/cgat-core

## Usage

- [ ] Create a new repository from this one, using the `Use as template` button on [GitHub](https://github.com/sims-lab/pipeline_rnaseq_hisat2).
  + That way, your new repository starts its own commit history, where you can record your own changes!
  + Only fork this repository if you wish to contribute updates to the template pipeline itself.
- [ ] Clone the new repository to the computer where you wish to run the pipeline.
- [ ] Create a Conda environment named `pipeline_rnaseq_hisat2` using the file `envs/pipeline.yml`. 
- [ ] Create symbolic links to your input FASTQ files, in the subdirectory `data/`.
- [ ] Edit the configuration of the pipeline as needed, in the file `config.yml`.
- [ ] Run the pipeline!
  + On a High-Performance Computing (HPC) cluster, `python pipeline.py make full -v 5`, to use the Distributed Resource Management Application API (DRMAA).
  + On a local machine `python pipeline.py make full -v 5 --local`.
