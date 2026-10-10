# Real-time object detector (YOLOv8 + Flask + HTML)

## Setup
    python -m venv venv
    source venv/bin/activate        # Windows: venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python app.py
Open http://127.0.0.1:5000 in Chrome, Edge or Firefox.

Use `127.0.0.1` or `localhost` - browsers only allow webcam access on those
addresses (or HTTPS).

## Tips
- Faster: keep `yolov8n.pt`, lower SEND_WIDTH in index.html, or run on a GPU
  (install a CUDA build of PyTorch; ultralytics uses it automatically).
- More accurate: change to `yolov8s.pt` or `yolov8m.pt` in app.py.
- Detects the 80 COCO classes (person, car, dog, cell phone, ...).
  For custom objects, train your own weights and pass that .pt file to YOLO().

## Downloading results
- **Image tab:** "Download result" saves the annotated image as `detection.png`.
- **Webcam / Video tabs:** "Save snapshot" saves the current annotated frame as PNG;
  "Record video" starts recording the annotated stream, and "Stop and download"
  saves it as `detection.webm` (video only, no audio).
