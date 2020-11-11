echo "# # # Removendo containers anteriores"
docker container rm -f coelhomq

echo ""

echo "# # # Iniciando container: coelhomq"
docker run -d --hostname coelhomq --name coelhomq \
    -p 15672:15672 -p 5672:5672 \
    -e RABBITMQ_DEFAULT_USER=arq30 -e RABBITMQ_DEFAULT_PASS=arq30 \
    rabbitmq:3-management

echo ""

echo "# # # Logs: coelhomq"
docker logs -f coelhomq
