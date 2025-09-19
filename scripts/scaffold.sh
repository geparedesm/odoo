CONTAINER_NAME=odoo-odoo-1
MODULE_NAME=custom_web
docker exec $CONTAINER_NAME odoo scaffold $MODULE_NAME /mnt/extra-addons