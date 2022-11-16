# Resynchronization

This is the documentation about resynchronization, github project available [here](https://github.com/EPFL-STD/Resynchronization).

## EXPLAIN WHAT IT DOES!!


## Setup/Installation

Before running, make sure you have achieved the following steps:

 1. Have cloned the repository [Resynchronization](https://github.com/EPFL-STD/Resynchronization)
 2. Create a dedicated virtual environment on top of python 3.7, for example with conda: `conda create -n <mydummyenv> python=3.7`, and activate it `conda activate <mydummyenv>`
 3. Install all the extra packages listed in the [requirements](https://github.com/EPFL-STD/Resynchronization/blob/main/requirements.txt) `pip3 install -r requirements.txt`
 4. **Note of caution**: make sure that the python version used to install the extra packages with `pip3` is the one of the virtual environment. You can check that with `which pip3` and it should return something like `/<mypathtoinstall>/anaconda3/envs/<mydummyenv>/bin/pip3`. If that is not the case, you might have to properly add it at the beginning of your `PATH`

## Running

To run the code you need to prepare a configuration file such as the one below, where you need to configure a few things...(To be detailed)

:::{admonition} Show example
:class: toggle
```python
input_directory = 'csv/'
list_name_datasets = ['DAPT1_os_20210331',
                      'DAPT1_ns_20210324',
                      'DMSO1_os_20210323',
                      'DMSO_ns_20220803',
                      ]

list_labels = ['DAPT 1 - Defective boundary',
               'DAPT 2 - Defective boundary',
               'DMSO 1',
               'DMSO 2',
                      ]

dist_neighbors = 15

n_nearest_neighbors = 6

save_to_folder = 'Figures/myConfig_dn{}_nnn{}'.format(dist_neighbors,n_nearest_neighbors)


condition_names = ['Anterior No', 'Anterior Yes', 'Posterior No', 'Posterior Yes', ]

condition_names_label = ['Correct - Anterior', 'Defective – Anterior',  ' Correct - Posterior', 'Defective - Posterior', ]

condition = 'AP + defect'

save_formats=['pdf','png']

index_defect = 2

dt = 2
ind_noto_static = 0

color_1 = 'olive'
color_2 = 'navy'
color_map = 'hsv'
color_map2 = 'hot'
alpha_value = 0.75
my_color_map =['sienna',  'royalblue', 'goldenrod', 'deepskyblue', 'lime', 'hotpink', 'bisque','limegreen', ]


time_lim_min_tracking = [130,
                         85,
                         97,
                         23,
                         ]
time_lim_max_tracking = [218,
                         230,
                         175,
                         106,
                         ]

time_lim_min = [270,
                210,
                185,
                50,
                ]
time_lim_max = [400,
                340,
                350,
                140,
                ]

alpha_shift = [5,
               1.6,
               0,
               0,
               ]
```
:::


Then you simply need to run like
```shell
 python bin/vortex_analysis.py config/testConfig.py
```

This will produce plots under the directory configure with the variable `save_to_folder` in the configuration file.

## Looking at the results

Using the [gallery](https://github.com/EPFL-STD/utils/tree/main/gallery) tool, you can produce browsable results, for example running:
```shell
python gallery.py <pathtotheplots>
```
will produce in `<pathtotheplots>` `index.html` that you can open with your browser. Alternatively, you can also deploy this on a server.
