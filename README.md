<div align="center">

# Generating CAD Code with Vision-Language Models for 3D Designs: |[Paper](https://arxiv.org/pdf/2410.05340)|
</div>

# Contribution
**1. CADCodeVerify approach:** a novel approach to iteratively verify and improve the design output of 3D objects generated from CAD code.<br>
**2. CADPrompt dataset:** the first benchmark for CAD code generation, consisting of 200 natural language prompts paired with expert-annotated scripting code for 3D objects to benchmark progress.


## 1. CADCodeVerify approach
We introduce CADCodeVerify, a novel approach to iteratively verify and improve 3D objects generated from CAD code. Our approach works by producing ameliorative feedback by prompting a Vision-Language Model (VLM) to generate and answer a set of validation questions to verify the generated object and prompt the VLM to correct deviations.

![Example Image](https://github.gatech.edu/kalrashedy3/CAD_Code_Generation/blob/main/CADCodeVerify.png?raw=true)

## 2. *CADPrompt* dataset
We introduce a new benchmark, *CADPrompt*, featuring 200 3D objects represented in the Standard Triangle Language (STL) format. Each sample includes: (I) the 3D object in STL format sourced from DeepCAD[1], (II) a language-based description of the 3D object, (III) the 3D object in OBJ format, detailing vertices, faces, and edges in standard 3D geometry, and (IV) a .json file containing the CAD commands and their parameters.

### Statistics of the *CADPrompt* dataset

The table below provides statistics for the *CADPrompt* dataset, including vertex and face counts of ground truth 3D objects, the lengths of language descriptions, and the corresponding Python code. The dataset is divided into simple and complex categories.

![Example Image](https://github.gatech.edu/kalrashedy3/CAD_Code_Generation/blob/main/Statistics.png?raw=true)

### Examples from CADPrompt

![Example Image](https://github.gatech.edu/kalrashedy3/CAD_Code_Generation/blob/main/Examples.png?s=100)



### Reference
[1] Wu, Rundi, Chang Xiao, and Changxi Zheng. "Deepcad: A deep generative network for computer-aided design models." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.


### Citation 
If this dataset contributes to your work, please consider citing the following publications.
```
@article{alrashedy2024generating,
  title={Generating CAD Code with Vision-Language Models for 3D Designs},
  author={Alrashedy, Kamel and Tambwekar, Pradyumna and Zaidi, Zulfiqar and Langwasser, Megan and Xu, Wei and Gombolay, Matthew},
  booktitle={International conference on learning representations (ICLR)},
  year={2025}
}

@inproceedings{wu2021deepcad,
  title={Deepcad: A deep generative network for computer-aided design models},
  author={Wu, Rundi and Xiao, Chang and Zheng, Changxi},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={6772--6782},
  year={2021}
}
```
