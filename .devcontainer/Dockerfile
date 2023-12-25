FROM python:3.12.1-slim-bookworm

RUN --mount=type=cache,target=/var/cache/apt \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends \
    zsh \
    sudo \
    git-core \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/tmp/* /var/lib/apt/lists/*

ARG USER_NAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $USER_NAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USER_NAME \
    && sudo usermod -aG sudo $USER_NAME \
    && sudo passwd -d $USER_NAME

ENV SHELL=/usr/bin/zsh
RUN chsh $USER_NAME -s $SHELL

WORKDIR /tmp

# Clean
RUN rm -rf /tmp/*

USER $USER_NAME

# Terminal with zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
