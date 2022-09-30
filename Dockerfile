FROM ubuntu:20.04

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

ARG USERNAME=ltr-count-python
ARG HOME=/home/$USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID -g $USERNAME --create-home $USERNAME

# Disable setrlimit(RLIMIT_CORE) message
RUN echo "Set disable_coredump false" >> /etc/sudo.conf

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends apt-utils 2>&1 \
    && apt-get -y install  git \
    && apt-get -y install python3-numpy

ENV PATH="$HOME/.local/bin:$PATH"

RUN mkdir /workspaces && chown $USERNAME:$USERNAME workspaces
WORKDIR /workspaces

# Grab the files from gitlab
COPY requirements.txt requirements.txt
COPY .devcontainer/ubuntu.20.04.sh ubuntu.20.04.sh

RUN chown $USERNAME:$USERNAME requirements.txt

# Run the install script
RUN chmod +x ubuntu.20.04.sh && ./ubuntu.20.04.sh

USER $USERNAME

# Install Python dependencies from requirements.txt if it exists
RUN if [ -f "requirements.txt" ]; then pip3 install --user -r requirements.txt; fi

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash
