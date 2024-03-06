#  Deeplearning based filebrowser (WIP):

## image captioning demo 
![demo for captioning](./filebrowser_demo.mp4)

- aim is to provide a better search in filebrowsers when the filebrowsere names are cryptic and it is hard to find an image or a document based on the standard search
## todo
- make ui
- make easily deoployable with docker and add onnx runtime or optimuim
- add support for pdfs, and videos using sentence transformer embeddings and video captioning models


## to run. do:
 build image:
``` docker build -t filehost .```
 and run:
``` docker run -p 50001 filehost ```
