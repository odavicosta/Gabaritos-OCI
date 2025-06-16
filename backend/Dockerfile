FROM ubuntu:24.04

# Instala as dependências de sistema MÍNIMAS que precisamos
RUN apt-get update && \
    apt-get install -y \
    python3.12 \
    python3-pip \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config

# Define o diretório de trabalho
WORKDIR /app

# 1. Copia as bibliotecas fornecidas para uma pasta padrão do sistema no container
COPY libs/ /usr/local/lib/

# 2. Atualiza o cache de bibliotecas do Linux para que ele encontre os novos arquivos .so
RUN ldconfig

# Continua com a instalação normal das dependências Python
COPY requirements.txt .
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# Copia o resto do código da sua aplicação
COPY . .

# Expõe a porta e inicia o servidor
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gabarito_oci.wsgi"]