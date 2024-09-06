# ANPR TRAK

##### For more details, don't hesitate to read the file `ANPR_REPORT.PDF`.

## Introduction

In my continuous learning journey, I often choose the challenging path. For this project, I decided to delve into some of the most complex and powerful APIs in the domain, even though I don't fully understand all the principles and mechanisms yet. This project focuses on two crucial concepts: detection and recognition. The goal is to create an application capable of determining the location and even the text of a car's license plate from an image or video frames. While this may seem simple, it is quite complex, at least for me.

I decided to use two models. The first model is the [Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) from the [TensorFlow](https://www.tensorflow.org/) framework. This allowed me to explore some of their features and learn the main functionalities of their API. I was able to fine-tune their object detection model for my classification problem, resulting in a high-quality model for car plate detection that predicts the position of the plate within an image. The second model uses the YOLOv3 architecture, trained on a large dataset created by students from Université Mohammed VI Polytechnique (UM6P).

## Test the Application Interface

To run the application interface, execute the following command:

```bash
python .\mainAnprApp.py
```

## Setup

To test the model, you can use the `TRAK_ANPR_Test.ipynb` notebook directly, or explore the entire object detection process in the `TRAK_ANPR.ipynb` notebook. Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/hamza-el-filali-en1999/) if you have any questions.

## Steps

These steps will help you prepare the environment to easily explore the project.

### Loading the Environment

**Step 1.** Clone this repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

**Step 2.** Create a new virtual environment:

```bash
python -m venv anprenv
```

**Step 3.** Activate your virtual environment:

```bash
source anprenv/bin/activate  # Linux
.\anprenv\Scripts\activate   # Windows
```

**Step 4.** Install dependencies and add the virtual environment to the Python Kernel:

```bash
python -m pip install --upgrade pip
pip install ipykernel
python -m ipykernel install --user --name=anprenv
```

**Step 5.** Open the Jupyter Notebook interface by typing this command in the terminal while your environment is activated:

```bash
jupyter notebook
```

- Ensure you change the kernel to the virtual environment.

**Step 6.** Install all requirements from the `requirements.txt` file:

```bash
pip install -r .\models\requirements.txt
```

**Step 7.** Run all cells in the notebook `TRAK_ANPR.ipynb`. Ensure you get the correct results at the end. During this process, the notebook will install TensorFlow Object Detection and test it. You should receive a notification indicating that the API has installed successfully.

### Application Testing

To run the main desktop application, use this command:

```bash
python .\mainAnprApp.py
```

**Step 8.** If you encounter installation errors, refer to the [Error Guide](https://github.com/nicknochnack/TFODCourse/blob/main/Error%20Guide.md) in this folder.

**Step 9.** Navigate to the evaluation directory and open TensorBoard with the following commands:

```bash
cd Tensorflow/workspace/models/my_ssd_mobnet/eval
tensorboard --logdir=.
```

TensorBoard will be accessible through your browser, allowing you to view metrics such as mean Average Precision (mAP) and Recall.
