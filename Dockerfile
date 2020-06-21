FROM centos:latest

RUN  yum install python36 -y

RUN  pip3 install --upgrade
RUN  pip3 install keras
RUN  pip3 install pandas
RUN  pip3 install sklearn

RUN  pip3 install https://files.pythonhosted.org/packages/64/c2/b80047c7ac2478f9501676c988a5411ed5572f35d1beff9cae07d321512c/PyYAML-5.3.1.tar.gz  
RUN pip3 install --upgrade  setuptools
RUN pip3 install grpcio==1.27.2
RUN pip3 install tensorflow==1.14
RUN pip3 install tensorflow-estimator==1.14
RUN pip3 install protobuf==3.6
RUN pip3 install termcolor==1.1
RUN pip3 install astor==0.6.0
RUN pip3 install wheel==0.26
RUN pip3 install pillow

RUN mkdir /ml_task/
#COPY  cnn_codes.py  /ml_task/
#COPY  dataset/  /ml_task/dataset/
ENTRYPOINT  [ "python3" ]
CMD [ "/ml_task/cnn_codes.py" ]
