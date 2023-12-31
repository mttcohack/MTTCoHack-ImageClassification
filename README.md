# MTT CoHack Challenge : Car Image Classification

## Introduction

In this challenge, we're diving into the whole process of creating an image classification app. You'll learn how to train and test an image classification model, plus we'll show you how to put that model into a simple web app using Flask.

![image](./images/image.png)

## Requirements

- You will need to have **git** installed in your computer, so that you can clone this repository to use the application code prepared for you.
```
git clone https://github.com/mttcohack/MTTCoHack-ImageClassification.git
```
- You will need to have **python** installed in your computer.
- You can also use your computer base environment for development, but as a best practice we can also create a python virtual environment. Navigate to your project folder and then execute this code (Be sure to replace {name-of-your-environment} with the name of your virtual environment.)
```
python -m venv {name-of-your-environment}
{name-of-your-environment}/Scripts/Activate #To activate your virtual env
```
- You will need to install the python libraries included in the *requirements.txt* file in the virtual environment or computer where you plan on developing the application using the following code.

```
pip install -r requirements.txt
```

- You will need an Azure subscription where you will be provisioning the services you will be using to train and test the model and as well as deploy the model.

## Learning Objectives

This hack will help you learn:

- You will learn to tag images using Azure AI services.
- You will delve into the world of model training and testing, all thanks to Azure AI services.
- You will discover the ropes of deploying that model into a straightforward web application.

## Success Criteria

### Challenge 1

- Create a project in Azure AI services to train your custom model for car classfication based on color.
- Train one model for classifying cars by color and test the model using the test images provided. The training data can be downloaded from [here](https://sakhdavd.blob.core.windows.net/cohack/car-color.zip).
- Create another project and train another model for classifying cars by the model of the car and test the model using the test images provided. The training data can be downloaded from [here](https://sakhdavd.blob.core.windows.net/cohack/car-make.zip).
- Test images can be found [here](https://sakhdavd.blob.core.windows.net/cohack/car-test-images.zip).
- Develop a simple web application to predict images using the models created in the azure service.

#### Resources

- [What is Azure AI Vision?](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview)
- [What is Vision Studio?](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-vision-studio)
- [What is Custom Vision?](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)
- [Test and retrain a model with Custom Vision Service](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/test-your-model)
- [Call the prediction API](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/use-prediction-api)
- [Custom Vision frequently asked questions](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/faq)
- [Create a virtual environment for your project](https://docs.python.org/3/library/venv.html)
- [Post HTTP Request using python requests function](https://www.w3schools.com/PYTHON/ref_requests_post.asp)


![image](./images/result.png)

### [Optional] Challenge 2

- Train another model which classifies both the color label and the make label using one model. The training data can be downloaded from [here](https://sakhdavd.blob.core.windows.net/cohack/car-color-make.zip).
- You can use the same test [images](https://sakhdavd.blob.core.windows.net/cohack/car-test-images.zip) from challenge 1.
- Deploy the flask application into Azure App service.

#### Resources

- [Quickstart: Deploy a Python (Django or Flask) web app to Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli)
