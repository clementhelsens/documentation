# Sequencing analysis workflow

In this documentation we review the analysis of the sequencing data.

## Project summary

* **Status:** Ongoing
* **Goals:**
  * Use demultiplexing procedure to disentangle cells from different individual
  * Find regions of the genome
  * Prove that the protocol works on Zebra fish embryo labeled cells
* **Contributors:** Clement Helsens, Cristina Loureiro
* **Starting date:** Jan. 2023
* **Tools involved:** Linux machine, cellranger, souporcell, sratools, samtools, picard, vireos synth tools, etc...

## Raw Data Availability

All the RAW data are located on our nas-rcp storage:

```shell
smb://sv-nas1.rcp.epfl.ch/UPOATES-sandbox1/data/sequencing/
```

On z-fishator machine, it is mounted in:
```shell
/mnt/nas-rcp/
```

## Workflow

### Cellranger

`cellranger-7.1.0` and `cellranger-arc-2.0.2` are installed on z-fishator machine and can be used by simply modifying your `PATH`:

```shell
export PATH=/usr/local/share/yard/apps/cellranger-7.1.0:$PATH
export PATH=/usr/local/share/yard/apps/cellranger-arc-2.0.2:$PATH
```

The latest version of cellranger can be accessible from [this link](https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest)

Running `cellranger count` should look like:

```shell
cellranger count --fastqs=/mnt/nas-rcp/data/sequencing/scRNA-seq/wildtype/fastq/ —-sample=replicate<X> —-localcores=8 —-localmem=15 --id=replicate<X> --transcriptome=/usr/local/share/yard/data/Danio.rerio_genome/ 
```

replace `<X>` by the appropriate replicate number.

