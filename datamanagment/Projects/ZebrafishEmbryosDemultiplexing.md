(ZED_project)=

# Zebrafish Embryos Demultiplexing (ZED)

## Project summary

* **Status:** Ongoing
* **Goals:**
  * Use demultiplexing procedure to disentangle cells from different individual
  * Prove that the protocol works on Zebra fish embryo labeled cells
* **Contributors:** Cristina, Nicholas D. Leigh (Lund-Sweden)
* **Starting date:** Jan. 2023
* **Tools involved:** Linux machine (z-fishator), souporcell, sratools, samtools, picard, vireos synth tools, etc...
* **Project documentation** [Add link once created]

--------

## Project issues/caveats

* Pooling BAM files from different experiments taking forever (Fixed!)

--------

## Project TODO list

* Need SRA files from Loic's lab

--------

## Project History

* 2023
  * February
    * Able to reproduce the workflow in the [paper](https://www.biorxiv.org/content/10.1101/2022.09.22.508993v1)
      * Helped to improve the procedure in the paper fixing many bugs
    * Working version of BAM file pooling with Multithreading and removal of memory leaks
    * Working version of BAM pooling without VCF reference genome

  * January
    * Setup Z-Fishator for Cristina
