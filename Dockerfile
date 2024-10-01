FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /inference_rt_mgt
WORKDIR /inference_rt_mgt
COPY . /inference_rt_mgt

RUN pip3 install -r ./requirements/base.txt

EXPOSE 30304
CMD python3 manage.py runserver 0.0.0.0:30304
