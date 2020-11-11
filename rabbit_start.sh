echo "# Removendo containers anteriores"
docker container rm -f my-rabbit

echo ""

echo "# Iniciando container: my-rabbit"
docker run -d --hostname my-rabbit --name my-rabbit -p 8080:15672 -p 5672:5672 -p 25676:25676 rabbitmq:3-management

echo ""

echo "# Logs: my-rabbit"
docker logs -f my-rabbit
