# Pipeline Cristina

This is the documentation about Cristina's pipeline.
We login to a linux machine we have in the lab `ssh -X <username>@128.178.192.147`

running cellranger
```shell
cellranger count --id=run_count_zf_7SS_r5_1 --fastqs=/home/cristinaloureiro/data/zf_7SS_r5_1 --sample=zf_7ss_r5_1 --localcores=8 --localmem 15 --
transcriptome=/home/clement/Danio.rerio_genome
```

:::{admonition} Prerequisites
:class: prereq
Before starting with this project, you should make sure that you have `anaconda` installed on your system as we will use it to define a specific virtual environment.
:::

```{eval-rst}
.. toctree::
    :hidden:
    :caption: Contents:

    Resynchronization/README.md
    Early-oscillations/README.md
```
