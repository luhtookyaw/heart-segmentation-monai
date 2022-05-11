# 3D Heart Segmentation with MONAI

## Resulting predictions of training 700 epochs on 15 samples, each with 64 slices

<div>
    <img src="./images/heart_segmentation_0.png" alt="Heart Segmentation Image Zero" style="border-radius: 5px;"/>
</div><br>

<div>
    <img src="./images/heart_segmentation_1.png" alt="Heart Segmentation Image One" style="border-radius: 5px;"/>
</div><br>

<div>
    <img src="./images/heart_segmentation_2.png" alt="Heart Segmentation Image Two" style="border-radius: 5px;"/>
</div>
<br>

## Training and Validating over Dice Loss and Dice Metric

<div>
    <img src="./images/train_versus_test.png" alt="Dice Loss and Dice Metric" style="border-radius: 5px;"/>
</div>
<div style="background: #ba1454; padding: 5px; border-radius: 10px"> 
    In medical imaging, there is no such a thing as perfect as other computer vision applications.
    This result is already good enough for training over only 15 samples. That can be a lot more better if there is more data and computational resources which 3D imaging takes abundance. This project is for fun only and not to be used in reallife scenerios. 
</div>


<h3>Train and Test in Colab<h3>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luhtookyaw/heart-segmentation-monai/blob/main/Training_and_Testing.ipynb)

<a href="https://monai.io">
    <img src="https://monai.io/assets/img/MONAI-logo_color.png" alt="MONAI"/>
</a><br/>

<a href="http://medicaldecathlon.com/">
    Download Datasets here
</a>