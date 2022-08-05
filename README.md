# AWR
This repo implements scripts based on the [AWR architecture](https://github.com/Elody-07/AWR-Adaptive-Weighting-Regression).
 to run inference and visualize results on depth images.

## Table of Contents
<details>
  <summary>Table of Contents</summary>
  
* [Getting Started](#getting-started)
    * [Conda Environment](#conda-environment)
    * [Requirements](#requirements)
    * [Installation](#installation)
    * [Build](#build)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#License)
</details>

## Getting Started
Please follow the instructions below to setup the project on your local system.

### Conda Environment
It is highly recommended to install a Miniconda environment before setting up the project. You can install Miniconda by following instructions from [here](https://docs.conda.io/en/latest/miniconda.html#installing). If you already have a Conda environment or do not want to install Miniconda, you can skip to the next section [Requirements](#requirements).

Create a new Conda environment called `awr`:
```
conda create -n awr python=3.7.0
```

To activate the environment:
```
conda activate awr
```

To deactivate the environment:
```
conda deactivate
```

For Python packages listed in the following [Requirements](#requirements) section, it is recommended to install them from Conda:
```
conda install <package-name>
```

### Requirements
The following dependencies are required to run the package:
- [Python3 (3.7)](https://www.python.org/downloads/)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html#installing)
- pytorch=1.4.0
```
conda install pytorch=1.4.0 -c pytorch
```
- opencv
```
pip install opencv-python
```


### Installation
Clone the repository:
```
git clone git@gitlab.com:telekinesis-ai/hand-pose-estimation/awr.git
```

## Usage
Run the package:
```
python hand_pose_awr.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Telekinesis AI]()
