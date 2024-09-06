# ANPR TRAK

##### For more details, please refer to `ANPR_REPORT.PDF`.

## Introduction

In my continuous learning journey, I often choose challenging paths. This project involves exploring complex and powerful APIs to develop an application capable of detecting and recognizing car license plates from images or video frames. The project focuses on two crucial concepts: detection and recognition.

I utilized two models for this task. The first model is the [Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) from the [TensorFlow](https://www.tensorflow.org/) framework, which I fine-tuned for car plate detection. The second model employs the YOLOv3 architecture, trained on a dataset created by students from Université Mohammed VI Polytechnique (UM6P).

## Test the Application Interface

To run the application interface, execute:

```bash
python mainAnprApp.py
```

## Setup

You can test the model using the `TRAK_ANPR_Test.ipynb` notebook or explore the full object detection process in `TRAK_ANPR.ipynb`. Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/hamza-el-filali-en1999/) for any questions.

## Environment Setup

Follow these steps to prepare your environment:

### Step 1: Clone the Repository

Clone this repository and navigate into it:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create and Activate a Virtual Environment

Create a new virtual environment and activate it:

```bash
python -m venv anprenv
```

- **Activate on Linux/MacOS:**

  ```bash
  source anprenv/bin/activate
  ```

- **Activate on Windows:**

  ```bash
  .\anprenv\Scripts\activate
  ```

### Step 3: Install Dependencies

Upgrade pip and install necessary packages:

```bash
python -m pip install --upgrade pip
pip install -r models/requirements.txt
```

### Step 4: Set Up Jupyter Notebook

Install the IPython kernel and add the virtual environment to Jupyter:

```bash
pip install ipykernel
python -m ipykernel install --user --name=anprenv
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

- Ensure you select the `anprenv` kernel in Jupyter.

### Step 5: Run the Notebooks

Run all cells in `TRAK_ANPR.ipynb` to ensure the setup is correct. The notebook will install TensorFlow Object Detection and test it. You should see a success notification.

## Application Testing

To run the main desktop application, use:

```bash
python mainAnprApp.py
```

If you encounter installation errors, refer to the [Error Guide](https://github.com/nicknochnack/TFODCourse/blob/main/Error%20Guide.md).

## Monitoring with TensorBoard

Navigate to the evaluation directory and start TensorBoard:

```bash
cd Tensorflow/workspace/models/my_ssd_mobnet/eval
tensorboard --logdir=.
```

Access TensorBoard through your browser to view metrics such as mean Average Precision (mAP) and Recall.
