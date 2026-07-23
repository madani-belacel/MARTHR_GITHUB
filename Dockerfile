FROM python:3.13-slim

# System dependencies for LaTeX and standard build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-latex-recommended \
        texlive-latex-extra \
        texlive-fonts-recommended \
        texlive-fonts-extra \
        texlive-bibtex-extra \
        latexmk \
        make \
        git \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /workspace

ENV TEXINPUTS=/workspace/manuscript/texmf//:
ENV BIBINPUTS=/workspace/manuscript/texmf//:
ENV BSTINPUTS=/workspace/manuscript/texmf//:

CMD ["bash"]
