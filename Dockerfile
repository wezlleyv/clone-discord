FROM python
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/discord
WORKDIR /opt/discord
ADD . /opt/discord

ENV DJANGO_SETTINGS_MODULE=core.settings
EXPOSE 8000

RUN pip install -r requirements.txt
RUN python manage.py migrate

VOLUME ["/opt/discord/static"]