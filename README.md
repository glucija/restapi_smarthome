# Rest API for smart home ASR

First build Docker image:

``` docker build -t kaldi-asr .```

Run Docker container:

``` docker run -d --name kaldi-asr-server - v your_absolute_path_to_asr_directory/asr:/asr -p 5000:5000 kaldi-asr ```
