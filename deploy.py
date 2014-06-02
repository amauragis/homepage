#!/usr/bin/env python3

from sh import scp, glob
import yaml
import sys
import logger

f = open("deploy.yaml")
deploy_data = yaml.load(f)

logger.info("Deploying to " + deploy_data["host"]["address"] + ":" + deploy_data["host"]["path"]);
try:
	scp("-r", glob("html/*"), deploy_data["host"]["address"] + ":" + deploy_data["host"]["path"]);
	logger.info("Deployment complete.")
except Exception:
	logger.error("Deployment failed.")
