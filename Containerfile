FROM registry.access.redhat.com/ubi9-minimal:9.4-949.1714662671
LABEL name="destiny/consulting_assistants_api" \
      version="0.8.0" \
      maintainer="Mihai Criveti <crmihai1@ie.ibm.com>" \
      description="libica and icali" \
      com.redhat.license_terms="https://www.redhat.com/en/about/red-hat-end-user-license-agreements#UBI" \
      help="For more information visit https://pages.github.ibm.com/destiny/consulting_assistants_api/"

ARG PYTHON_VERSION=3.11
ENV PYTHON_VERSION=$PYTHON_VERSION

# INSTALL PYTHON
RUN microdnf -y upgrade --refresh --best --nodocs --noplugins --setopt=install_weak_deps=0 \
    && microdnf -y install --nodocs --setopt=install_weak_deps=0 vim shadow-utils python$PYTHON_VERSION gcc-c++ python$PYTHON_VERSION-devel\
    && microdnf clean all \
    && rm -rf /var/cache/* /var/log/dnf* /var/log/yum.*
RUN useradd -u 1001 -g 0 -m -d /app -s /bin/bash default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python$PYTHON_VERSION 1

# COPY application
COPY --chown=1001:0 .ica.env.sample /app/.config/icacli/.ica.env
COPY --chown=1001:0 . /app

# SWITCH TO REGULAR USER
RUN chown -R 1001:0 /app \
    && chmod -R g=u /app
USER 1001
WORKDIR /app
ENV PATH=/app/.venv/bin:/app/bin:$PATH

# INSTALL PYTHON PACKAGES
RUN /bin/bash -c \
    "python3 -m venv /app/.venv \
    && . /app/.venv/bin/activate \
    && python3 -m pip install --upgrade pip pdm \
    && python3 -m pip install .[langchain]"

# COMMAND and ENTRYPOINT:
CMD ["icacli"]
