FROM pykaldi/pykaldi

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/kaldi/src/featbin:/kaldi/src/ivectorbin:/kaldi/src/online2bin:/kaldi/src/rnnlmbin:/kaldi/src/fstbin:$PATH

ENV LC_ALL C.UTF-8
ENV TZ=Europe/Ljubljana
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install nano -y
RUN pip install --upgrade pip \
	pandas \
        pysubs2 \
        librosa \
        tqdm \
        flask
RUN apt-get install cron -y
CMD cd /asr && mkdir temp && python3.6 server.py >> output_server.txt
