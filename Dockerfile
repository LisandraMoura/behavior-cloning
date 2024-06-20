FROM python:3.10.14

RUN pip install \
	numpy \
	pillow \
	eventlet \
        flask \
	python-socketio==4.2.1 \
	torch \
	torchvision

WORKDIR /workspace/

CMD  ["bash"]
