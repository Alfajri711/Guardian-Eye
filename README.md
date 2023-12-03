# Guardian Eyes: Automatic Detection of Dangerous Objects in Public Spaces

## Project Description
<b>Guardian Eyes: Automatic Detection of Dangerous Objects in Public Spaces</b> is a project created by <b>The Explorers</b> team as part of our final assignment for our independent study at Startup Campus. This project was inspired by the increasing incidents of crimes involving sharp weapons and even firearms. Consequently, we conceived the idea of developing an object detection system to identify and alert authorities about such hazardous objects.

## Contributor
| Full Name | Affiliation | Email | LinkedIn | Role |
| --- | --- | --- | --- | --- |
| Muhammad Asri Alfajri | Startup Campus, AI Track | muhammadasrialfajri@gmail.com | [link](https://www.linkedin.com/in/m-asri-a-495073262/) | Team Lead |
| Nanda Eka Suci Ramadan | Startup Campus, AI Track | nandaeka17.info@gmail.com | [link]() | Team Member |
| Iis Ismail | Startup Campus, AI Track | iis.ismail.te20@mhsw.pnj.ac.id | [link]() | Team Member |
| Elsa Indriani | Startup Campus, AI Track | elsadian704@gmail.com | [link](https://www.linkedin.com/in/elsa-indria/) | Team Member |
| Rifan Ahmad Rifandi | Startup Campus, AI Track | ahmadrifan931@gmail.com | [link](https://www.linkedin.com/in/rifan-ahmad-rifandi-15844421a/) | Team Member |
| Elfiede Nirwana Sihite | Startup Campus, AI Track | elfiedenirwanasihite@gmail.com | [link](https://www.linkedin.com/in/elfiede-nirwana-sihite-5873a8291/) | Team Member |
| Nicholas Dominic | Startup Campus, AI Track | nic.dominic@icloud.com | [link](https://linkedin.com/in/nicholas-dominic) | Supervisor |

## Setup
### Prerequisite Packages (Dependencies)
- altair==4.2.2
- attrs==23.1.0
- blinker==1.7.0
- cachetools==5.3.2
- certifi==2023.11.17
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- contourpy==1.2.0
- cycler==0.12.1
- Cython==3.0.6
- entrypoints==0.4
- filelock==3.13.1
- fonttools==4.44.3
- fsspec==2023.10.0
- gitdb==4.0.11
- GitPython==3.1.40
- idna==3.4
- importlib-metadata==6.8.0
- importlib-resources==6.1.1
- Jinja2==3.1.2
- jsonschema==4.20.0
- jsonschema-specifications==2023.11.1
- kiwisolver==1.4.5
- lapx==0.5.5
- markdown-it-py==3.0.0
- MarkupSafe==2.1.3
- matplotlib==3.8.2
- mdurl==0.1.2
- mpmath==1.3.0
- networkx==3.2.1
- numpy==1.26.2
- opencv-python==4.8.1.78
- packaging==23.2
- pandas==2.1.3
- Pillow==10.1.0
- protobuf==3.20.3
- psutil==5.9.6
- py-cpuinfo==9.0.0
- pyarrow==14.0.1
- pydeck==0.8.1b0
- Pygments==2.17.2
- Pympler==1.0.1
- pyparsing==3.1.1
- python-dateutil==2.8.2
- pytz==2023.3.post1
- PyYAML==6.0.1
- referencing==0.31.0
- requests==2.31.0
- rich==13.7.0
- rpds-py==0.13.1
- scipy==1.11.4
- seaborn==0.13.0
- semver==3.0.2
- six==1.16.0
- smmap==5.0.1
- streamlit==1.12.0
- sympy==1.12
- thop==0.1.1.post2209072238
- toml==0.10.2
- toolz==0.12.0
- torch==2.1.1
- torchvision==0.16.1
- tornado==6.3.3
- tqdm==4.66.1
- typing_extensions==4.8.0
- tzdata==2023.3
- tzlocal==5.2
- ultralytics==8.0.213
- urllib3==2.1.0
- validators==0.22.0
- watchdog==3.0.0
- zipp==3.17.0


### Environment
| | |
| --- | --- |
| CPU | Laptop Asus X441U I3-6600U |
| GPU | None |
| ROM | 128 SSD |
| RAM | 12 GB |
| OS | Windows 10 |

## Dataset
We conducted classification to determine the types of objects our project can detect. We identified six objects that can be recognized: Knife, Pistol, Axe, Crowbar, Hammer, and Scissors.
| ![Pistol](/assets/pistol.jpg "Pistol") | ![Knife](/assets/pisau.jpg "Knife") | ![Axe](/assets/axe.jpg "Axe") | ![Hammer](/assets/hammer.jpg "Hammer") | ![Crowbar](/assets/crowbar1%201.png "Crowbar") | ![Scissor](/assets/scissor.jpg "Scissor") |
| --- | --- | --- | --- | --- | --- |

- Link: https://...

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
Inform your model validation performances, as follows:
- For classification tasks, use **Precision and Recall**.
- For object detection tasks, use **Precision and Recall**. Additionaly, you may also use **Intersection over Union (IoU)**.
- For image retrieval tasks, use **Precision and Recall**.
- For optical character recognition (OCR) tasks, use **Word Error Rate (WER) and Character Error Rate (CER)**.
- For adversarial-based generative tasks, use **Peak Signal-to-Noise Ratio (PNSR)**. Additionally, for specific GAN tasks,
  - For single-image super resolution (SISR) tasks, use **Structural Similarity Index Measure (SSIM)**.
  - For conditional image-to-image translation tasks (e.g., Pix2Pix), use **Inception Score**.

Feel free to adjust the columns in the table below.

| model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | 1000 |  0.0001 | 32 | Adam | 0.093 | 88.34% | 84.15% | ... |
| vit_l_32 | 2500 | 0.00001 | 128 | SGD | 0.041 | 90.19% | 87.55% | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | 

![confusion_matrix](https://github.com/nandaeka02/the-explorers/assets/111878995/128ba3d6-b5f8-47dc-982c-f7f16b0cd660)

#### 2. Ablation Study
Any improvements or modifications of your base model, should be summarized in this table. Feel free to adjust the columns in the table below.

| model | layer_A | layer_B | layer_C | ... | top1_acc | top5_acc |
| --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | Conv(3x3, 64) x2 | Conv(3x3, 512) x3 | Conv(1x1, 2048) x3 | ... | 77.43% | 80.08% |
| vit_b_16 | Conv(3x3, 32) x3 | Conv(3x3, 128) x3 | Conv(1x1, 1028) x2 | ... | 72.11% | 76.84% |
| ... | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
Insert an image regarding your training and evaluation performances (especially their losses). The aim is to assess whether your model is fit, overfit, or underfit.
 
### Testing
Show some implementations (demos) of this model. Show **at least 10 images** of how your model performs on the testing data.

## Supporting Documents
### Presentation Deck
- Link: https://...

### Business Model Canvas
Provide a screenshot of your Business Model Canvas (BMC). Give some explanations, if necessary.

### Short Video
<video width="320" height="240" controls>
  <source src="assets/VideoTheExplorers.mp4" type="video/mp4">
</video>

## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://...
- Link: https://...
- Link: https://...

## Additional Comments
Provide your team's additional comments or final remarks for this project. For example,
1. ...
2. ...
3. ...

## How to Cite
If you find this project useful, we'd grateful if you cite this repository:
```
@article{
...
}
```

## License
For academic and non-commercial use only.

## Acknowledgement
This project entitled <b>"YOUR PROJECT TITLE HERE"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.

