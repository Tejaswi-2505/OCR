# Optical Character Recognisition

This project is an Optical Character Recognition (OCR) application built using Python, Kivy, OpenCV, and Tesseract. It allows users to extract text from images and display the results in a user-friendly interface.

## Table of Contents

- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Installation Instructions

Follow the steps below to set up the environment for this project.

### 1. Python Installation

Make sure Python is installed on your computer. You can download it from the official [Python website](https://www.python.org/downloads/) and choose the suitable version for your operating system. After installation, verify that Python is installed by running the following command in your command prompt or terminal:

bash
python --version


### 2. OpenCV Installation

To install OpenCV, use the following command in your command prompt or terminal:

bash
pip install opencv-python


### 3. PIL Library Installation

To install the Pillow library (PIL), run:

bash
pip install Pillow


### 4. Tesseract-OCR Installation

To install Tesseract, download the appropriate version for your operating system from [this link](https://github.com/UB-Mannheim/tesseract/wiki). Follow the installation instructions provided on the page.

### 5. Pytesseract Installation

Once Tesseract is installed, you can install the Pytesseract library using:

bash
pip install pytesseract


### 6. Kivy Installation

To install Kivy and its dependencies, first update pip and setuptools. Run the following commands:

bash
python -m pip install --upgrade pip wheel setuptools
python -m pip install kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer


Then, install Kivy itself:

bash
pip install kivy


### Notes

- Ensure you run these commands in the terminal or command prompt.
- Depending on your operating system, some steps may differ slightly.

## Usage

To run the application, navigate to the project directory in your command prompt or terminal and execute:

bash
python OCRApp.py



## Dependencies

This project requires the following Python libraries:

- opencv-python
- Pillow
- pytesseract
- kivy

These dependencies will be installed automatically when you run the installation commands above.
