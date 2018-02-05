FROM centos:latest
MAINTAINER Andrew Walker <awalker125@users.noreply.github.com>

# Change to root user
USER root



# Install deps
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
	yum -y upgrade && \
	yum -y install \
	httpd \
	mod_ssl \
  	python-pip \
  	python-devel \ 
  	gcc \
  	openssl-devel \
  	openldap-devel \
  	libffi-devel \
	&& yum -y clean all \
	&& rm -rf /var/cache/yum

# Create our wsgi user
RUN groupadd -g 678 wsgi && useradd -u 678 -g wsgi wsgi

# Install the app
RUN pip install pip --upgrade && pip install inol_rest

# Change to wsgi user
USER wsgi
