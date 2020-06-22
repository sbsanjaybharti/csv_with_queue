#!/usr/bin/env python3
"""
Import packages
"""
import os
from flask import current_app
from ..utility.rabbit_mq import RabbitMq
import pandas as pd

#############################################################################
# Class declare in single responsible & Factory method design pattern
#############################################################################


class DataProcess:

    def process_start(self, file):

        server = RabbitMq()

        # Panda for cleaning and managing
        col_Names = ["full_name", "email"]  # Add header to data

        df = pd.read_csv(
            os.path.join(current_app.config['UPLOAD_FOLDER'], file),
            sep=',',
            names=col_Names
        )

        # sorting by first name
        df.sort_values("email", inplace=True)

        # dropping ALL duplicte values
        df.drop_duplicates(subset="email", keep=False, inplace=True)

        # displaying data
        for row in df.to_dict(orient='records'):
            server.publish({'name': row['full_name'], 'email': row['email']})
        server.close_connection()
