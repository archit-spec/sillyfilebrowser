#  Deeplearning based filebrowser (WIP):

## filebrowser demo 
![demo](https://www.youtube.com/watch?v=CIXq6xz7tHc)

- aim is to provide a better search in filebrowsers when the filebrowsere names are cryptic and it is hard to find an image or a document based on the standard search
## todo
- [x] Make UI
- [ ] Make easily deployable with Docker and add ONNX Runtime or Optimuim
- [ ] Add support for PDFs and videos using Sentence Transformer embeddings and video captioning models
- [ ] Optimize using `joblib` cache


## to run. do:
 build image:
``` docker build -t filehost .```
 and run:
``` docker run -p 50001 filehost ```
