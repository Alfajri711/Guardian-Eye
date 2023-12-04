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

- Link: https://drive.google.com/drive/folders/1eiRJh5qtRo5ASq4rr0PsrtP_tNlHK_Lh?usp=sharing

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
| model | epoch | learning_rate | batch_size | optimizer | val_precision | val_recall | val_mAP50 | val_mAP50-95 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLOv8 | 100 | 0.0003 | 16 | Adam | 95.2% | 92.9% | 95.8% | 77% |
| YOLOv8 | 150 | 0.0003 | 16 | Adam | 92.7% | 92% | 95.4% | 76.4% |
| YOLOv8 | 200 | 0.0003 | 16 | Adam | 93.3% | 91.6% | 94.2% | 77% |
| YOLOv8 | 250 | 0.0003 | 16 | Adam | ... | ... | ... | ... |
| YOLOv8 | 300 (Stop at 249) | 0.0003 | 16 | Adam | 94.7% | 92.8% | 95.2% | 77.7% |
| YOLOv8 | 100 | 0.001 | 16 | Adam | ... | ... | ... | ... |
| YOLOv8 | 150 | 0.001 | 16 | Adam | ... | ... | ... | ... |
| YOLOv8 | 200 | 0.001 | 16 | Adam | ... | ... | ... | ... |
| YOLOv8 | 250 | 0.001 | 16 | Adam | ... | ... | ... | ... |
| YOLOv8 | 300 | 0.001 | 16 | Adam | ... | ... | ... | ... |

Confusion Matrix:
![confusion_matrix](https://github.com/nandaeka02/the-explorers/assets/111878995/5c08ade4-edb1-47fe-b53e-ff45b06fb71e)

#### 2. Ablation Study
Backbone Improvement:
| model | modification | layer | before_mod | after_mod | precision | recall | mAP50 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| YOLOv8 | Backbone | ... | ... | ... | ... | ... | ... |

Head Improvement:
| model | modification | layer | before_mod | after_mod | precision | recall | mAP50 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| YOLOv8 | Head | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
Train Curve:
- Precision Curve:
![P_curve](https://github.com/nandaeka02/the-explorers/assets/111878995/be0b1e6f-8613-4099-8f2f-ea3c5d8ea500)

- Recall Curve:
![R_curve](https://github.com/nandaeka02/the-explorers/assets/111878995/93b458f0-7383-4803-aa09-532696392639)

- PR Curve:
![PR_curve](https://github.com/nandaeka02/the-explorers/assets/111878995/de7dfd6d-a8fa-460a-85bb-9cec04a8d0a1)

- F1 Curve:
![F1_curve](https://github.com/nandaeka02/the-explorers/assets/111878995/4924bb65-d466-47ea-a480-fd503b126471)

Val Curve:
- Precision Curve:
![P_curve (1)](https://github.com/nandaeka02/the-explorers/assets/111878995/5db18324-ed1b-4415-9c6c-c35d34355500)

- Recall Curve:
![R_curve (1)](https://github.com/nandaeka02/the-explorers/assets/111878995/c5259d71-4fda-472b-b2c0-01532f015825)

- PR Curve:
![PR_curve (1)](https://github.com/nandaeka02/the-explorers/assets/111878995/2558796e-ff18-4dae-9285-a0ec1d6f52b9)

- F1 Curve:
![F1_curve (1)](https://github.com/nandaeka02/the-explorers/assets/111878995/7fb777f4-8a30-45fb-8e4b-b80361cee521)

Train & Val Loss:
![results](https://github.com/nandaeka02/the-explorers/assets/111878995/f6d803b6-8093-4070-a147-fa0bdccd9e1f)

### Testing
1. Pisau:
   
![WhatsApp Image 2023-12-04 at 13 11 55](https://github.com/nandaeka02/the-explorers/assets/111878995/57bd7e4a-d3e7-4e95-afe1-e92fd7a9d87f)

2. Pistol:

![datates2](https://github.com/nandaeka02/the-explorers/assets/111878995/cc4508a4-5d68-4588-9389-456cd4eb073e)

3. Palu:

![WhatsApp Image 2023-12-04 at 13 12 07](https://github.com/nandaeka02/the-explorers/assets/111878995/868a5e19-d6e2-41d6-b623-ec13457d278d)

4. Gunting:

![WhatsApp Image 2023-12-04 at 13 12 19](https://github.com/nandaeka02/the-explorers/assets/111878995/a0296dcc-8803-4ad6-beed-5c9caa99d7ee)

5. Linggis:

![WhatsApp Image 2023-12-04 at 13 12 10](https://github.com/nandaeka02/the-explorers/assets/111878995/dfe45ea0-f8c3-4f63-8154-dd83da384d97)

6. Kapak:

![WhatsApp Image 2023-12-04 at 13 12 03](https://github.com/nandaeka02/the-explorers/assets/111878995/1b7f2105-2b5a-4e7f-8dc4-dc216564dfb8)

7. Mix Pistol x Pisau:

![Detect Mix 1](https://github.com/nandaeka02/the-explorers/assets/111878995/b4bea8d8-f370-41ab-92b9-6d06f1772363)

8. Mix Pistol x Kapak:

![Detect Mix 2](https://github.com/nandaeka02/the-explorers/assets/111878995/6eb15855-d076-436c-b518-8eaf00e71e2c)

9. Mix Gunting x Linggis:

![Detect Mix 3](https://github.com/nandaeka02/the-explorers/assets/111878995/c64c7e26-a313-461f-aa74-d4798b1bd2d8)

10. Mix Kapak x Palu:

![Detect Mix 4](https://github.com/nandaeka02/the-explorers/assets/111878995/fb0bcb10-a489-49dd-b22a-4be88dcf2874)

- Link: https://drive.google.com/drive/folders/1yeLHSicb5bEEm1r6uWRfUQXl_Zr09Bdq?usp=drive_link

## Supporting Documents
### Presentation Deck
![PPT](https://github.com/nandaeka02/the-explorers/assets/111878995/47c36528-1fc1-4c87-8ee6-aa0f19c4aa54)

- Link: https://drive.google.com/drive/folders/1BrpHt4gspyVullIAzbdHZwiV_Jzyrjws?usp=drive_link

### Business Model Canvas
<img width="960" alt="SSBMC1" src="https://github.com/nandaeka02/the-explorers/assets/111878995/60be4c48-9cf2-40b0-b293-6eb1d4e95c28">
<img width="960" alt="SSBMC2" src="https://github.com/nandaeka02/the-explorers/assets/111878995/63407f9c-c9c1-4f43-928a-cd9497e95a23">
- Link: https://docs.google.com/document/d/1ObH4PCTKWE6KUfARezBSU31ebE5hh975/edit?usp=sharing&ouid=108973949485557616792&rtpof=true&sd=true

### Short Video
<video width="320" height="240" controls>
  <source src="assets/VideoTheExplorers.mp4" type="video/mp4">
</video>
https://drive.google.com/drive/folders/12_8-MZmSEBr9rrZo6Y5iMK59ajVhZpej?usp=drive_link

## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://github.com/ultralytics/ultralytics
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
This project entitled <b>"Guardian Eyes: Automatic Detection of Dangerous Objects in Public Spaces"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.

