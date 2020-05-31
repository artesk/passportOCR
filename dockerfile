FROM python:3
RUN apt -y update
RUN apt -y install tesseract-ocr 
RUN apt -y install libtesseract-dev
RUN pip3 install web.py
RUN pip3 install PassportEye
COPY passportOCR.py .
COPY eng.traineddata /usr/share/tesseract-ocr/4.00/tessdata/
EXPOSE 8080
CMD ["python3", "passportOCR.py"]