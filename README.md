# ANPR TRAK

## introduction
Always in my learning process . I choose the hard way, for this project I decide to deep dive in some of the most complecated and pwerfull api's in the domaine eaven if I still don't understand the hole principales and mechanismes of the field . So here we have tow crucial concepts Detection and recognition, in order to create an application capable of detrmine the place and eaven more the text of the car plate number from an image or a video ( frames ) . this looks simple but in depth it's very complecated at least for me. In my case I decided to use tow models , The first model is the <a href="">object_detection</a> api from the <a href="">TensorFlow</a> framework so I have the chance to explore some of the features on their <a href="">documentation in github</a> and learn some of the main functionalities of their api , with it I was able to figure out how finetuning done to their object detection model on my own classification problem in result I get a high quality model for car plate detection that predict the position of the plate with in an image . The second model uses YoloV3 architecture trained on a big dataset created by some UM6P students ( Université Mohammed VI Polytechnique ).

## Setup


<p>To test the model you can use directly the TRAK_ANPR_Test.ipynb or you can see the hole process of object detection on this notebook TRAK_ANPR.ipynb. And this is My <a href="https://www.linkedin.com/in/hamza-el-filali-en1999/">LinkedIn Profile</a> if you have any questions.
<img src="https://i.imgur.com/SaUSstN.png">

## Steps
this steps helps you prepare the environement to easly explore the project .
<br />
<b><h3> Loading the environement : </h3></b>
<br />
<b>Step 1.</b> Clone this repository: __My Repo__
<br/><br/>
<b>Step 2.</b> Create a new virtual environment 
<pre>
python -m venv anprenv
</pre> 
<br/>
<b>Step 3.</b> Activate your virtual environment
<pre>
source anprenv/bin/activate # Linux
.\anprenv\Scripts\activate # Windows 
</pre>
<br/>
<b>Step 4.</br> Install dependencies and add virtual environment to the Python Kernel
<pre>
python -m pip install --upgrade pip
pip install ipykernel
python -m ipykernel install --user --name=anprenv
</pre>
<br/>
<b>Step 5.</br>Open jupyter notebooks interface by typing this commande in the cmd while your environment is activated
<pre>
jupyter notebook 
</pre>
- ensure you change the kernel to the virtual environment as shown below .
<img src="https://i.imgur.com/V8eBDTP.png"> 
<br/>
<b>Step 6.</b>At this point you need to install all requirements in the file requirements.txt . 
<pre>
pip install -r .\models\requirements.txt
</pre>

<b>Step 7.</b>  Run all cells In the notebook *TRAK_ANPR.ipynb* <br/>
Make sure you get at the end a result as the image below .
<br/><br/>
<img src="https://i.imgur.com/V8eBDTP.png"> 
Because during this process the Notebook will install Tensorflow Object Detection and then test it. You should ideally receive a notification indicating that the API has installed successfully .
<img src="https://i.imgur.com/V8eBDTP.png"> 
</pre>
<b><h3> Application Testing : </h3></b>
<br />To run the main desktop application application use this command 
<pre>
python .\mainAnprApp.py<br/>
<b>Step 8.</b> So 
<img src="https://i.imgur.com/FSQFo16.png">
If not, resolve installation errors by referring to the <a href="https://github.com/nicknochnack/TFODCourse/blob/main/">Error Guide.md</a> in this folder.
<br /> <br/>
<b>Step 9.</b>  
<img src="https://i.imgur.com/K0wLO57.png"> 
<br />
<b>Step 10.</b> 
<pre> cd Tensorlfow/workspace/models/my_ssd_mobnet/eval</pre> 
and open Tensorboard with the following command
<pre>tensorboard --logdir=. </pre>
Tensorboard will be accessible through your browser and you will be able to see metrics including mAP - mean Average Precision, and Recall.
<br />