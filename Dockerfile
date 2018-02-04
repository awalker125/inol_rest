FROM centos:latest
MAINTAINER Andrew Walker <awalker125@users.noreply.github.com>

# Change to root user
USER root

RUN yum upgrade all \
	&& yum install \
	httpd \
	mod_ssl \
  	python-pip \
  	python-devel \ 
  	gcc \
  	openssl-devel \
  	openldap-devel \
  	libffi-devel \
	&& yum clean all

RUN groupadd -g 678 wsgi && useradd -u 678 -g wsgi wsgi

# Install Docker Compose and ansible
RUN pip install inol_rest

# Change to wsgi user
USER wsgi



