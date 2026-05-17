import logging
logging.basicConfig(
    filename='logs/cloudops.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()
