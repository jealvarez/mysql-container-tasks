FROM python:3

WORKDIR /opt/apps

COPY roles roles
COPY playbook.yml playbook.yml
COPY requirements.txt requirements.txt
COPY run.py run.py
COPY docker-entrypoint.sh docker-entrypoint.sh

RUN apt-get update -y \
  && apt-get install -y default-mysql-client \ 
  && pip install ansible \
  && pip install -r /opt/apps/requirements.txt \
  && useradd -m mysql-container-tasks \
  && chown -R mysql-container-tasks /opt/apps \
  && apt-get clean autoclean \
  && apt-get autoremove --yes \
  && rm -rf /var/lib/apt/lists/*

USER mysql-container-tasks

ENTRYPOINT [ "python", "/opt/apps/run.py" ]
