FROM mageai/mageai:llm

ARG PROJECT_NAME=llm
ARG MAGE_CODE_PATH=/home/src
ARG USER_CODE_PATH=${MAGE_CODE_PATH}/${PROJECT_NAME}

WORKDIR ${MAGE_CODE_PATH}

COPY ${PROJECT_NAME} ${PROJECT_NAME}

ENV USER_CODE_PATH=${USER_CODE_PATH}

# Install custom Python libraries and dependencies for your project.
RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
RUN pip3 install --no-cache-dir "git+https://github.com/mage-ai/mage-ai.git@td--create_blocks_tmp3#egg=mage-ai[all]"

ENV PYTHONPATH="${PYTHONPATH}:${MAGE_CODE_PATH}/${PROJECT_NAME}"

CMD ["/bin/sh", "-c", "/app/run_app.sh"]
