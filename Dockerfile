FROM python:alpine

# Update OS Packages
RUN apk update && \
    apk upgrade && \
    apk add build-base postgresql postgresql-dev

# Install python packages
WORKDIR /tmp
ADD ./the_dancing_fools_and_feats/requirements.in .
RUN pip install pip-tools
RUN pip-compile
RUN pip uninstall pip-tools -y
RUN pip install -r requirements.txt --no-cache-dir
RUN rm /tmp/*

WORKDIR /app
ADD ./the_dancing_fools_and_feats/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
