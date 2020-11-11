echo "# # # Removendo containers anteriores"
docker container rm -f my-rabbit

echo ""

echo "# # # Iniciando container: my-rabbit"
docker run -d --hostname my-rabbit --name my-rabbit -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=guildarq30 -e RABBITMQ_DEFAULT_PASS=guildarq30 rabbitmq:3-management

echo ""

echo "# # # Logs: my-rabbit"
docker logs -f my-rabbit
