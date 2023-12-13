# Italian Marriage Document Handwriting Detection
Our collaborative efforts led to the development of a deep-learning model based on YOLOv8. This model seamlessly generates a virtual spreadsheet, effectively alleviating the human workload associated with transcribing intricate Italian marriage documents. Its primary goal is to amplify the availability of invaluable data for genealogical research purposes.

Leveraging a curated dataset comprising historical marriage documents sourced from Caiazzo, Italy, dating between 1875-1889, retrieved from Ancestry.com, our model has been trained to identify key machine-printed text and extract the handwriting associated with it. By utilizing this historical dataset, we aim to change the accessibility and ease of exploring genealogical data.

## Packages

This project uses
- Ultralytics v8.0.20
- pyyaml
- roboflow

## Usage Guide for Python Notebook

### Instructions:
1. **Access Notebook:** Go to the `notebook_code` folder.
2. **Test Documents:** Place test documents in the `test_image_folder1`. (*Note: Pre-existing test images are available.*)
3. **Run Script:** Execute the `MarriageRecords.ipynb` file.
4.  **Final Output:** Retrieve the generated final spreadsheet image from the `finalvConcatImages` folder.

### Quick Steps:
1. **Location:** `notebook_code/MarriageRecords.ipynb`
2. **Test Documents:** `test_image_folder1` (contains sample images)
3. **Output:** `finalvConcatImages` folder (final spreadsheet image)

## Usage Guide for Tkinder UI

### Instructions:
1. **Access Notebook:** Go to the `tkinter_UI` folder.
2. **Run Script:** Execute the `MarriageRecords.ipynb` file.
3. **Test Documents:** A window will pop up to upload images. Once all images are uploaded close the window.
4.  **Final Output:** Retrieve the generated final spreadsheet image from the `finalvConcatImages` folder.

### Quick Steps:
1. **Location:** `tkinter_UI/MarriageRecords_UI.ipynb`
2. **Test Documents:** `test_image_folder` 
3. **Output:** `finalvConcatImages` folder (final spreadsheet image)

## Usage Guide for React UI
In development, to come soon!

## Contributors

- [Taylor Schermer](https://github.com/tschermer02)
- [Joel Nash](https://github.com/jxnash)
- [Jade Martinez](https://github.com/jademartinezz)
- [Lyla Wortham](https://github.com/Lyla009)
- [Lethicia Calderon](https://github.com/ticiacal)
  

