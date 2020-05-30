FROM  centos


RUN yum install python36 -y
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install pillow 
RUN pip3 install opencv-python
RUN pip3 install numpy

RUN pip3 install pandas
ENTRYPOINT["python36"]


WORKDIR /home/ashutosh/Documents/MLworkshop/MLproject/
COPY mnsit_keras_library_cnn.py /home/ashutosh/Documents/MLworkshop/MLproject/

CMD python36 mnsit_keras_library_cnn.py

