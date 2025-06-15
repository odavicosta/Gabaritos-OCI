# /backend/Dockerfile

# 1. Imagem Base de Linux com Python
FROM python:3.10-slim-bookworm

# 2. Define o ENV para garantir que o Python não faça buffer da saída, facilitando ver os logs
ENV PYTHONUNBUFFERED 1

# 3. Instala dependências do S.O. (compilador C/C++ etc)
RUN apt-get update && apt-get install -y build-essential gcc g++

# 4. Define o diretório de trabalho dentro do container
WORKDIR /app

# 5. Copia a lista de requisitos e instala as dependências Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# 6. Copia TODO o conteúdo da pasta backend local para a pasta /app no container
COPY . .

# 7. (OPCIONAL) Se você tiver a biblioteca C para compilar, descomente as linhas abaixo
# COPY ./cpp_library /app/cpp_library
# RUN gcc -shared -o libgabarito.so -fPIC /app/cpp_library/seu_codigo.c

# 8. Expõe a porta que o Django vai usar
EXPOSE 8000

# 9. Comando para iniciar o servidor Django
# ATENÇÃO: Substitua "gabarito_oci.wsgi" pelo nome correto do seu projeto se for diferente.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gabarito_oci.wsgi"]
